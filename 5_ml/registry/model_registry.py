"""
Model registry (save/load)
------------------------------
Persists trained models to disk with joblib and reloads them, so
training (slow, offline) and inference (fast, online in the API) stay
decoupled. The service layer in 2_backend calls `load_model`, not the
training code.
"""

import joblib
from pathlib import Path

MODEL_DIR = Path(__file__).parent / "saved_models"
MODEL_DIR.mkdir(exist_ok=True)


def save_model(model, name: str) -> Path:
    """Serialize a trained model object to disk under a versioned filename."""
    path = MODEL_DIR / f"{name}.joblib"
    joblib.dump(model, path)
    return path


def load_model(name: str):
    """Load a previously saved model by name. Raises if not found."""
    path = MODEL_DIR / f"{name}.joblib"
    if not path.exists():
        raise FileNotFoundError(f"No saved model named '{name}' in {MODEL_DIR}")
    return joblib.load(path)
