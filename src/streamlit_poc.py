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
    "CARB": CARBExtractor(),
    "EPAFlight": EPAExtractor(),
    "EPAHub": EPAHubExtractor(),
    "EMFAC": EMFACExtractor(),
    "GoogleEIE": GoogleScraper(),
    "USCensus": USCensus(),
}

# Get the current year
current_year = datetime.now().year

# Add a title to your app
st.title("Long Beach Climate Inventory Data Extraction App")
st.sidebar.image("longbeach_logo.png")

extractor_choice = st.selectbox(
    "Select a data source to fetch data", list(extractors.keys())
)

# Add a selector for the user to choose a year in the sidebar
year = st.sidebar.selectbox(
    "Select a year", range(2015, current_year + 1)
)  # Modify the range as needed

# Add a selector for the user to choose an extractor
extractor_choice = st.selectbox(
    "Select an extractor",
    ("CARB", "EPAFlight", "EPAHub", "EMFAC", "GoogleEIE", "USCensus"),
)

# If GoogleEIE is selected, ask the user to choose between transportation and buildings
google_choice = None
if extractor_choice == "GoogleEIE":
    google_choice = st.selectbox("Choose a type", ("Transportation", "Buildings"))


emfac_choice = None
if extractor_choice == "EMFAC":
    emfac_choice = st.selectbox("Choose a type of emissions", ("Onroad", "Offroad"))


# When the user presses the 'Run' button, run the appropriate extractor with the chosen year
if st.button("Run"):
    extractor = extractors[extractor_choice]

    if extractor_choice == "GoogleEIE":
        data = extractor.run(
            year, google_choice
        )  # Assuming the run() method takes a type as second argument
    else:
        data = extractor.run(
            year
        )  # Assuming each extractor has a run() method that takes a year as argument

    # Display the data
    st.write(data)
