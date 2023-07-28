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
years_list = list(range(2015, current_year + 1))
# Add the  'all' option
years_list.insert(0, "All years")


# Saving csv in cache
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode("utf-8-sig")


# App layout
st.title("Long Beach Climate Inventory Data Extraction App")
st.sidebar.image("climate_inventory\src\longbeach_logo.png")

# Add a selector for the user to choose an extractor
extractor_choice = st.selectbox(
    "Select a data source to fetch data", list(extractors.keys())
)

# Add a selector for the user to choose a year in the sidebar
year = st.sidebar.selectbox("Select a year", years_list)  # Modify the range as needed

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

    # Display the data
    try:
        data = data.astype(str) if "CARB" in extractor_choice else data
        st.write(data)

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
