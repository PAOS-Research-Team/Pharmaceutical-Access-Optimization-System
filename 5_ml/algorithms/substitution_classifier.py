"""
Material Substitution Classifier
------------------------------------
Given a candidate replacement material's measured properties, predicts
whether it is "SUITABLE" or "NOT SUITABLE" as a substitute for the
original material without breaching Critical Quality Attribute limits.

Uses Gradient Boosting: strong default performance on small/medium
tabular datasets (typical for lab-scale pharma data) and produces
well-calibrated class probabilities, useful for risk-based
decision-making rather than a hard yes/no.
"""

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


class MaterialSubstitutionClassifier:
    def __init__(self, random_state: int = 42):
        self.model = GradientBoostingClassifier(random_state=random_state)
        self.is_trained = False

    def train(self, X: np.ndarray, y: np.ndarray) -> dict:
        """
        X: candidate material property matrix
        y: binary labels, 1 = suitable substitute, 0 = not suitable
        """
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        self.model.fit(X_train, y_train)
        self.is_trained = True
        predictions = self.model.predict(X_test)
        return classification_report(y_test, predictions, output_dict=True)

    def predict_suitability(self, X: np.ndarray) -> np.ndarray:
        """Returns probability of being a suitable substitute (0-1)."""
        if not self.is_trained:
            raise RuntimeError("Model must be trained before predicting.")
        return self.model.predict_proba(X)[:, 1]
