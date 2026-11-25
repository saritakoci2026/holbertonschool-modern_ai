#!/usr/bin/env python3
"""Module for SHAP model explainability."""

import shap


def get_shap_explainer_and_values(model, X_train, X_test):
    """Create a SHAP explainer and calculate SHAP values."""
    explainer = shap.Explainer(model, X_train)
    shap_values = explainer(X_test)
    return explainer, shap_values
