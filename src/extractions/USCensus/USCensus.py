# Author: Federico Dominguez Molina
# Description: This script extracts the data from the US Census API.

import requests
import pandas as pd


class USCensus:
    def __init__(self):
        self.API_METADATA = "https://data.census.gov/api/search/metadata/table?id=ACSDT1Y2021.B25040&g=160XX00US0643000"
        self.API_TABLE = "https://data.census.gov/api/access/data/table?id=ACSDT1Y2021.B25040&g=160XX00US0643000"

        self.headers = {
            "authority": "data.census.gov",
            "method": "GET",
            "path": "/table?q=B25040&g=160XX00US0643000&tid=ACSDT1Y2021.B25040",
            "scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "max-age=0",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    def get_metadata_content(self):
        """
        Gets metadata content from API
        """
        r = requests.get(self.API_METADATA, headers=self.headers)
        metadata_content = r.json()
        self.metadata_content = metadata_content["response"]

    def get_mapping_dict(self):
        """
        Gets mapping dictionary from metadata content
        """
        mapping_content = self.metadata_content["response"]["metadataContent"][
            "dimensions"
        ][2]["categories"]
        # Note - M is for margin of error and E is for estimate
        self.mapping_dict = {}

        for item in mapping_content:
            label = item["label"]

            corresponding_ids = item["item_mapping"]
            for corresponding_id in corresponding_ids:
                if "E" in corresponding_id:
                    self.mapping_dict[corresponding_id] = f"{label} Estimate"
                else:
                    self.mapping_dict[corresponding_id] = f"{label} Margin of Error"
