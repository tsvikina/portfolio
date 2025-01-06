import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize = (10,8))
    plt.scatter(
        data['Year'], data['CSIRO Adjusted Sea Level'], color = 'blue', alpha = 0.6)  
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')



    # Create first line of best fit
    years_all = pd.Series(range(1880, 2051))
    # first_line 
    slope, intercept, _, _, _= linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    first_line = slope*years_all + intercept
    plt.plot(years_all, first_line, color = 'red', label = 'Fit: All Data')

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    years_intervals_recent = pd.Series(range(2000, 2051))
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    second_line = slope_recent*years_intervals_recent + intercept_recent
    plt.plot(years_intervals_recent, second_line, color = 'green', label = 'Fit: Data (2000 Onwards)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
draw_plot()