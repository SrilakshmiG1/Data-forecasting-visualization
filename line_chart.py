#for linear algebra operations
import numpy as np

# data processing, CSV file I/O (e.g. pd.read_csv)
import pandas as pd

#importing the pandas packages
from pandas import *

#for ignoring the warnings
import warnings
warnings.filterwarnings('ignore')

#interactive visualizing library 
from bokeh.plotting import figure, show, output_file
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

#grouping the data by year and month
temp_df = data.groupby(['Year', 'Month']).sum().reset_index()
#print(temp_df.head)

#plotting the line plot for the data
TOOLS = 'save,pan,box_zoom,reset,wheel_zoom,hover'
p = figure(title="Monthly Modal Prices of Tomato in Kolar Market",x_axis_type="datetime", y_axis_type="linear", plot_height = 400,
           tools = TOOLS, plot_width = 800)
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Modal Price'
p.line(data.Month_Year, data.Modal_Price,line_color="purple", line_width = 3)
p.select_one(HoverTool).tooltips = [('Month_Year', '@x'),('Modal_Price', '@y'),]

#creating the output html file
output_file("line_plot.html", title="Line Chart")

#view in the browser
show(p)



