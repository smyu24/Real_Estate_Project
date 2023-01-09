import datacommons_pandas as dc

# Import other libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

states = dc.get_places_in(['country/USA'], 'State')['country/USA']
data = dc.build_multivariate_dataframe(states)
data.head()

data.insert(0, 'name', data.index.map(dc.get_property_values(data.index, 'name')).str[0])

data.head(5)

#dc.build_multivariate_dataframe(["country/USA", "geoId/06", "geoId/06085"],["Count_Person", "Median_Age_Person", "UnemploymentRate_Person"])

# labor force participation rate = labor force / working age population
# (Labor Force ÷ Civilian Noninstitutional Population) x 100
# The working age population is defined as those aged 15 to 64.


"""
About: Lifetime Cancer Risk
dcid: AirPollutant_Cancer_Risk
typeOf: StatisticalVariable
Properties
Property	Value	Provenance
dcid	
AirPollutant_Cancer_Risk
typeOf	
StatisticalVariable

constraintProperties	
pollutantHealthRisk

description	
Probability of contracting cancer over a 70 year lifetime due to air pollutant exposure

measuredProperty	
lifetimeContractionProbability

memberOf	
Atmosphere by Pollutant Health Risk (dcid: dc/g/Atmosphere_PollutantHealthRisk)

name	
Lifetime Cancer Risk

pollutantHealthRisk	
Cancer

populationType	
Atmosphere

statType	
measuredValue

\
About: CO2 Emissions Per Capita
dcid: Amount_Emissions_CarbonDioxide_PerCapita
\
About: Hazard Index: Non Carcinogenic Respiratory Hazard
dcid: AirPollutant_Respiratory_Hazard
typeOf: StatisticalVariable
\
About: Air Quality Index
dcid: AirQualityIndex_AirPollutant
typeOf: StatisticalVariable
\
About: Amount of Debt: Government
dcid: Amount_Debt_Government
typeOf: StatisticalVariable

"""