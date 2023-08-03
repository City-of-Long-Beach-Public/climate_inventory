import streamlit as st
from datetime import datetime

# Local Imports
from extractions.CARB.CARBExtractor import CARBExtractor
from extractions.EPAFlight.EPAExtractor import EPAExtractor
from extractions.EPAHub.EPAHubExtractor import EPAHubExtractor
from extractions.EMFAC.EMFACExtractor import EMFACExtractor
from extractions.GoogleEIE.GoogleScraper import GoogleScraper
from extractions.USCensus.USCensus import USCensus

# Get current year
current_year = datetime.now().year


# Helper functions - saving csv to cache
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8-sig")


# Constants
INITIAL_YEAR = 2015
LAST_AVAILABLE_YEAR = 2021
LOGO_URL = "https://www.parklb.com/media/1031/longbeachlogostacked480px72dpi.png"
data_type_dict = {}

# Initialize Extractors

extractors = {
    "CARB": {
        "object": CARBExtractor(),
        "options": ["Emissions", "URLs"],
        "years": list(range(INITIAL_YEAR, current_year + 1)),
    },
    "EPAFlight": {
        "object": EPAExtractor(),
        "options": [],
        "years": list(range(INITIAL_YEAR, LAST_AVAILABLE_YEAR + 1)),
    },
    "EPAHub": {
        "object": EPAHubExtractor(),
        "options": ["Emissions", "URLs"],
        "years": list(range(INITIAL_YEAR, current_year + 1)),
    },
    "EMFAC": {
        "object": EMFACExtractor(),
        "options": ["Onroad", "Offroad"],
        "years": list(range(INITIAL_YEAR, current_year + 1)),
    },
    "GoogleEIE": {
        "object": GoogleScraper(),
        "options": ["Transportation", "Buildings"],
        "years": list(range(INITIAL_YEAR, current_year + 1)),
    },
    "USCensus": {
        "object": USCensus(),
        "options": ["1Y", "5Y"],
        "years": list(range(INITIAL_YEAR, LAST_AVAILABLE_YEAR + 1)),
    },
}

# App layout
st.title("Long Beach Climate Inventory Data Extraction App")
st.sidebar.image(LOGO_URL)

# Add a selector for the user to choose an extractor
extractor_choice = st.selectbox(
    "Select a data source to fetch data", list(extractors.keys())
)

# Add the  'all' option to the years list
years_list = extractors[extractor_choice]["years"]
years_list.insert(0, "All years")

# Add a selector for the user to choose a year in the sidebar
year = st.sidebar.selectbox("Select a year", years_list)  # Modify the range as needed

data_type = None
# If there are options for the selected extractor, let the user choose an option
if extractors[extractor_choice]["options"]:
    data_type = st.selectbox("Choose a type", extractors[extractor_choice]["options"])

# When the user presses the 'Run' button, run the appropriate extractor with the chosen year and option
if st.button("Run"):
    extractor = extractors[extractor_choice]["object"]

    if data_type:
        data_type_dict["option"] = data_type
        data = extractor.run(
            year,
            data_type_dict,
        )
    else:
        data = extractor.run(year)

    # Display the data
    # Remove one column from the dataframe until it can be displayed
    try:
        st.write(data)
        success = True

    except Exception as err:
        print(err)
        st.write(data.to_html(), unsafe_allow_html=True)

    if not data.empty:
        csv = convert_df(data)
        st.download_button(
            "Download csv file",
            csv,
            f"results_{extractor_choice}.csv",
            "text/csv",
            key="download-csv",
        )

    else:
        st.markdown(
            "<h4 style='text-align: center; color: black;'>No data found for the specified criteria</h4>",  # noqa: E501
            unsafe_allow_html=True,
        )
