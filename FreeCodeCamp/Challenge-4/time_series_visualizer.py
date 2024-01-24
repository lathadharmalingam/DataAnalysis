import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('/content/drive/MyDrive/timeseries.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df = df[(df['value'] >= df['value'].quantile(0.025)) &
(df['value'] <= df['value'].quantile(0.975)) ]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(17, 6))
    df.set_index('date')
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year']=df.index.year
    df['month']=df.index.month
    df['month'] = df.index.strftime('%B')
    group = df.groupby(['year','month'])
    group = group.mean().reset_index()
    group = group.pivot(index='year', columns='month', values='value')
    ax = sns.barplot(x=group['year'], y=group['value'], hue=group['month'], data=group, palette='Set1')
    # Draw bar plot
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper left')
    fig = ax.get_figure()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    ax = sns.boxplot(data=df_box, x=df_box['year'],y=df_box['value'])
    ax = sns.boxplot(data=df_box, x=df_box['month'],y=df_box['value'])
    ax.set_ylabel('Page views')



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
