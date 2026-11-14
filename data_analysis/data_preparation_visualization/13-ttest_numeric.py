#!/usr/bin/env python3
"""Perform Welch's t-tests on continuous numeric features."""

from scipy import stats


def ttest_numeric(df):
    """Test differences in numeric feature means by Churn."""
    results = {}

    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        if col == 'Churn' or df[col].nunique() <= 2:
            continue

        churn_yes = df[df['Churn'] == 'Yes'][col].dropna()
        churn_no = df[df['Churn'] == 'No'][col].dropna()

        t_stat, p_value = stats.ttest_ind(
            churn_yes,
            churn_no,
            equal_var=False
        )

        results[col] = p_value

    return results
