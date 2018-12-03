# For linear algebra operations
import numpy as np 

# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd

#Importing all the classes 
from pandas import *

#data visualization using plots
from matplotlib import *

#For ignoring the warnings
import warnings
warnings.filterwarnings('ignore')

#interactive visualizing library 
from bokeh.plotting import figure, show, output_file, output_notebook 
from bokeh.palettes import Spectral11, colorblind, Inferno, BuGn, brewer
from bokeh.models import HoverTool, value, LabelSet, Legend, ColumnDataSource,LinearColorMapper,BasicTicker, PrintfTickFormatter, ColorBar


#datetime operations
from datetime import *

#Reading the data from csv file
data = pd.read_csv('kolar_market.csv', parse_dates=['Month_Year'])
print(data.head())

#extracting the month and year from data
data['Month'] = data.Month_Year.apply(lambda x: x.month)
data['Year'] = data.Month_Year.apply(lambda x: x.year)

#grouping the data based on year and month
temp_df = data.groupby(['Year', 'Month']).sum().reset_index()
print(temp_df.head)

#Rectangular plot of data using bokeh 
TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom,tap"
p = figure(title="Month-Year wise Arrivals(Quintal)", tools=TOOLS, toolbar_location='above')
source = ColumnDataSource(temp_df)
colors = brewer['BuGn'][9]
colors = colors[::-1]
mapper = LinearColorMapper(palette=colors, low=temp_df.Arrivals.min(), high=temp_df.Arrivals.max())
p.rect(x="Year", y="Month",width=2,height=1,source = source,  
    fill_color={
        'field': 'Arrivals',
        'transform': mapper
    },line_color=None)
color_bar = ColorBar(
    color_mapper=mapper,
    major_label_text_font_size="10pt",
    ticker=BasicTicker(desired_num_ticks=len(colors)),
    formatter=PrintfTickFormatter(),
    label_standoff=6,
    border_line_color=None,
    location=(0, 0))
p.add_layout(color_bar, 'right')
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Month'
p.select_one(HoverTool).tooltips = [('Year', '@Year'),('Month', '@Month'), ('Number of Arrivals', '@Arrivals')]

#creating the output
output_file("dataview.html", title="Data Collection from Kolar Market")

#showing the output in browser
show(p)  
