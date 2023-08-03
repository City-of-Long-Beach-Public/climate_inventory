"""Scrapes data from the California Air Resources Board website"""
# California Air Resources Board

import requests
import pandas as pd
from io import BytesIO
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://ww2.arb.ca.gov/mrr-data"

headers = {
    "Authority": "ww2.arb.ca.gov",
    "Method": "GET",
    "Path": "/mrr-data",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",  # noqa: E501
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "If-None-Match": "1689111602",
    "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",  # noqa: E501
}


class CARBExtractor:
    def __init__(self):
        self.URL = URL
        self.headers = headers
        self.undesired_words = ["facility", "entity", "archive"]
        # Number of records needed for a row to be considered valid
        self.NA_THRESH = 10
        # Getting urls and names
        self.get_urls_df()

        # Current year
        self.current_year = datetime.now().year
        self.years_list = list(range(2015, self.current_year + 1))

    def get_urls_df(self):
        """
        Gets dataframe with all of the urls with GHG data and
        their corresponding names

        Returns:
            df (pd.DataFrame): dataframe with urls and names
        """
        r = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(r.content, "html.parser")
        soup
        # Get all hrefs and their text
        href_dicts = []
        hrefs = soup.find_all("a")
        for href in hrefs:
            href_dict = {}
            text = href.text
            url = href.get("href")

            if "xls" in url:
                href_dict["name"] = text
                href_dict["url"] = f"https:{url}"

                href_dicts.append(href_dict)

        df = pd.DataFrame(href_dicts)

        self.urls_df = df

    @staticmethod
    def convert_cols_to_str(mega_df):
        """Numeric cols are converted to float"""
        for col in mega_df.columns:
            mega_df[col] = mega_df[col].astype(str)

        return mega_df

    def get_longbeach_data(self, year=None):
        """
        Gets dataframe with all of the urls with GHG data for
        the city of Long Beach

        Returns:
            df (pd.DataFrame): dataframe with urls and names
        """
        xlsx_urls = self.urls_df["url"].tolist()

        xlsx_urls = [
            url
            for url in xlsx_urls
            if not any(word in url for word in self.undesired_words)
        ]
        mega_df = pd.DataFrame([])
        for xlsx_url in xlsx_urls:
            if any(word in xlsx_url.lower() for word in self.undesired_words):
                print(f"Skipping {xlsx_url}")
                continue
            response = requests.get(xlsx_url)
            xls_file = pd.ExcelFile(BytesIO(response.content))
            # Create a dictionary of DataFrames, with sheet name as key
            dataframes = {
                sheet_name: xls_file.parse(sheet_name)
                for sheet_name in xls_file.sheet_names
            }

            key_of_interest = None
            for key in dataframes.keys():
                if "GHG Data" in key:
                    if year is not None:
                        if str(year) in key:
                            key_of_interest = key
                    else:
                        key_of_interest = key

            if key_of_interest is None:
                print(f"Skipping {xlsx_url}")
                continue

            ghg_data = dataframes[key_of_interest]
            # Remove rows with several NaNs
            ghg_data = ghg_data.dropna(thresh=self.NA_THRESH)
            # First row is the header
            ghg_data.columns = ghg_data.iloc[0]
            # Remove rows
            longbeach_df = ghg_data.loc[
                ghg_data.loc[:, "City"] == "Long Beach"
            ].reset_index(drop=True)
            # Remove columns with NaNs
            longbeach_df = longbeach_df.dropna(axis=1, how="all")
            # Remove \n in column names
            longbeach_df.columns = longbeach_df.columns.str.replace("\n", " ")
            # First column is not needed
            mega_df = pd.concat([mega_df, longbeach_df], ignore_index=True)

        # Index name removal
        mega_df = mega_df.rename_axis(None, axis=1)
        mega_df.fillna("Not Available", inplace=True)
        # Converting all columns to string
        self.longbeach_df = mega_df

    def get_all_yearly_data(self):
        """Gets all the yearly data from EPAHub"""
        all_yearly_data = pd.DataFrame([])
        for year in self.years_list:
            try:
                print(f"Getting data for year {year}...")
                self.get_longbeach_data(year)
                all_yearly_data = pd.concat(
                    [all_yearly_data, self.longbeach_df], ignore_index=True
                )
            except Exception as err:
                print(err)
                print(f"Data not found for year {year}")

        return all_yearly_data

    def run(self, year, data_type_dict):
        """
        Runs scraper for CARB data for a given year
        """
        option = data_type_dict["option"]
        if option == "Emissions":
            if year == "All years":
                data = self.get_all_yearly_data()
            else:
                try:
                    self.get_longbeach_data(year)
                    data = self.longbeach_df
                except Exception as e:
                    print(e)
                    print(f"Could not get data for {year}")
                    data = pd.DataFrame([])
        else:
            self.get_urls_df()
            data = self.urls_df

        return data
