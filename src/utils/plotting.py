import os
import matplotlib.pyplot as plt
import pandas as pd
from .constants import NO_COLOR, YES_COLOR, rain_or_not_list


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