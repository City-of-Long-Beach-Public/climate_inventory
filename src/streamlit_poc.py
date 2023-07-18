import pandas as pd
import streamlit as st

# Local Imports
from extractions.CARB.CARBExtractor import CARBExtractor
from extractions.EPAFlight.EPAExtractor import EPAExtractor
from extractions.EPAHub.EPAHubExtractor import EPAHubExtractor
from extractions.EMFAC.EMFACExtractor import EMFACExtractor
from extractions.GoogleEIE.GoogleScraper import GoogleScraper
from extractions.USCensus.USCensus import USCensus


# Initialize Extractors
carb_extractor = CARBExtractor()
epa_extractor = EPAExtractor()
epa_hub_extractor = EPAHubExtractor()
emfac_extractor = EMFACExtractor()
google_scraper = GoogleScraper()
uscensus_extractor = USCensus()


# Add a title to your app
st.title("Data Extraction App")

# Add a selector for the user to choose an extractor
extractor_choice = st.selectbox(
    "Select an extractor",
    ("CARB", "EPAFlight", "EPAHub", "EMFAC", "GoogleEIE", "USCensus"),
)

# When the user presses the 'Run' button, run the appropriate extractor
if st.button("Run"):
    if extractor_choice == "CARB":
        data = carb_extractor.run()  # Assuming each extractor has a run() method
    elif extractor_choice == "EPAFlight":
        data = epa_extractor.get_facilities()
    elif extractor_choice == "EPAHub":
        data = epa_hub_extractor.get_emission_factors_df()
    elif extractor_choice == "EMFAC":
        data = emfac_extractor.get_onroad_data()
    elif extractor_choice == "GoogleEIE":
        data = google_scraper.get_transportation_df()
    elif extractor_choice == "USCensus":
        data = uscensus_extractor.extract_data()

    # Display the data
    st.write(data)
