"""Class to extract data from EPA Hub website"""
import re
import requests
import pandas as pd
from io import BytesIO
from datetime import datetime
from bs4 import BeautifulSoup


class EPAHub:
    def __init__(self):
        self.URL = "https://www.epa.gov/climateleadership/ghg-emission-factors-hub"
        self.headers = {
            "Authority": "www.epa.gov",
            "Method": "GET",
            "Path": "/climateleadership/ghg-emission-factors-hub",
            "Scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "If-None-Match": "1689275341",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        self.undesired_words = ["pdf"]
        self.NA_THRESH = 2

    def get_urls_df(self):
        """
        Gets dataframe with all of the urls with GHG data and
        their corresponding names
        """
        r = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(r.content, "html.parser")
        # Get all hrefs and their text
        href_dicts = []
        hrefs = soup.find_all("a")
        for href in hrefs:
            href_dict = {}
            text = href.text
            url = href.get("href")

            if "GHG" not in text:
                continue

            if "xls" in url:
                href_dict["name"] = str(text).replace("\n", "")
                href_dict["url"] = f"https:{url}"
                href_dicts.append(href_dict)

            elif "pdf" in url:
                href_dict["name"] = str(text).replace("\n", "")
                href_dict["url"] = f"https:{url}"

                href_dicts.append(href_dict)

        # Create dataframe
        self.urls_df = pd.DataFrame.from_dict(href_dicts)

    def get_emission_factors_df(self, year):
        """
        Downloads excel from the corresponding year
        """
        xlsx_urls = self.urls_df["url"].tolist()
        FIRST_INDEX = 0
        SECOND_INDEX = 1

        xlsx_urls = [
            url
            for url in xlsx_urls
            if not any(word in url for word in self.undesired_words)
        ]

        urls_of_interest = [url for url in xlsx_urls if str(year) in url]

        if urls_of_interest:
            xlsx_url = urls_of_interest[FIRST_INDEX]
        else:
            xlsx_url = xlsx_urls[SECOND_INDEX]

        response = requests.get(xlsx_url, headers=self.headers)
        xls_file = pd.ExcelFile(BytesIO(response.content))
        # Create a dictionary of DataFrames, with sheet name as key
        dataframes = {
            sheet_name: xls_file.parse(sheet_name)
            for sheet_name in xls_file.sheet_names
        }
        key_of_interest = None
        for key in dataframes.keys():
            if "Hub" in key:
                key_of_interest = key

        ghg_data = dataframes[key_of_interest]
        ghg_data = ghg_data.dropna(axis=1, how="all")
        # Remove rows with several NaNs
        ghg_data = ghg_data.dropna(axis=0, thresh=self.NA_THRESH)
        ghg_data.reset_index(drop=True, inplace=True)
