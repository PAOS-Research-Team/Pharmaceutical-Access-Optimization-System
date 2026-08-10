"""
Uncertainty Quantification (Bootstrap)
------------------------------------------
Wraps any of the models above to produce a CONFIDENCE INTERVAL around
a prediction, not just a point estimate. This directly supports PAOS's
core scientific question: manufacturing decisions under material
uncertainty need an honest sense of how uncertain each prediction is.

Uses bootstrap resampling: model-agnostic (works with the regression,
classification, or forecasting models above without modification) and
requires no distributional assumptions about the errors.
"""

import numpy as np


def bootstrap_prediction_interval(
    model,
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_query: np.ndarray,
    n_iterations: int = 100,
    confidence: float = 0.90,
):
    """
    Retrains `model` on `n_iterations` bootstrap resamples of the
    training data, predicts on X_query each time, and returns the
    median prediction plus a confidence interval from the spread
    of predictions.
    """
    predictions = []
    n_samples = X_train.shape[0]

    for _ in range(n_iterations):
        # Sample with replacement to build one bootstrap training set.
        indices = np.random.choice(n_samples, size=n_samples, replace=True)
        model.train(X_train[indices], y_train[indices], feature_names=[])
        predictions.append(model.predict(X_query))

    predictions = np.array(predictions)
    lower_pct = (1 - confidence) / 2 * 100
    upper_pct = (1 - (1 - confidence) / 2) * 100

    return {
        "median": np.median(predictions, axis=0),
        "lower_bound": np.percentile(predictions, lower_pct, axis=0),
        "upper_bound": np.percentile(predictions, upper_pct, axis=0),
    }
