#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Remove all duplicate rows from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to process.

    Returns:
        pd.DataFrame: DataFrame without duplicate rows.
    """
    return df.drop_duplicates()
