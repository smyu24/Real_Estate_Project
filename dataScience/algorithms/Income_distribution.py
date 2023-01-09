"""
The American Community Survey (published by the US Census) annually reports the number of individuals in a given income bracket at the state level. 
We can use this information, stored in Data Commons, to visualize disparity in income for each state in the US. 
Our goal for this tutorial will be to generate a plot that visualizes the total number of individuals across a given set of income brackets for a given state.
"""

# Import the Data Commons Pandas library
import datacommons_pandas as dc

# Import other libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

states = dc.get_places_in(['country/USA'], 'State')['country/USA']


# A list of income bracket StatisticalVariables
income_brackets = [
                   "Count_Household_IncomeOfUpto10000USDollar",
                   "Count_Household_IncomeOf10000To14999USDollar",
                   "Count_Household_IncomeOf15000To19999USDollar",
                   "Count_Household_IncomeOf20000To24999USDollar",
                   "Count_Household_IncomeOf25000To29999USDollar",
                   "Count_Household_IncomeOf30000To34999USDollar",
                   "Count_Household_IncomeOf35000To39999USDollar",
                   "Count_Household_IncomeOf40000To44999USDollar",
                   "Count_Household_IncomeOf45000To49999USDollar",
                   "Count_Household_IncomeOf50000To59999USDollar",
                   "Count_Household_IncomeOf60000To74999USDollar",
                   "Count_Household_IncomeOf75000To99999USDollar",
                   "Count_Household_IncomeOf100000To124999USDollar",
                   "Count_Household_IncomeOf125000To149999USDollar",
                   "Count_Household_IncomeOf150000To199999USDollar",

                   "Count_Household_IncomeOf200000Or250000USDollar",

                   "Count_Household_IncomeOf250000OrMoreUSDollar",
]

data = dc.build_multivariate_dataframe(states, income_brackets)
print(data.head())


# Get all state names and store it in a column "name"
# Get the first name, if there are multiple for a state
data.insert(0, 'name', data.index.map(dc.get_property_values(data.index, 'name')).str[0])

data.head(5)

# Bar chart endpoints (for calculating bar width)
label_to_range = {
  "Count_Household_IncomeOfUpto10000USDollar": [0, 9999],
  "Count_Household_IncomeOf10000To14999USDollar": [10000, 14999],
  "Count_Household_IncomeOf15000To19999USDollar": [15000, 19999],
  "Count_Household_IncomeOf20000To24999USDollar": [20000, 24999],
  "Count_Household_IncomeOf25000To29999USDollar": [25000, 29999],
  "Count_Household_IncomeOf30000To34999USDollar": [30000, 34999],
  "Count_Household_IncomeOf35000To39999USDollar": [35000, 39999],
  "Count_Household_IncomeOf40000To44999USDollar": [40000, 44999],
  "Count_Household_IncomeOf45000To49999USDollar": [45000, 49999],
  "Count_Household_IncomeOf50000To59999USDollar": [50000, 59999],
  "Count_Household_IncomeOf60000To74999USDollar": [60000, 74999],
  "Count_Household_IncomeOf75000To99999USDollar": [75000, 99999],
  "Count_Household_IncomeOf100000To124999USDollar": [100000, 124999],
  "Count_Household_IncomeOf125000To149999USDollar": [125000, 149999],
  "Count_Household_IncomeOf150000To199999USDollar": [150000, 199999],

  "Count_Household_IncomeOf200000Or250000USDollar": [200000, 250000],

  "Count_Household_IncomeOf200000OrMoreUSDollar": [250000, 300000],
}

def plot_income(data, state_name):
  # Assert that specified "state_name" is a valid state name
  frame_search = data.loc[data['name'] == state_name].squeeze()
  if frame_search.shape[0] == 0:
    print('{} does not have sufficient income data to generate the plot!'.format(state_name))
    return
  
  # Print the resulting series
  data = frame_search[1:]

  # Calculate the lengths without intervals
  widths_without_interval = []
  for bracket in income_brackets:
    r = label_to_range[bracket] 
    widths_without_interval.append(int((r[1] - r[0]) / 18))

  # Calculate the x-axis positions
  pos, total = [], 0
  for l in widths_without_interval:
    pos.append(total + (l // 2))
    total += l

  # Calculate the bar lengths
  widths = []
  for bracket in income_brackets:
    r = label_to_range[bracket] 
    # 50 here to be the intervals between bars
    widths.append(int((r[1] - r[0]) / 18 - 50))

  # Plot the histogram
  plt.figure(figsize=(12, 10))
  plt.xticks(pos, income_brackets, rotation=90)
  plt.grid(True)
  plt.bar(pos, data.values, widths, color='b', alpha=0.3)

  # Return the resulting frame.
  return frame_search

def add_name_col(df):
  # Add a new column called name, where each value is the name for the place dcid in the index.
  df['name'] = df.index.map(dc.get_property_values(df.index, 'name'))
  
  # Keep just the first name, instead of a list of all names.
  df['name'] = df['name'].str[0]


add_name_col(data)
print(data.head())

