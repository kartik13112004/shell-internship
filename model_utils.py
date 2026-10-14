
# model_utils.py

import os
import joblib
import pandas as pd

MODEL_PATH = "ev_range_model_v2.joblib"


def load_model(path=MODEL_PATH):
    """Load the trained EV range prediction pipeline."""
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Model file not found: {path}. "
            "Please add the trained model file."
        )

    model = joblib.load(path)

    if not hasattr(model, "predict"):
        raise TypeError("Loaded object does not support predict().")

    return model


def predict_range(vehicle_features, model=None):
    """
    Predict EV range from a dictionary of vehicle features.

    vehicle_features must contain the input columns used during
    training, excluding Range_Km, Brand, and Model.
    """
    if model is None:
        model = load_model()

    if not isinstance(vehicle_features, dict):
        raise TypeError(
            "Pass vehicle features as a dictionary."
        )

    X = pd.DataFrame([vehicle_features])
    prediction = model.predict(X)

    return float(prediction[0])
