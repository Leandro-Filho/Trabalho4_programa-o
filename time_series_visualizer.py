import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
low = df["value"].quantile(0.025)
high = df["value"].quantile(0.975)
df = df[(df["value"] >= low) & (df["value"] <= high)]


def draw_line_plot(df):
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df['date'], df['value'], color='red', linewidth=1)
    ax.set_title("Gráficos diários de visitas a páginas 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("value")
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot(df):
    # Copy and modify data for monthly bar plot
    df['years'] = pd.to_datetime(df['date']).dt.year
    df['months'] = pd.to_datetime(df['date']).dt.month
    df_bar = df.groupby(['years', 'months'])['value'].mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(
        data=df_bar,
        x='years',
        y='value',
        hue='months',
        palette='tab10',
        ax=ax
    )
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend(title="Months")

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
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    fig.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
