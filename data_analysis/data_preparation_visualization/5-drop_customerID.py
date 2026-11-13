#!/usr/bin/env python3
"""Remove the customerID column from a DataFrame."""


def drop_customerID(df):
    """Drop the customerID column.

    Args:
        df (pd.DataFrame): DataFrame containing customerID.

    Returns:
        pd.DataFrame: DataFrame without customerID.
    """
    return df.drop(columns=['customerID'])
