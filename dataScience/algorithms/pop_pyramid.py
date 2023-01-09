"""
Population Pyramid; Youthful states
[https://usafacts.org/articles/population-pyramids-every-state/]
"""
# UPLOAD A CSV AND ADJUST ACCORDINGLY

import pandas as pd
import numpy as np
import random

# Visualisation
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import plotly.io as pio

# Load Data
csv = '../input/FOLDERNAME/FILENAME.csv'
df = pd.read_csv(csv)

# Clean
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

# View
df.head()

# Custom Function to Plot Pyramid
def plotPyramid (cntry):
  temp = df[df['Country'] == cntry].reset_index(drop=True, inplace=False)
  temp_df = temp.groupby(['Age']).agg({'M':'sum','F':'sum'})

  # Plot
  layout = go.Layout(yaxis=go.layout.YAxis(title='Age'),
                   xaxis=go.layout.XAxis(
                       range=[-20000000, 20000000],
                       tickvals=[-20000000,-10000000,-1000000, -100000, -10000, -1000, 0, 1000, 10000, 100000, 1000000, 10000000,20000000],
                       ticktext=[100000000,10000000,1000000, 100000, 10000, 1000, 0, 1000, 10000, 100000, 1000000, 10000000,100000000],
                       title=cntry + ' Population Count'),
                   barmode='overlay',
                   bargap=0.1)
  
  data = [go.Bar(y=temp_df.index,
               x=-temp_df['M'],
               orientation='h',
               name='Men',
               hoverinfo='x',
               marker=dict(color='#937666')
               ),
          go.Bar(y=temp_df.index,
               x=temp_df['F'],
               orientation='h',
               name='Women',
               #text=-1 * women_bins.astype('int'),
               hoverinfo='x',
               marker=dict(color='#3D3A4B')
               )]

  return pio.show(dict(data=data, layout=layout))