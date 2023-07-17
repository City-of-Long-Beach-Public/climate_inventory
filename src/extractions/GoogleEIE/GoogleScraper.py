import requests
import pandas as pd


class GoogleScraper:
    def __init__(self):
        self.API = "https://alkalienvironmentalinsights-pa.googleapis.com/v1/releases/public/features/ChIJWdeZQOjKwoARqo8qxPo6AKE?key=AIzaSyBofhq7e63zkJXbp-r6SZ8V9MLjQuP01a8&language_code=en-US&alt=protojson"

        self.headers = {
            "Authority": "alkalienvironmentalinsights-pa.googleapis.com",
            "Method": "GET",
            "Path": "/v1/releases/preview/features?locale=en-US&key=AIzaSyBofhq7e63zkJXbp-r6SZ8V9MLjQuP01a8&alt=protojson",
            "Scheme": "https",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://insights.sustainability.google",
            "Referer": "https://insights.sustainability.google/places/ChIJWdeZQOjKwoARqo8qxPo6AKE/download?hl=en-US",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "X-Client-Data": "CJK2yQEIo7bJAQipncoBCIuEywEIlKHLAQiFoM0B",
        }

    def initial_request(self):
        """
        Initial call to Google API to get the data
        """
        r = requests.get(self.API, headers=self.headers)
        self.content = r.json()

    def get_buildings_data(self):
        """
        Gets buildings data from response
        and parses it into a dataframe
        """

        # NOTE: A lot of things are hard coded because the data is formatted
        # in a very specific way. If the data format changes, this function
        # will need to be updated.

        buildings_raw = self.content[8][10]
        residential_data = buildings_raw[0]
        non_residential_data = buildings_raw[1]

        buildings_dict_list = []

        for list_content in [residential_data, non_residential_data]:
            buildings_dict = {}
            buildings_dict["Type"] = list_content[0]
            buildings_dict["co2e tons"] = list_content[1]
            buildings_dict["number of buildings"] = list_content[2]
            buildings_dict["energy intensity"] = list_content[3][0][2]
            buildings_dict["floor space"] = list_content[3][0][-1]
            additonal_data = list_content[3][0][7]
            buildings_dict["electricity intensity"] = additonal_data[0][1]
            buildings_dict["electricity fraction"] = additonal_data[0][2]
            buildings_dict["natural gas intensity"] = additonal_data[1][1]
            buildings_dict["natural gas fraction"] = additonal_data[1][2]
            buildings_dict["diesel oil intensity"] = additonal_data[2][1]
            buildings_dict["diesel oil fraction"] = additonal_data[2][2]
            buildings_dict["propane intensity"] = additonal_data[3][1]
            buildings_dict["propane fraction"] = 0

            buildings_dict_list.append(buildings_dict)

        self.buildings_df = pd.DataFrame.from_dict(buildings_dict_list)
