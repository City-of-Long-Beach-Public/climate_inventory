import requests
import pandas as pd


class EPAExtractor:
    def __init__(self):
        self.SERVICE_API = (
            "https://ghgdata.epa.gov/ghgp/service/populateSectorDashboard/"
        )
        self.FACILITIES_API = "https://ghgdata.epa.gov/ghgp/service/listFacility/"
        self.headers = {
            "Host": "ghgdata.epa.gov",
            "Origin": "https://ghgdata.epa.gov",
            "Referer": "https://ghgdata.epa.gov/ghgp/main.do",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    def get_facilities(self, payload_facilities, year_to_query=2021):
        """
        Makes a request to the FACILITIES_API and returns a dataframe of the results.

        Parameters
        ----------
        payload_facilities : dict
        """

        payload_facilities["reportingYear"] = str(year_to_query)

        r_facilities = requests.post(
            self.FACILITIES_API, json=payload_facilities, headers=self.headers
        )
        content = r_facilities.json()
        unit = content["unit"]
        year = content["year"]
        df_facilities = pd.DataFrame(content["data"]["rows"])
        df_facilities.drop(columns=["id", "icons"], inplace=True)
        df_facilities.rename(columns={"total": "metric_tons_CO2"}, inplace=True)
        df_facilities.loc[:, "unit"] = unit
        df_facilities.loc[:, "year"] = year

        return df_facilities
