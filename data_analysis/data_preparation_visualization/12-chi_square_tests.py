#!/usr/bin/env python3
"""Perform chi-square tests on categorical features."""

import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Perform chi-square independence tests against Churn."""
    results = {}

    categorical_cols = df.select_dtypes(
        include=['object', 'category', 'bool']
    ).columns.tolist()

    # Include numeric categorical columns such as SeniorCitizen.
    for col in df.columns:
        if col != 'Churn' and col not in categorical_cols:
            if df[col].nunique() <= 10:
                categorical_cols.append(col)

    for col in categorical_cols:
        if col == 'Churn':
            continue

        contingency_table = pd.crosstab(df[col], df['Churn'])
        chi2, p_value, dof, expected = stats.chi2_contingency(
            contingency_table
        )
        results[col] = p_value

    return results
