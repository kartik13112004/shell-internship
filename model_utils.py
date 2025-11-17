# model_utils.py
import importlib
import os
import sys
import traceback
from joblib import load as joblib_load

# --- Compatibility monkeypatches for known missing sklearn private names ---
# This must run BEFORE joblib.load() is called.
def _ensure_sklearn_compatibility():
    module_name = "sklearn.compose._column_transformer"
    try:
        ct = importlib.import_module(module_name)
    except Exception:
        ct = None

    if ct is not None:
        # Fallback: if the old private name is missing, provide a simple shim.
        if not hasattr(ct, "_RemainderColsList"):
            class _RemainderColsList(list):
                """Compatibility fallback for old pickles that referenced _RemainderColsList"""
                pass
            setattr(ct, "_RemainderColsList", _RemainderColsList)

    # add any other compatibility fallbacks here if needed:
    # e.g. for very old pipelines you might need to create aliases for other names.

# --- Model loader with helpful logging ---
def load_model(model_path="ev_range_model.joblib"):
    """
    Load the joblib model at model_path. If unpickling fails because of missing
    classes from sklearn, this function attempts compatibility fallbacks first.
    """
    # Ensure compatibility shims are present
    _ensure_sklearn_compatibility()

    # Resolve absolute path (if the model sits in a folder, adjust accordingly)
    abs_path = os.path.join(os.getcwd(), model_path) if not os.path.isabs(model_path) else model_path

    if not os.path.exists(abs_path):
        # helpful error for debugging in Streamlit logs
        raise FileNotFoundError(f"Model file not found at: {abs_path}")

    try:
        # Use joblib to load the model
        model = joblib_load(abs_path)
        return model
    except Exception as ex:
        # Print stacktrace to the logs so Streamlit's log viewer shows the full detail
        tb = traceback.format_exc()
        # Re-raise a clear error so you see something in the app logs
        raise RuntimeError(
            "Failed to load model via joblib.load(). See nested exception and logs.\n\n"
            f"Original exception:\n{ex}\n\nTraceback:\n{tb}"
        ) from ex
