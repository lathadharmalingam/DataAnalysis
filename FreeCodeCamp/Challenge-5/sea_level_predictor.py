import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
  

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    plt.figure(figsize=(15,7))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    years_future = range(1880, 2051)
    line_fit = slope * years_future + intercept
    plt.plot(years_future, line_fit, color='red', label='Line of Best Fit (All Data)')
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'],df_recent['CSIRO Adjusted Sea Level'])
    line_fit_recent = slope_recent * years_future + intercept_recent
    plt.plot(years_future, line_fit_recent, color='green', label='Line of Best Fit (2000 Onward)')

    # Create second line of best fit


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()