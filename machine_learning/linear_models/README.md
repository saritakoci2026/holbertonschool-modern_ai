# Linear Regression

## Description

This project contains functions for creating and evaluating Linear Regression models using Scikit-learn.

## Files

- `0-linear_regression.py`: Defines the `Linear_Regression()` function, which creates and returns an untrained Linear Regression model.
- `1-regression_evaluation_metrics.py`: Defines the `evaluation_metrics_for_regression()` function to calculate regression evaluation metrics.

## Functions

### `Linear_Regression()`

Creates and returns an untrained `LinearRegression` model using `sklearn.linear_model`.

### `evaluation_metrics_for_regression(y_true, y_pred)`

Calculates four evaluation metrics for a regression model:

- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- R-squared (R²)

Returns a tuple containing `(mse, rmse, mae, r2)`.

## Requirements

- Python 3
- NumPy
- Scikit-learn
