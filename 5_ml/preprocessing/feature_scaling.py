"""
Feature preprocessing utilities
------------------------------------
Shared scaling/encoding helpers so every ML algorithm in 5_ml/algorithms
consumes consistently prepared features (same scaler fit on training
data only, to avoid data leakage into test/validation sets).
"""

import numpy as np
from sklearn.preprocessing import StandardScaler


def scale_features(X_train: np.ndarray, X_test: np.ndarray | None = None):
    """
    Fit a StandardScaler on X_train only, then transform X_train (and
    X_test if provided). Prevents test-set statistics from leaking
    into the scaling of the training set.
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    if X_test is not None:
        X_test_scaled = scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, scaler
    return X_train_scaled, scaler


def train_test_time_split(series: np.ndarray, test_size: int):
    """
    Chronological split for time-series data (never shuffle time series:
    training must only ever see the past relative to the test window).
    """
    return series[:-test_size], series[-test_size:]
