#!/usr/bin/env python3
"""Module for Lasso Regression model creation."""

from sklearn import linear_model


def lasso_regression(random_state):
    """Create and return an untrained Lasso Regression model."""
    model = linear_model.Lasso(random_state=random_state)
    return model
