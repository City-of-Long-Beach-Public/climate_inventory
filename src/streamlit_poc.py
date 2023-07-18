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
