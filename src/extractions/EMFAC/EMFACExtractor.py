# EMFAC Extraction - LGB

# Standard imports
import requests
import pandas as pd
from datetime import datetime

# Local imports
from extractions.EMFAC.emfac_payloads import onroad_payload, offroad_payload

# Global variables


class EMFACExtractor:
    def __init__(self):
        self.ONROAD_API = "https://arb.ca.gov/emfac/handler/request_emfac2021.php"
        self.OFFROAD_API = "https://arb.ca.gov/emfac/handler/request_orion.php"

        self.headers = {
            "Host": "arb.ca.gov",
            "Origin": "https://arb.ca.gov",
            "Referer": "https://arb.ca.gov/emfac/emissions-inventory/4592b9779ca87f0b0d21346bbf923961ad4d3b24",
            "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        self.onroad_payload = onroad_payload
        self.offroad_payload = offroad_payload
        self.INITIAL_MODEL_YEAR = 1965

    def get_onroad_data(self, initial_year=2015, final_year=None):
        """Get data from EMFAC API Onroad endpoint
        and parse it into a DF

        Args:
            payload (dict): Payload for EMFAC API
            initial_year (int, optional): First year of data. Defaults to 2015.
            final_year (int, optional): Last year of data. Defaults to None.

        Returns:
            df (pd.DataFrame): DataFrame with data from EMFAC API
        """

        if final_year is None:
            final_year = 2050

        years = list(range(initial_year, final_year + 1))
        model_years = list(range(self.INITIAL_MODEL_YEAR, final_year + 1))
        new_payload = self.onroad_payload.copy()
        new_payload["form"]["calendarYear"] = years
        new_payload["form"]["calendarYearStart"] = initial_year
        new_payload["form"]["calendarYearEnd"] = final_year
        new_payload["form"]["calendarYearStartSelected"] = initial_year
        new_payload["form"]["calendarYearEndSelected"] = final_year
        new_payload["form"]["modelYear"] = model_years
        new_payload["form"]["modelYearStart"] = self.INITIAL_MODEL_YEAR
        new_payload["form"]["modelYearEnd"] = final_year
        new_payload["form"]["modelYearStartSelected"] = self.INITIAL_MODEL_YEAR
        new_payload["form"]["modelYearEndSelected"] = final_year

        response = requests.post(
            self.ONROAD_API, json=new_payload, headers=self.headers
        )
        content = response.json()
        df = pd.DataFrame(content["output"])

        return df

    def get_offroad_data(self, initial_year=2015, final_year=None):
        """
        Get data from EMFAC API for Offroad data

        Args:
            payload (dict): Payload for EMFAC API
            initial_year (int, optional): First year of data. Defaults to 2015.
            final_year (int, optional): Last year of data. Defaults to None.

        Returns:
            df (pd.DataFrame): DataFrame with data from EMFAC API
        """

        if final_year is None:
            final_year = 2050

        years = list(range(initial_year, final_year + 1))
        model_years = list(range(self.INITIAL_MODEL_YEAR, final_year + 1))

        new_payload = self.offroad_payload.copy()
        new_payload["form"]["calendarYear"] = years
        new_payload["form"]["calendarYearStart"] = initial_year
        new_payload["form"]["calendarYearEnd"] = final_year
        new_payload["form"]["calendarYearStartSelected"] = initial_year
        new_payload["form"]["calendarYearEndSelected"] = final_year
        new_payload["form"]["modelYear"] = model_years
        new_payload["form"]["modelYearStart"] = self.INITIAL_MODEL_YEAR
        new_payload["form"]["modelYearEnd"] = final_year
        new_payload["form"]["modelYearStartSelected"] = self.INITIAL_MODEL_YEAR
        new_payload["form"]["modelYearEndSelected"] = final_year

        response = requests.post(
            self.OFFROAD_API, json=new_payload, headers=self.headers
        )
        content = response.json()
        df = pd.DataFrame(content["output"])

        return df

    def run(self, year, choice):
        """
        Runs scraper for EMFAC data, getting the info
        from the given year and choice (Onroad or Offroad)
        """
        if choice == "Onroad":
            df = self.get_onroad_data(year)
        else:
            df = self.get_offroad_data(year)

        if year != "All years":
            print(f"Getting data for {year}...")
            df = df.loc[df.loc[:, "Calendar Year"] == str(year), :]

        return df
