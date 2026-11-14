#!/usr/bin/env python3
"""Plot a correlation heatmap for continuous numeric features."""

import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Display an annotated heatmap of numeric feature correlations."""
    plt.figure(figsize=(6, 5))

    numeric_df = df.select_dtypes(include=['number'])
    correlation = numeric_df.corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap='coolwarm',
        vmin=-1,
        vmax=1
    )

    plt.show()
