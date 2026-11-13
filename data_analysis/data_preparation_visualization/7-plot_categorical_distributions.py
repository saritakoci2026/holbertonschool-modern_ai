#!/usr/bin/env python3
"""Plot distributions of categorical features in a DataFrame."""

import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Display bar plots for categorical columns.

    Args:
        df (pd.DataFrame): DataFrame containing categorical features.
        columns_to_plot (list): Optional list of columns to plot.

    Returns:
        None
    """
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include=['object']).columns
            if col != 'Churn'
        ]

    if not columns_to_plot:
        return None

    n_cols = 3
    n_rows = (len(columns_to_plot) + n_cols - 1) // n_cols

    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(15, 5 * n_rows), squeeze=False
    )
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', labelrotation=45)

    for i in range(len(columns_to_plot), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()

    return None
