#!/usr/bin/env python3
"""Plot numeric features against customer churn."""

import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """Plot numeric feature distributions by churn."""
    churn_no = df[df['Churn'] == 'No'][col].dropna()
    churn_yes = df[df['Churn'] == 'Yes'][col].dropna()

    plt.figure(figsize=(12, 8))
    plt.hist(
        [churn_no, churn_yes],
        bins=30,
        label=['No', 'Yes']
    )

    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.legend(title='Churn')
    plt.show()

    return None
