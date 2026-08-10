"""
ML model tests
------------------
Smoke tests confirming each model trains and predicts without error
on small synthetic data. Not a substitute for real validation against
lab data, but catches breakage early.
"""

import numpy as np
from 5_ml.algorithms.quality_regression import QualityPredictionModel
from 5_ml.algorithms.substitution_classifier import MaterialSubstitutionClassifier
from 5_ml.algorithms.anomaly_detection import ManufacturingAnomalyDetector


def test_quality_regression_trains_and_predicts():
    X = np.random.rand(50, 4)
    y = X[:, 0] * 2 + np.random.normal(0, 0.1, 50)
    model = QualityPredictionModel()
    metrics = model.train(X, y, feature_names=["particle_size", "moisture", "purity", "density"])
    assert "r2_score" in metrics
    assert model.predict(X[:5]).shape == (5,)


def test_substitution_classifier_trains_and_predicts():
    X = np.random.rand(50, 3)
    y = (X[:, 0] > 0.5).astype(int)
    model = MaterialSubstitutionClassifier()
    report = model.train(X, y)
    assert "accuracy" in report
    probs = model.predict_suitability(X[:5])
    assert ((probs >= 0) & (probs <= 1)).all()


def test_anomaly_detector_flags_outliers():
    X_normal = np.random.normal(0, 1, (100, 3))
    detector = ManufacturingAnomalyDetector(contamination=0.1)
    detector.fit(X_normal)
    X_outlier = np.array([[50, 50, 50]])
    assert detector.flag_anomalies(X_outlier)[0] == True
