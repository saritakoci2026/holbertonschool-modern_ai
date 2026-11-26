#!/usr/bin/env python3
"""Create a logistic regression classification model."""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Create and return an untrained logistic regression model."""
    model = linear_model.LogisticRegression(
        random_state=random_state
    )
    return model
