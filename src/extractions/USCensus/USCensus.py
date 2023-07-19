# Author: Federico Dominguez Molina
# Description: This script extracts the data from the US Census API.

import requests
import pandas as pd


class USCensus:
    def __init__(self, year_to_query=2021, type_estimate="1Y"):
        if type_estimate not in ["1Y", "5Y"]:
            raise ValueError('type_estimate must be either "1Y" or "5Y"')
        self.year_to_query = year_to_query
        self.type_estimate = type_estimate
        self.API_METADATA = f"https://data.census.gov/api/search/metadata/table?id=ACSDT{self.type_estimate}{self.year_to_query}.B25040&g=160XX00US0643000"
        self.API_TABLE = f"https://data.census.gov/api/access/data/table?id=ACSDT{self.type_estimate}{self.year_to_query}.B25040&g=160XX00US0643000"

        self.headers = {
            "authority": "data.census.gov",
            "method": "GET",
            "path": f"/table?q=B25040&g=160XX00US0643000&tid=ACSDT1Y{self.year_to_query}.B25040",
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
        self.metadata_content = r.json()
        self.dataset_info = self.metadata_content["response"]["metadataContent"][
            "dataset"
        ]

    def get_mapping_dict(self):
        """
        Gets mapping dictionary from metadata content
        """
        DATA_INDEX = 2
        mapping_content = self.metadata_content["response"]["metadataContent"][
            "dimensions"
        ][DATA_INDEX]["categories"]
        # Note - M is for margin of error and E is for estimate
        self.mapping_dict = {}

        for item in mapping_content:
            label = item["label"]

            corresponding_ids = item["item_mapping"]
            for corresponding_id in corresponding_ids:
                if "E" in corresponding_id:
                    self.mapping_dict[corresponding_id] = f"{label}-Estimate"
                else:
                    self.mapping_dict[corresponding_id] = f"{label}-Margin of Error"

    def get_data_table(self):
        """
        Gets data table from API and parses the data
        into a clean dataframe
        """
        LABEL_INDEX = 0
        DATA_INDEX = 1
        r = requests.get(self.API_TABLE, headers=self.headers)
        table_content = r.json()["response"]

        labels = table_content["data"][LABEL_INDEX]
        data = table_content["data"][DATA_INDEX]

        df = pd.DataFrame.from_dict({"labels": labels, "data": data})
        self.location = df.loc[df["labels"] == "NAME"]["data"].values[LABEL_INDEX]
        df = df.loc[df["labels"].isin(self.mapping_dict.keys())]
        df.replace(self.mapping_dict, inplace=True)
        df.dropna(inplace=True)

        # Split 'labels' into 'label' and 'metric'
        df[["label", "metric"]] = df["labels"].str.rsplit("-", n=1, expand=True)

        # Pivot to get 'Estimate' and 'Margin of Error' as separate columns
        df_pivot = df.pivot(index="label", columns="metric", values="data")

        # Reset index
        df_pivot = df_pivot.reset_index()

        # Rename columns
        df_pivot.columns.name = ""
        df_pivot.rename(
            columns={"Estimate": "estimate", "Margin of Error": "margin of error"},
            inplace=True,
        )

        self.parsed_data = df_pivot

    def complete_df(self):
        """
        Completes dataframe with dataset information
        """
        self.parsed_data["year"] = self.dataset_info["vintage"]
        self.parsed_data["name"] = self.dataset_info["name"]
        self.parsed_data["program"] = self.dataset_info["program"]
        self.parsed_data["subprogram"] = self.dataset_info["subProgram"]
        self.parsed_data["location"] = self.location

    def extract_data(self):
        """
        Extracts data from API
        """
        print(
            f"Extracting data from US Census API, {self.year_to_query}, {self.type_estimate}"
        )
        try:
            self.get_metadata_content()
            print("Obtained metadata content")
            self.get_mapping_dict()
            print("Obtained mapping dictionary")
            self.get_data_table()
            print("Obtained data table")
            self.complete_df()
            print("Completed dataframe")
        except Exception as e:
            print(
                f"Error extracting data from US Census API (data may not be available for {self.year_to_query}, {self.type_estimate})"
            )
            print(e)

    def run(self, year_to_query, type_estimate):
        """Calls census API and returns parsed data"""

        self.API_METADATA = f"https://data.census.gov/api/search/metadata/table?id=ACSDT{type_estimate}{year_to_query}.B25040&g=160XX00US0643000"
        self.API_TABLE = f"https://data.census.gov/api/access/data/table?id=ACSDT{type_estimate}{year_to_query}.B25040&g=160XX00US0643000"
        try:
            self.extract_data()
            data = self.parsed_data
        except Exception as e:
            print(e)
            data = pd.DataFrame()

        return data
