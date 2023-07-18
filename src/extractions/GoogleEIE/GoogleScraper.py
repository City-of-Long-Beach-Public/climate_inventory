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

        # Mapping params
        self.trip_types_dict = {0: "INBOUND", 1: "OUTBOUND", 2: "IN-BOUNDARY"}
        self.mode_dict = {
            1: "AUTOMOBILE",
            5: "TRAM",
            7: "BUS",
            9: "CYCLING",
            10: "ON FOOT",
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

    @staticmethod
    def get_gpc_metrics(df):
        # If travel bound is in-boundary, then the gpc distance is the same as the full distance
        # otherwise, it is half of the full distance
        df.loc[:, "gpc distance km"] = df.loc[:, "full distance km"]
        df.loc[df.loc[:, "travel bound"] != "IN-BOUNDARY", "gpc distance km"] = (
            df.loc[df.loc[:, "travel bound"] != "IN-BOUNDARY", "full distance km"] / 2
        )

        df.loc[:, "gpc co2e tons"] = df.loc[:, "full co2e tons"]
        df.loc[df.loc[:, "travel bound"] != "IN-BOUNDARY", "gpc co2e tons"] = (
            df.loc[df.loc[:, "travel bound"] != "IN-BOUNDARY", "full co2e tons"] / 2
        )

        return df

    def get_transportation_df(self):
        """
        Gets the transortation emissions from the raw response
        """
        dfs = []
        transportation_raw = self.content[11]

        for year_data in transportation_raw:
            year = year_data[9]
            trip_type_data = year_data[19]
            counter = 0
            for trip_type_sub in trip_type_data:
                transport_dicts = []
                data_list = trip_type_sub[3]
                for row in data_list:
                    transport_dict = {}
                    transport_dict["mode"] = row[0]
                    transport_dict["travel bound"] = counter
                    transport_dict["trips"] = row[1]
                    transport_dict["full distance km"] = row[4]
                    transport_dict["factor 1"] = row[2]
                    transport_dict["factor 2"] = row[3]
                    if transport_dict["factor 1"]:
                        transport_dict["full co2e tons"] = (row[4] * row[3]) / row[2]
                    else:
                        transport_dict["full co2e tons"] = 0
                    transport_dicts.append(transport_dict)
                trip_type_df = pd.DataFrame.from_dict(transport_dicts)
                trip_type_df.loc[:, "year"] = year
                counter += 1

                dfs.append(trip_type_df)
        self.transportation_df = pd.concat(dfs, ignore_index=True)
        # Replace the travel bound column with the actual travel bound
        self.transportation_df.loc[:, "travel bound"] = self.transportation_df.loc[
            :, "travel bound"
        ].map(self.trip_types_dict)
        self.transportation_df.loc[:, "mode"] = self.transportation_df.loc[
            :, "mode"
        ].map(self.mode_dict)

        # Get GPC metrics
        self.transportation_df = self.get_gpc_metrics(self.transportation_df)
