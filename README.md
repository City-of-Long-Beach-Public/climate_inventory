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

The webscraped site is the [EPAHub Website](https://www.epa.gov/climateleadership/ghg-emission-factors-hub) This website contains the emission factors for several categories, including electricity, vehicles and waste. The scraper is very similar to the CARB one, where the user selects a year, which is associated with an excel file that is downloaded and parsed. 

There is also the option to only get the dataframe with the corresponding urls so the user can download the excel file themselves.


**Google - Environmental Insights Explorer (GoogleEIE)**

This scraper gets the Long Beach data from the [Google EIE Website](https://insights.sustainability.google/places/ChIJWdeZQOjKwoARqo8qxPo6AKE/download?hl=en-US). This website contains the emissions per sector for Long Beach. The scraper is done by calling their API.

This was the hardest scraper since the API results are very inconsistent, and they do not have all of the information. For example, the CO2 emissions for the transportation vehicles were not available from the API response, but two 'factors' were available in the response. The code then calculates the CO2 emissions by using those two factors and the total distance.

**US Census (USCensus)**

This scraper gets the Long Beach house heating fuel consumption from the [US Census Website](https://data.census.gov/table?q=B25040&g=160XX00US0643000&tid=ACSDT1Y2021.B25040).

The US Census API is queried to get the table from this data. The user has the option to choose the year and the type of estimations (5-year or 1-year).

## Future Work

Some future work that could be done include:

- Adding more scrapers to get more data
- Adding a functionality to the streamlit app to merge as much data as possible into a single dataframe
- Adding a functionality to the streamlit app to upload the data either to a database or a sharepoint folder.

Contact Information:

- Federico Dominguez, fd.molina@outlook.com

