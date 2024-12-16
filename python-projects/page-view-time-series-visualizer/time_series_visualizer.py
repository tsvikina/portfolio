import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col = 'date', parse_dates = True)
print(df.head())

# Clean data
cleaned = (df['value'] >= df['value'].quantile(0.01)) & (df['value'] <= df['value'].quantile(0.99))

df = df[cleaned].copy()
print(df.mean())

def draw_line_plot():
    # Draw line plot
    fig, ax= plt.subplots(figsize = (10, 8))
    sns.lineplot(
        df, 
        x = 'date', 
        y ='value', color = 'darkred'
        )
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

draw_line_plot()

def draw_bar_plot():
    # Add Year and Month columns
    df['Year'] = df.index.year
    df['Month'] = df.index.month_name()

    # Group data and prepare for plotting
    df_grouped = df.groupby(['Year', 'Month'], sort=False)['value'].mean().reset_index()

    # Ensure months are sorted in the correct order
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_grouped['Month'] = pd.Categorical(df_grouped['Month'], categories=month_order, ordered=True)
    df_grouped.sort_values(['Year', 'Month'], inplace=True)

    # Create the bar plot
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(data=df_grouped, x='Year', y='value', hue='Month', hue_order=month_order, palette = 'Set1', ax=ax)

    # Set axis labels and legend
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc = 'upper left')
    plt.tight_layout()

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


draw_bar_plot()

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1,2, figsize = (16,8))

    ax1 = sns.boxplot(data = df_box, x = 'year', y = 'value', ax = ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(data = df_box, x = 'month', y = 'value', order = month_order, ax = ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_box_plot()