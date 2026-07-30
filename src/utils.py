import os
import matplotlib.pyplot as plt
import sys
import numpy as np
import pandas as pd
project_root = os.path.abspath("..")
sys.path.insert(0, project_root)

def separator(title=None, length=50):
    """
    Separator Function to Separate Between Phases in Terminal Visually
    """
    if title:
        print(f"\n{'-' * 10} {title} {'-' * 10}")
    else:
        print('-' * length)



# Professional, muted color palette (replaces default Tokyo Night look)
HIST_COLOR = "#4C72B0"   # muted steel blue — used for all histograms
BAR_COLOR = "#55A868"    # muted green — used for all categorical bar charts
PIE_COLORS = ["#4C72B0", "#DD8452"]  # blue / orange — used for binary pie charts
def set_labels(title, xlabel="", ylabel="Frequency"):
    fontdict = {"fontsize": 12, "fontweight": "bold"}
    plt.title(title, fontdict=fontdict)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)


def highlight_max_bar(ax):
    """Highlight the highest bar in a barplot."""
    max_val = max(bar.get_height() for bar in ax.patches)
    for bar in ax.patches:
        if bar.get_height() == max_val:
            bar.set_color("red")


def save_fig(fig, output_path):
    """Save and close a matplotlib figure."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.tight_layout()
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)




rain_or_not_list = ['Rain Tomorrow', 'No Rain Tomorrow']
NO_COLOR = "#4C72B0"   # blue — RainTomorrow = No
YES_COLOR = "#DD8452"  # orange — RainTomorrow = Yes
def violinplot(df, col):
    col_will_rain = df.loc[df['RainTomorrow'], col].dropna()
    col_no_rain = df.loc[~df['RainTomorrow'], col].dropna()
    plt.violinplot([col_will_rain, col_no_rain], showmedians=True, showextrema=True)
    plt.xticks([1, 2], rain_or_not_list)
    set_labels(f"{col} vs Rain Tomorrow", ylabel=col)
    plt.grid()


def crosstab_barchart(df, categorical_column, bar_kind='bar', figsize=(8, 6)):
    crosstab_result = pd.crosstab(
        index=df[categorical_column], 
        columns=df['RainTomorrow'], 
        normalize='index'
        )
    ax = crosstab_result.plot(
        kind=bar_kind,  # type: ignore
        stacked=True, 
        color=[NO_COLOR, YES_COLOR], 
        figsize=figsize
        )
    set_labels(f"{categorical_column} vs RainTomorrow (Proportion)", xlabel=categorical_column, ylabel="Proportion")
    plt.xticks(rotation=45)
    plt.legend(title="Rain Tomorrow", labels=['No', 'Yes'])
    plt.tight_layout()
    return ax.get_figure()


def save_dataset(df, output_path, name, file_extension='parquet'):
    saving_path = f"{output_path}/{name}.{file_extension}"
    if isinstance(df, pd.Series):
        df = df.to_frame()
    if file_extension == "parquet":
        df.to_parquet(saving_path)



def diff(df, col_a, col_b, new_col):
    df[new_col] = df[col_a] - df[col_b]
    return df

def average(df, col_a, col_b, new_col):
    df[new_col] = (df[col_a] + df[col_b]) / 2
    return df

def interaction(df, col_a, col_b, new_col):
    df[new_col] = df[col_a] * df[col_b]
    return df

def log_transform(df, col, new_col):
    df[new_col] = np.log1p(df[col])
    return df