payload = {
    {
        "form": {
            "output": "Emissions",
            "regionType": "Sub-Area",
            "modelVersion": "emfac2021",
            "modelVersionNumber": {"label": "v1.0.2", "value": "v102_byspeed"},
            "modelVersionNumberLabel": "v1.0.2",
            "modelVersionNumberValue": "v102_byspeed",
            "region": [{"id": "59", "name": "Los Angeles (SC)"}],
            "calendarYear": [
                "2015",
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
                "2022",
                "2023",
            ],
            "season": "Annual",
            "scenario": "exh",
            "vehicleCategoryMode": "emfac202x",
            "vehicleCategory": [
                "LDA",
                "LDT1",
                "LDT2",
                "MDV",
                "MCY",
                "MH",
                "LHD1",
                "LHD2",
                "T6 Public Class 4",
                "T6 Public Class 5",
                "T6 Public Class 6",
                "T6 Public Class 7",
                "T6 Utility Class 5",
                "T6 Utility Class 6",
                "T6 Utility Class 7",
                "T6 Instate Tractor Class 6",
                "T6 Instate Delivery Class 4",
                "T6 Instate Delivery Class 5",
                "T6 Instate Delivery Class 6",
                "T6 Instate Other Class 4",
                "T6 Instate Other Class 5",
                "T6 Instate Other Class 6",
                "T6 Instate Tractor Class 7",
                "T6 Instate Delivery Class 7",
                "T6 Instate Other Class 7",
                "T6 CAIRP Class 4",
                "T6 CAIRP Class 5",
                "T6 CAIRP Class 6",
                "T6 CAIRP Class 7",
                "T6 OOS Class 4",
                "T6 OOS Class 5",
                "T6 OOS Class 6",
                "T6 OOS Class 7",
                "T6TS",
                "T7 Public Class 8",
                "T7 CAIRP Class 8",
                "T7 Utility Class 8",
                "T7 NNOOS Class 8",
                "T7 NOOS Class 8",
                "T7 Other Port Class 8",
                "T7 POAK Class 8",
                "T7 POLA Class 8",
                "T7 Single Concrete/Transit Mix Class 8",
                "T7 Single Dump Class 8",
                "T7 Single Other Class 8",
                "T7 Tractor Class 8",
                "T7 SWCV Class 8",
                "T7IS",
                "PTO",
                "UBUS",
                "SBUS",
                "Motor Coach",
                "OBUS",
                "All Other Buses",
            ],
            "vehicleCategoryOffroadSector": [],
            "modelYearMode": "Aggregate",
            "modelYear": [
                1971,
                1972,
                1973,
                1974,
                1975,
                1976,
                1977,
                1978,
                1979,
                1980,
                1981,
                1982,
                1983,
                1984,
                1985,
                1986,
                1987,
                1988,
                1989,
                1990,
                1991,
                1992,
                1993,
                1994,
                1995,
                1996,
                1997,
                1998,
                1999,
                2000,
                2001,
                2002,
                2003,
                2004,
                2005,
                2006,
                2007,
                2008,
                2009,
                2010,
                2011,
                2012,
                2013,
                2014,
                2015,
                2016,
                2017,
                2018,
                2019,
                2020,
                2021,
                2022,
                2023,
                2024,
            ],
            "modelYearStart": 1971,
            "modelYearEnd": 2024,
            "modelYearStartSelected": 1971,
            "modelYearEndSelected": 2024,
            "speedMode": "Aggregate",
            "speed": [
                5,
                10,
                15,
                20,
                25,
                30,
                35,
                40,
                45,
                50,
                55,
                60,
                65,
                70,
                75,
                80,
                85,
                90,
            ],
            "fuel": [
                {"id": 1, "name": "Gasoline"},
                {"id": 2, "name": "Diesel"},
                {"id": 3, "name": "Electricity"},
                {"id": 4, "name": "Natural Gas"},
                {"id": 5, "name": "Plug-in Hybrid"},
            ],
            "unit": "year",
            "outputCols": {
                "activities": [
                    "Population",
                    "Total VMT",
                    "CVMT",
                    "EVMT",
                    "Trips",
                    "Energy Consumption",
                    "Fuel Consumption",
                ],
                "pollutants": [
                    "NOx",
                    "PM2.5",
                    "PM10",
                    "CO2",
                    "CH4",
                    "N2O",
                    "ROG",
                    "TOG",
                    "CO",
                    "SOx",
                    "NH3",
                ],
                "processes": [
                    "RUNEX",
                    "IDLEX",
                    "STREX",
                    "TOTEX",
                    "PMTW",
                    "PMBW",
                    "TOTAL",
                    "DIURN",
                    "HOTSOAK",
                    "RUNLOSS",
                ],
                "tableColumns": [
                    {"name": "No", "label": "No", "field": "No", "sortable": "true"},
                    {
                        "name": "Calendar Year",
                        "label": "Calendar Year",
                        "field": "Calendar Year",
                        "sortable": "true",
                    },
                    {
                        "name": "Vehicle Category",
                        "label": "Vehicle Category",
                        "align": "left",
                        "field": "Vehicle Category",
                        "sortable": "true",
                    },
                    {
                        "name": "Fuel",
                        "label": "Fuel",
                        "align": "left",
                        "field": "Fuel",
                        "sortable": "true",
                    },
                    {
                        "name": "Population",
                        "label": "Population",
                        "field": "Population",
                        "sortable": "true",
                    },
                    {
                        "name": "Total VMT",
                        "label": "Total VMT",
                        "field": "Total VMT",
                        "sortable": "true",
                    },
                    {
                        "name": "CVMT",
                        "label": "CVMT",
                        "field": "CVMT",
                        "sortable": "true",
                    },
                    {
                        "name": "EVMT",
                        "label": "EVMT",
                        "field": "EVMT",
                        "sortable": "true",
                    },
                    {
                        "name": "Trips",
                        "label": "Trips",
                        "field": "Trips",
                        "sortable": "true",
                    },
                    {
                        "name": "Energy Consumption",
                        "label": "Energy Consumption",
                        "field": "Energy Consumption",
                        "sortable": "true",
                    },
                    {
                        "name": "NOx_RUNEX",
                        "label": "NOx_RUNEX",
                        "field": "NOx_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "NOx_IDLEX",
                        "label": "NOx_IDLEX",
                        "field": "NOx_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "NOx_STREX",
                        "label": "NOx_STREX",
                        "field": "NOx_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "NOx_TOTEX",
                        "label": "NOx_TOTEX",
                        "field": "NOx_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_RUNEX",
                        "label": "PM2.5_RUNEX",
                        "field": "PM2.5_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_IDLEX",
                        "label": "PM2.5_IDLEX",
                        "field": "PM2.5_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_STREX",
                        "label": "PM2.5_STREX",
                        "field": "PM2.5_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_TOTEX",
                        "label": "PM2.5_TOTEX",
                        "field": "PM2.5_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_PMTW",
                        "label": "PM2.5_PMTW",
                        "field": "PM2.5_PMTW",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_PMBW",
                        "label": "PM2.5_PMBW",
                        "field": "PM2.5_PMBW",
                        "sortable": "true",
                    },
                    {
                        "name": "PM2.5_TOTAL",
                        "label": "PM2.5_TOTAL",
                        "field": "PM2.5_TOTAL",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_RUNEX",
                        "label": "PM10_RUNEX",
                        "field": "PM10_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_IDLEX",
                        "label": "PM10_IDLEX",
                        "field": "PM10_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_STREX",
                        "label": "PM10_STREX",
                        "field": "PM10_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_TOTEX",
                        "label": "PM10_TOTEX",
                        "field": "PM10_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_PMTW",
                        "label": "PM10_PMTW",
                        "field": "PM10_PMTW",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_PMBW",
                        "label": "PM10_PMBW",
                        "field": "PM10_PMBW",
                        "sortable": "true",
                    },
                    {
                        "name": "PM10_TOTAL",
                        "label": "PM10_TOTAL",
                        "field": "PM10_TOTAL",
                        "sortable": "true",
                    },
                    {
                        "name": "CO2_RUNEX",
                        "label": "CO2_RUNEX",
                        "field": "CO2_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO2_IDLEX",
                        "label": "CO2_IDLEX",
                        "field": "CO2_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO2_STREX",
                        "label": "CO2_STREX",
                        "field": "CO2_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO2_TOTEX",
                        "label": "CO2_TOTEX",
                        "field": "CO2_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CH4_RUNEX",
                        "label": "CH4_RUNEX",
                        "field": "CH4_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CH4_IDLEX",
                        "label": "CH4_IDLEX",
                        "field": "CH4_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CH4_STREX",
                        "label": "CH4_STREX",
                        "field": "CH4_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "CH4_TOTEX",
                        "label": "CH4_TOTEX",
                        "field": "CH4_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "N2O_RUNEX",
                        "label": "N2O_RUNEX",
                        "field": "N2O_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "N2O_IDLEX",
                        "label": "N2O_IDLEX",
                        "field": "N2O_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "N2O_STREX",
                        "label": "N2O_STREX",
                        "field": "N2O_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "N2O_TOTEX",
                        "label": "N2O_TOTEX",
                        "field": "N2O_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_RUNEX",
                        "label": "ROG_RUNEX",
                        "field": "ROG_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_IDLEX",
                        "label": "ROG_IDLEX",
                        "field": "ROG_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_STREX",
                        "label": "ROG_STREX",
                        "field": "ROG_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_TOTEX",
                        "label": "ROG_TOTEX",
                        "field": "ROG_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_DIURN",
                        "label": "ROG_DIURN",
                        "field": "ROG_DIURN",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_HOTSOAK",
                        "label": "ROG_HOTSOAK",
                        "field": "ROG_HOTSOAK",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_RUNLOSS",
                        "label": "ROG_RUNLOSS",
                        "field": "ROG_RUNLOSS",
                        "sortable": "true",
                    },
                    {
                        "name": "ROG_TOTAL",
                        "label": "ROG_TOTAL",
                        "field": "ROG_TOTAL",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_RUNEX",
                        "label": "TOG_RUNEX",
                        "field": "TOG_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_IDLEX",
                        "label": "TOG_IDLEX",
                        "field": "TOG_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_STREX",
                        "label": "TOG_STREX",
                        "field": "TOG_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_TOTEX",
                        "label": "TOG_TOTEX",
                        "field": "TOG_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_DIURN",
                        "label": "TOG_DIURN",
                        "field": "TOG_DIURN",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_HOTSOAK",
                        "label": "TOG_HOTSOAK",
                        "field": "TOG_HOTSOAK",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_RUNLOSS",
                        "label": "TOG_RUNLOSS",
                        "field": "TOG_RUNLOSS",
                        "sortable": "true",
                    },
                    {
                        "name": "TOG_TOTAL",
                        "label": "TOG_TOTAL",
                        "field": "TOG_TOTAL",
                        "sortable": "true",
                    },
                    {
                        "name": "CO_RUNEX",
                        "label": "CO_RUNEX",
                        "field": "CO_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO_IDLEX",
                        "label": "CO_IDLEX",
                        "field": "CO_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO_STREX",
                        "label": "CO_STREX",
                        "field": "CO_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "CO_TOTEX",
                        "label": "CO_TOTEX",
                        "field": "CO_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "SOx_RUNEX",
                        "label": "SOx_RUNEX",
                        "field": "SOx_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "SOx_IDLEX",
                        "label": "SOx_IDLEX",
                        "field": "SOx_IDLEX",
                        "sortable": "true",
                    },
                    {
                        "name": "SOx_STREX",
                        "label": "SOx_STREX",
                        "field": "SOx_STREX",
                        "sortable": "true",
                    },
                    {
                        "name": "SOx_TOTEX",
                        "label": "SOx_TOTEX",
                        "field": "SOx_TOTEX",
                        "sortable": "true",
                    },
                    {
                        "name": "NH3_RUNEX",
                        "label": "NH3_RUNEX",
                        "field": "NH3_RUNEX",
                        "sortable": "true",
                    },
                    {
                        "name": "Fuel Consumption",
                        "label": "Fuel Consumption",
                        "field": "Fuel Consumption",
                        "sortable": "true",
                    },
                ],
                "visibleCols": [
                    "No",
                    "Calendar Year",
                    "Vehicle Category",
                    "Fuel",
                    "Population",
                    "Total VMT",
                    "CVMT",
                    "EVMT",
                    "Trips",
                    "Energy Consumption",
                    "NOx_RUNEX",
                    "NOx_IDLEX",
                    "NOx_STREX",
                    "NOx_TOTEX",
                    "PM2.5_RUNEX",
                    "PM2.5_IDLEX",
                    "PM2.5_STREX",
                    "PM2.5_TOTEX",
                    "PM2.5_PMTW",
                    "PM2.5_PMBW",
                    "PM2.5_TOTAL",
                    "PM10_RUNEX",
                    "PM10_IDLEX",
                    "PM10_STREX",
                    "PM10_TOTEX",
                    "PM10_PMTW",
                    "PM10_PMBW",
                    "PM10_TOTAL",
                    "CO2_RUNEX",
                    "CO2_IDLEX",
                    "CO2_STREX",
                    "CO2_TOTEX",
                    "CH4_RUNEX",
                    "CH4_IDLEX",
                    "CH4_STREX",
                    "CH4_TOTEX",
                    "N2O_RUNEX",
                    "N2O_IDLEX",
                    "N2O_STREX",
                    "N2O_TOTEX",
                    "ROG_RUNEX",
                    "ROG_IDLEX",
                    "ROG_STREX",
                    "ROG_TOTEX",
                    "ROG_DIURN",
                    "ROG_HOTSOAK",
                    "ROG_RUNLOSS",
                    "ROG_TOTAL",
                    "TOG_RUNEX",
                    "TOG_IDLEX",
                    "TOG_STREX",
                    "TOG_TOTEX",
                    "TOG_DIURN",
                    "TOG_HOTSOAK",
                    "TOG_RUNLOSS",
                    "TOG_TOTAL",
                    "CO_RUNEX",
                    "CO_IDLEX",
                    "CO_STREX",
                    "CO_TOTEX",
                    "SOx_RUNEX",
                    "SOx_IDLEX",
                    "SOx_STREX",
                    "SOx_TOTEX",
                    "NH3_RUNEX",
                    "Fuel Consumption",
                ],
                "allCols": [
                    "No",
                    "Calendar Year",
                    "Vehicle Category",
                    "Fuel",
                    "Population",
                    "Total VMT",
                    "CVMT",
                    "EVMT",
                    "Trips",
                    "Energy Consumption",
                    "NOx_RUNEX",
                    "NOx_IDLEX",
                    "NOx_STREX",
                    "NOx_TOTEX",
                    "PM2.5_RUNEX",
                    "PM2.5_IDLEX",
                    "PM2.5_STREX",
                    "PM2.5_TOTEX",
                    "PM2.5_PMTW",
                    "PM2.5_PMBW",
                    "PM2.5_TOTAL",
                    "PM10_RUNEX",
                    "PM10_IDLEX",
                    "PM10_STREX",
                    "PM10_TOTEX",
                    "PM10_PMTW",
                    "PM10_PMBW",
                    "PM10_TOTAL",
                    "CO2_RUNEX",
                    "CO2_IDLEX",
                    "CO2_STREX",
                    "CO2_TOTEX",
                    "CH4_RUNEX",
                    "CH4_IDLEX",
                    "CH4_STREX",
                    "CH4_TOTEX",
                    "N2O_RUNEX",
                    "N2O_IDLEX",
                    "N2O_STREX",
                    "N2O_TOTEX",
                    "ROG_RUNEX",
                    "ROG_IDLEX",
                    "ROG_STREX",
                    "ROG_TOTEX",
                    "ROG_DIURN",
                    "ROG_HOTSOAK",
                    "ROG_RUNLOSS",
                    "ROG_TOTAL",
                    "TOG_RUNEX",
                    "TOG_IDLEX",
                    "TOG_STREX",
                    "TOG_TOTEX",
                    "TOG_DIURN",
                    "TOG_HOTSOAK",
                    "TOG_RUNLOSS",
                    "TOG_TOTAL",
                    "CO_RUNEX",
                    "CO_IDLEX",
                    "CO_STREX",
                    "CO_TOTEX",
                    "SOx_RUNEX",
                    "SOx_IDLEX",
                    "SOx_STREX",
                    "SOx_TOTEX",
                    "NH3_RUNEX",
                    "Fuel Consumption",
                ],
            },
            "showMap": "true",
            "offroadTable": "null",
            "version": "2022-04-29",
            "calendarYearMode": "Range",
            "calendarYearStartSelected": "2015",
            "calendarYearEndSelected": "2023",
            "calendarYearStart": "2000",
            "calendarYearEnd": "2050",
            "vehicleCategoryAll": "true",
            "modelYearAll": "true",
            "speedAll": "true",
            "fuelAll": "true",
            "output_format": "json",
        },
        "hash": "5aaa9ee6bc4e55a01517e89dd1027911526fb9ee",
    }
}
