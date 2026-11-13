#!/usr/bin/env python3
"""Plot distributions of continuous numerical features."""

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def plot_continuous_distributions(df, columns_to_plot=None):
    """Display histograms with KDE and boxplots for numeric columns.

    Args:
        df (pd.DataFrame): DataFrame containing numerical features.
        columns_to_plot (list): Optional list of columns to plot.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = df.select_dtypes(
            include=[np.number]
        ).columns.tolist()

    n_cols = len(columns_to_plot)

    if n_cols == 0:
        return None

    fig, axes = plt.subplots(n_cols, 2, figsize=(10, 3 * n_cols))

    if n_cols == 1:
        axes = axes.reshape(1, -1)

    for i, col in enumerate(columns_to_plot):
        data = df[col].dropna()

        axes[i, 0].hist(
            data,
            bins=30,
            density=True,
            alpha=0.7,
            edgecolor='black'
        )

        if len(data) > 1 and data.nunique() > 1:
            kde = stats.gaussian_kde(data)
            x = np.linspace(data.min(), data.max(), 200)
            axes[i, 0].plot(x, kde(x), color='red')

        axes[i, 0].set_title(f'{col} Histogram + KDE')
        axes[i, 1].boxplot(data)
        axes[i, 1].set_title(f'{col} Boxplot')

    plt.tight_layout()
    plt.savefig("Task_8.png")
    plt.show()

    return None
