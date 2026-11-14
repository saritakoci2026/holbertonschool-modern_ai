#!/usr/bin/env python3
"""Scale numeric features for customer churn modeling."""

from sklearn import preprocessing


def scale_numeric(df):
    """Standardize MonthlyCharges and TotalCharges."""
    df = df.copy()

    scaler = preprocessing.StandardScaler()

    numeric_cols = ['MonthlyCharges', 'TotalCharges']

    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    return df
