#!/usr/bin/env python3
"""Plot categorical features against customer churn."""

import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Plot the churn rate for each category of a given column."""
    churn_rate = df.groupby(col)['Churn'].apply(
        lambda x: (x == 'Yes').mean()
    )

    plt.figure(figsize=(12, 8))
    churn_rate.plot(kind='bar')

    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)

    plt.show()

    return None
