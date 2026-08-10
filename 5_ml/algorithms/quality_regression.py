"""
Quality Prediction Model (Regression)
----------------------------------------
Predicts a Critical Quality Attribute (CQA) — e.g. dissolution rate,
hardness, potency — as a continuous value from measured material
properties (particle size, moisture content, API purity, etc).

Uses a Random Forest Regressor: robust to non-linear relationships
between raw-material variability and product quality, handles mixed
feature scales without heavy preprocessing, and gives feature
importances that are directly useful for engineering interpretation
(which material property drives quality risk the most).
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


class QualityPredictionModel:
    def __init__(self, n_estimators: int = 200, random_state: int = 42):
        self.model = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=random_state,
        )
        self.feature_names: list[str] = []
        self.is_trained = False

    def train(self, X: np.ndarray, y: np.ndarray, feature_names: list[str]):
        """
        X: material property matrix (rows = batches, cols = properties)
        y: measured CQA values for each batch
        """
        self.feature_names = feature_names
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        self.model.fit(X_train, y_train)
        self.is_trained = True

        # Report held-out performance so engineers can trust the model
        # before using it to guide manufacturing decisions.
        predictions = self.model.predict(X_test)
        return {
            "mean_absolute_error": mean_absolute_error(y_test, predictions),
            "r2_score": r2_score(y_test, predictions),
        }

    def predict(self, X: np.ndarray) -> np.ndarray:
        if not self.is_trained:
            raise RuntimeError("Model must be trained before predicting.")
        return self.model.predict(X)

    def feature_importance(self) -> dict:
        """Which material properties most influence predicted quality."""
        if not self.is_trained:
            raise RuntimeError("Model must be trained before inspecting importances.")
        return dict(zip(self.feature_names, self.model.feature_importances_))
