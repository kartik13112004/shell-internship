# model_utils.py
import joblib
import os
import numpy as np

MODEL_PATH = "ev_range_model.joblib"

def load_model(path=MODEL_PATH):
    """
    Load a joblib model and return an object that has .predict()
    If the file doesn't exist return None.
    If the loaded object doesn't have .predict, return a fallback object with predict().
    """
    if not os.path.exists(path):
        return None

    try:
        obj = joblib.load(path)
    except Exception as e:
        # If loading fails, raise a helpful error so app can show it in UI
        raise RuntimeError(f"Failed to load model file '{path}': {e}")

    # If it already has predict(), return it
    if hasattr(obj, "predict") and callable(getattr(obj, "predict")):
        return obj

    # If it's a dict, try common keys
    if isinstance(obj, dict):
        for key in ("model", "estimator", "pipeline"):
            candidate = obj.get(key)
            if candidate and hasattr(candidate, "predict"):
                return candidate

    # Otherwise return a fallback object that implements predict
    class FallbackModel:
        """Implements a simple predict using battery_kwh * eff_km_per_kwh"""
        def predict(self, X):
            # Accept list/tuple/ndarray or single sample
            arr = np.asarray(X)
            # If single numeric values passed as shape (,) or (n,), handle common cases
            if arr.ndim == 0:
                # Single scalar -> cannot infer features; return 0
                return np.array([0.0])
            if arr.ndim == 1:
                # Single sample vector: use first two elements as battery and eff
                battery = float(arr[0]) if arr.size > 0 else 0.0
                eff = float(arr[1]) if arr.size > 1 else 0.0
                return np.array([battery * eff])
            # 2D: treat first two columns as battery,eff
            if arr.ndim == 2:
                battery = arr[:, 0].astype(float)
                eff = arr[:, 1].astype(float) if arr.shape[1] > 1 else np.ones_like(battery) * 5.0
                return battery * eff
            # Fallback:
            return np.zeros((arr.shape[0],))

    fallback = FallbackModel()
    fallback._is_fallback = True
    return fallback

def predict_range(battery_kwh, eff_km_per_kwh, model=None):
    """
    Unified predict helper used by app.py
    - If model provided and has predict -> call it
    - If model is None -> try to load default model
    - If model missing or no predict -> fallback to battery * eff
    """
    if model is None:
        model = load_model()

    if model is None:
        # No file present — return deterministic formula
        return float(battery_kwh * eff_km_per_kwh)

    # If model is fallback or doesn't have predict, use simple formula
    if not hasattr(model, "predict") or getattr(model, "_is_fallback", False):
        return float(battery_kwh * eff_km_per_kwh)

    # Call model.predict with a 2D array
    try:
        x = [[battery_kwh, eff_km_per_kwh]]
        pred = model.predict(x)
        # Normalize output
        if hasattr(pred, "__len__"):
            return float(pred[0])
        return float(pred)
    except Exception:
        # On any error, fallback to simple formula
        return float(battery_kwh * eff_km_per_kwh)
