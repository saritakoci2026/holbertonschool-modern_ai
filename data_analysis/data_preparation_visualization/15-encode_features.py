#!/usr/bin/env python3
"""Encode categorical features for customer churn modeling."""

import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Encode features and return the fitted encoders."""
    df = df.copy()

    # Encode Churn: No -> 0, Yes -> 1
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    # Encode binary columns: No -> 0, Yes -> 1
    binary_cols = [
        'Partner',
        'Dependents',
        'PaperlessBilling',
        'SeniorCitizen'
    ]

    binary_oe = preprocessing.OrdinalEncoder(
        categories=[
            ['No', 'Yes'],
            ['No', 'Yes'],
            ['No', 'Yes'],
            ['No', 'Yes']
        ]
    )

    df[binary_cols] = binary_oe.fit_transform(
        df[binary_cols]
    ).astype(int)

    # Encode TenureGroup in alphabetical order
    tenure_oe = preprocessing.OrdinalEncoder()

    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']]
    ).astype(int)

    # One-hot encode Contract and PaymentMethod
    df = pd.get_dummies(
        df,
        columns=['Contract', 'PaymentMethod'],
        drop_first=True,
        dtype=int
    )

    return df, churn_le, binary_oe, tenure_oe
