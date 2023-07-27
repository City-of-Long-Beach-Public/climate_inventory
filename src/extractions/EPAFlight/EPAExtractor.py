import time
import requests
import pandas as pd
from datetime import datetime

# Local imports
from extractions.EPAFlight.epa_payloads import payload_facilities


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
        self.payload_facilities = payload_facilities
        self.current_year = datetime.now().year
        self.years_list = list(range(2015, self.current_year + 1))

    def get_facilities(self, year_to_query=2021):
        """
        Makes a request to the FACILITIES_API and returns a dataframe of the results.

        Parameters
        ----------
        payload_facilities : dict
        """

        payload_facilities["reportingYear"] = str(year_to_query)

        r_facilities = requests.post(
            self.FACILITIES_API, json=self.payload_facilities, headers=self.headers
        )
        content = r_facilities.json()
        unit = content["unit"]
        year = content["year"]
        try:
            df_facilities = pd.DataFrame(content["data"]["rows"])
            df_facilities.drop(columns=["id", "icons"], inplace=True)
            df_facilities.rename(columns={"total": "metric_tons_CO2"}, inplace=True)
            df_facilities.loc[:, "unit"] = unit
            df_facilities.loc[:, "year"] = year
        except Exception:
            print("Data not found")
            df_facilities = pd.DataFrame([])

        return df_facilities

    def get_all_yearly_facilities(self):
        """Gets all of the yearly facilities data and returns a dataframe"""
        all_yearly_data = pd.DataFrame([])
        for year in self.years_list:
            try:
                print(f"Getting data for year {year}...")
                df_facilities = self.get_facilities(year_to_query=year)
                time.sleep(0.25)
            except Exception as err:
                print(err)
                print(f"Data not found for year {year}")
                df_facilities = pd.DataFrame([])
            all_yearly_data = pd.concat(
                [all_yearly_data, df_facilities], ignore_index=True
            )

    def run(self, year):
        """Runs scraper for the given year or all years"""

        if year == "All years":
            data = self.get_all_yearly_facilities()
        else:
            data = self.get_facilities(year_to_query=year)

        return data
