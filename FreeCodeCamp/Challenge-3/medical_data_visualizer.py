import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['BMI'] = df['weight']/((df['height']/100)*2)
df['overweight'] = np.where(df['BMI'] > 25, 1, 0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)
# Draw Categorical Plot
def draw_cat_plot():
  selected_columns = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=selected_columns)
  fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count', height=5, aspect=1)


    # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat =df[(df['ap_lo'] <= df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025)) &
  (df['height'] <= df['height'].quantile(0.975)) &
  (df['weight'] >= df['weight'].quantile(0.025)) &
  (df['weight'] <= df['weight'].quantile(0.975))]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax =plt.figure(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='hot',fmt=".1f",linewidths=0.5, mask=np.triu(corr))
    plt.show()


    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
