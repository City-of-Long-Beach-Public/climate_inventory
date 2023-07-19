import pandas as pd
import streamlit as st
from datetime import datetime

# Local Imports
from extractions.CARB.CARBExtractor import CARBExtractor
from extractions.EPAFlight.EPAExtractor import EPAExtractor
from extractions.EPAHub.EPAHubExtractor import EPAHubExtractor
from extractions.EMFAC.EMFACExtractor import EMFACExtractor
from extractions.GoogleEIE.GoogleScraper import GoogleScraper
from extractions.USCensus.USCensus import USCensus

# Initialize Extractors
extractors = {
    "CARB": {"object": CARBExtractor(), "options": ["Emissions", "URLs"]},
    "EPAFlight": {"object": EPAExtractor(), "options": []},
    "EPAHub": {"object": EPAHubExtractor(), "options": ["Emissions", "URLs"]},
    "EMFAC": {"object": EMFACExtractor(), "options": ["Onroad", "Offroad"]},
    "GoogleEIE": {
        "object": GoogleScraper(),
        "options": ["Transportation", "Buildings"],
    },
    "USCensus": {"object": USCensus(), "options": ["1Y", "5Y"]},
}

# Get the current year
current_year = datetime.now().year

# Add a title to your app
st.title("Long Beach Climate Inventory Data Extraction App")
st.sidebar.image("climate_inventory\src\longbeach_logo.png")

# Add a selector for the user to choose an extractor
extractor_choice = st.selectbox(
    "Select a data source to fetch data", list(extractors.keys())
)

# Add a selector for the user to choose a year in the sidebar
year = st.sidebar.selectbox(
    "Select a year", range(2015, current_year + 1)
)  # Modify the range as needed

option_choice = None
# If there are options for the selected extractor, let the user choose an option
if extractors[extractor_choice]["options"]:
    option_choice = st.selectbox(
        "Choose a type", extractors[extractor_choice]["options"]
    )

# When the user presses the 'Run' button, run the appropriate extractor with the chosen year and option
if st.button("Run"):
    extractor = extractors[extractor_choice]["object"]

    if option_choice:
        data = extractor.run(year, option_choice)
    else:
        data = extractor.run(year)

    # Display the data - parse float columns as needed
    for col in data.columns:
        if data[col].dtype == "int64":
            data[col] = data[col].astype("float64")
    st.write(data)
