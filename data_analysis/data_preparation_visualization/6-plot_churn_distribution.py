#!/usr/bin/env python3
"""Plot the distribution of customer churn classes."""

import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Display the distribution of Churn values.

    Args:
        df (pd.DataFrame): DataFrame containing the Churn column.

    Returns:
        None
    """
    plt.figure(figsize=(12, 8))

    churn_counts = df['Churn'].value_counts()

    colors = [
        'skyblue' if value == 'No' else 'salmon'
        for value in churn_counts.index
    ]

    plt.bar(churn_counts.index, churn_counts.values, color=colors)
    plt.title('Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.show()

    return None
