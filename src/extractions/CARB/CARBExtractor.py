# California Air Resources Board

import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://ww2.arb.ca.gov/mrr-data"

headers = {
    "Authority": "ww2.arb.ca.gov",
    "Method": "GET",
    "Path": "/mrr-data",
    "Scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
}


class CARBExtractor:
    def __init__(self):
        self.URL = URL
        self.headers = headers

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
