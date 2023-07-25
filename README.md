# Climate Inventory

This repository contains several scrapers that pull relevant data for the Green House Gas Emissions Inventory for the City of Long Beach. We also include the `streamlit_app.py` file that contains the streamlit app that allows the user to run the scrapers and download the data.

## Scrapers

The scrapers are located in the `src/extrations` folder. There, there are several scrapers that pull data from different sources. The scrapers are:

**California Air Resources Board (CARB)** 
 
 We scrape the data from the following [website](https://ww2.arb.ca.gov/mrr-data). There, there are several excel files that contain emissions per facility. The code scrapes the excel that the user desires, and filters then by Long Beach. There is also the option to only get the dataframe with the corresponding urls.


**EMFAC** 

The data from the [EMFAC website](https://arb.ca.gov/emfac/emissions-inventory/9e6154b79f6137b0be32ec52da0c7f8c3c6cb03c) is scraped, but this is done through an API call (note: this is not a documented API, and it was found by tracking the requests the website makes when a query is called). 

This website contains the onroad and offroad emissions per vehicle type for the years and county selected. In the API call, the South LA County is selected, along with the selected year.


**Environmental Protection Agency - FLIGHT App (EPAFlight)**

The webscraped site is the [EPAFlight Website](https://ghgdata.epa.gov/ghgp/main.do). This website also shows emissions per facility for the selected city. As with the EMFAC code, the scraping is also done by calling their API and using the adequate payload (which includes the city and the year selected). By default, we select the Long Beach city, and the year is up to the user.

**Environmental Protection Agency - Hub**


**Google - Environmental Insights Explorer (GoogleEIE)**


**US Census (USCensus)**


## Future Work



Contact Information:

