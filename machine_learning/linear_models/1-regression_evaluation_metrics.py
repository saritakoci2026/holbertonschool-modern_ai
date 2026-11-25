#!/usr/bin/env python3
"""Calculate evaluation metrics for regression models."""

import numpy as np
from sklearn import metrics


def evaluation_metrics_for_regression(y_true, y_pred):
    """Calculate MSE, RMSE, MAE, and R2 score."""
    mse = metrics.mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = metrics.mean_absolute_error(y_true, y_pred)
    r2 = metrics.r2_score(y_true, y_pred)

    return (mse, rmse, mae, r2)
