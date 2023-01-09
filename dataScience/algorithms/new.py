>>> datacommons_pandas.build_multivariate_dataframe(["country/USA", "geoId/06", "geoId/06085"],["Count_Person", "Median_Age_Person", "UnemploymentRate_Person"])
#              Median_Age_Person  Count_Person  UnemploymentRate_Person
# place
# country/USA               37.9     328239523                      NaN
# geoId/06                  36.3      39512223                     11.6
# geoId/06085               37.0       1927852                      7.5


#Example: Compare the historic populations, median ages, and unemployment rates of the US, California, and Santa Clara County.


datacommons_pandas.build_multivariate_dataframe(places, stat_vars)
# Required arguments:

# places: The dcid or dcid list of the Place objects to query for.
# stat_vars: The dcid or dcid list of the StatisticalVariable objects to query for.



# General information about this endpoint
# Signature:

datacommons.get_stat_value(place, stat_var, date=None, measurement_method=None,observation_period=None, unit=None, scaling_factor=None)
# Required arguments:

# place: The DCID of the Place to query for.
# stat_var: The DCID of the StatisticalVariable.
# You can find a list of StatisticalVariables with human-readable names here.

# Optional arguments:

# date: The preferred date of observation in ISO 8601 format. If not specified, returns the latest observation.
# measurement_method: The DCID of the preferred measurementMethod value.
# observation_period: The preferred observationPeriod value.
# unit: The DCID of the preferred unit value.
# scaling_factor: The preferred scalingFactor value.
# Assembling the information you will need for a call to the get_stat_value method
# Going into more detail on how to assemble the values for the required arguments:

# place: For this parameter, you will need to specify the DCID (the unique ID assigned by Data Commons to each node in the graph) of the place you are interested in.
# stat_var: The statistical variable whose value you are interested in.
# In addition to these required properties, this method also allows for other, optional arguments. Here are helpful arguments in regular use by Data Commons developers:

# date: Specified in ISO 8601 format. Examples include 2011 (the year 2011), 2019-06 (the month of June in the year 2019), and 2019-06-05T17:21:00-06:00 (5:17PM on June 5, 2019, in CST).

# measurement_method: The technique used for measuring a statistical variable.

# observation_period: The time period over which an observation is made.

# unit: The unit of measurement.

# scaling_factor: Property of statistical variables indicating factor by which a measurement is multiplied to fit a certain format.


#-----------------------------------------------


# What to expect in the return
# The method will return a simple number, like ‘1.20949’ or ‘1431252’.

# Examples
# Example 1: Retrieve the count of men in the state of California.
>>> datacommons.get_stat_value("geoId/05", "Count_Person_Male")
1474705
Example 2: Retrieve the count of men in the state of California in the year 2012.
>>> datacommons.get_stat_value("geoId/05", "Count_Person_Male", date="2012")
1431252
Example 3: Retrieve the number of people in Bosnia and Herzegovina as counted by the Bosnian census.
>>> datacommons.get_stat_value("country/BIH", "Count_Person", measurement_method="BosniaCensus")
3791622
Example 4: Retrieve the death count in Miami-Dade County over a period of one year.
>>> datacommons.get_stat_value("geoId/12086", "Count_Death", observation_period="P1Y")
20703
Example 5: Retrieve the distrubtion of the drug naloxone in Miami-Dade County in grams.
>>> datacommons.get_stat_value("geoId/12086", "RetailDrugDistribution_DrugDistribution_Naloxone", unit="Grams")
118.79
Example 6: Retrieve the percentage of nominal GDP spent by the government of the Gambia on education.
>>> datacommons.get_stat_value("country/GMB", "Amount_EconomicActivity_ExpenditureActivity_EducationExpenditure_Government_AsFractionOf_Amount_EconomicActivity_GrossDomesticProduction_Nominal", scaling_factor="100.0000000000")
2.43275
Error Returns
If there is no value associated with the requested property, nan is returned:

>>> datacommons.get_stat_value("geoId/1001", "Count_Person_Male")
nan
If you do not pass a required positional argument, a TypeError is returned:

>>> datacommons.get_stat_value("geoId/1001")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: get_stat_value() missing 1 required positional argument: 'stat_var'



Statistical Variables
https://docs.datacommons.org/statistical_variables.html