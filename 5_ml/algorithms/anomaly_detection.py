"""
Manufacturing Anomaly Detection
------------------------------------
Flags batches/process runs whose sensor or material-property readings
deviate abnormally from the learned "normal operating" distribution,
BEFORE they translate into an out-of-spec quality failure.

Uses Isolation Forest: unsupervised (no labeled failure examples
needed, which is realistic since failures are rare), and scales well
to high-dimensional process data (temperature, pressure, humidity,
mixing time, etc. all at once).
"""

import numpy as np
from sklearn.ensemble import IsolationForest


class ManufacturingAnomalyDetector:
    def __init__(self, contamination: float = 0.05, random_state: int = 42):
        # contamination = expected proportion of anomalous batches in training data.
        self.model = IsolationForest(contamination=contamination, random_state=random_state)
        self.is_trained = False

    def fit(self, X: np.ndarray):
        """X: process/sensor readings from known-good historical batches."""
        self.model.fit(X)
        self.is_trained = True

    def flag_anomalies(self, X: np.ndarray) -> np.ndarray:
        """Returns True for rows flagged as anomalous, False for normal."""
        if not self.is_trained:
            raise RuntimeError("Detector must be fit before use.")
        # IsolationForest returns -1 for anomalies, 1 for normal.
        return self.model.predict(X) == -1

    def anomaly_score(self, X: np.ndarray) -> np.ndarray:
        """Lower (more negative) score = more anomalous. Useful for ranking."""
        if not self.is_trained:
            raise RuntimeError("Detector must be fit before use.")
        return self.model.decision_function(X)
