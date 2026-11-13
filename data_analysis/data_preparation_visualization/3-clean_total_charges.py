#!/usr/bin/env python3
"""Handle missing values in the TotalCharges column."""


def clean_total_charges(df, method='drop'):
    """Clean missing values in the TotalCharges column.

    Args:
        df (pd.DataFrame): DataFrame containing missing values.
        method (str): Strategy to handle missing values.

    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    cleaned_df = df.copy()

    if method == 'drop':
        cleaned_df = cleaned_df.dropna(subset=['TotalCharges'])

    elif method == 'median':
        median = cleaned_df['TotalCharges'].median()
        cleaned_df['TotalCharges'] = (
            cleaned_df['TotalCharges'].fillna(median)
        )

    elif method == 'impute':
        cleaned_df['TotalCharges'] = cleaned_df[
            'TotalCharges'
        ].fillna(
            cleaned_df['MonthlyCharges'] * cleaned_df['tenure']
        )

    else:
        raise ValueError("Invalid method")

    return cleaned_df
