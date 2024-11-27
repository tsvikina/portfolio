import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight']/(df['height']/100)**2
df['overweight'] = np.where(bmi > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# 4
def draw_cat_plot():
    df_cat = pd.melt(df, id_vars=['id', 'cardio'], value_vars=['gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'], var_name='feature', value_name='value').sort_values(by=['id', 'feature']).reset_index(drop=True)

    # Create the catplot
    fig = sns.catplot(
        data=df_cat, 
        x='feature', 
        hue='value', 
        col='cardio', 
        kind='count'
    )
    fig.savefig('catplot.png')

    # Correct way to access axes of FacetGrid object
    ax = fig.axes[0]  # This should work now since fig.axes will give access to subplots if there are any
    return fig, ax

draw_cat_plot()

def draw_heat_map():
    # 11
    condition_bp = df['ap_lo'] <= df['ap_hi']
    condition_height = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    condition_weight = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))

    combined_conditions = condition_bp & condition_height & condition_weight
    df_heat = df[combined_conditions].copy()
    print(df_heat.head(5))

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(10, 8))  # You already have ax here, no need for fig.axes[0]

    sns.heatmap(
        corr, 
        mask=mask,
        annot=True,          
        fmt=".2f",  # Ensure two decimal places
        cmap='coolwarm',      
        center=0,
        square=True,         
        linewidths=0.5,      
        cbar_kws={"shrink": 0.5}
    )

    fig.savefig('heatmap.png')
    return fig, ax

draw_heat_map()
