#!/usr/bin/env python3
"""Module for Ridge Regression model creation."""

from sklearn import linear_model


def ridge_regression(random_state):
    """Create and return an untrained Ridge Regression model."""
    model = linear_model.Ridge(random_state=random_state)
    return model
