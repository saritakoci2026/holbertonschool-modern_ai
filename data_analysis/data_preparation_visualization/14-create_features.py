#!/usr/bin/env python3
"""Create new features from the customer churn dataset."""

import pandas as pd


def create_features(df):
    """Create NumServices and TenureGroup features."""
    service_cols = [
        'MultipleLines',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies'
    ]

    # Count services marked as Yes.
    num_services = df[service_cols].eq('Yes').sum(axis=1)

    # Count DSL and Fiber optic as internet service subscriptions.
    num_services += df['InternetService'].isin(
        ['DSL', 'Fiber optic']
    ).astype(int)

    df['NumServices'] = num_services

    # Group customers according to their tenure.
    df['TenureGroup'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+']
    )

    # Drop original columns used to create the new features.
    df.drop(
        columns=service_cols + ['InternetService', 'tenure'],
        inplace=True
    )

    return df
