import sys
import tensorflow as tf
import numpy as np
from url_feature import (
    extract_features_from_url
)  # Ensure this function is accessible


def load_model_rl():
    print("Loading rl model...")
    model = tf.keras.models.load_model("dqn_model.h5")
    return model
    # return 0

def load_model():
    print("Loading model...")
    return tf.keras.models.load_model("best_model.keras")

def predict(model, url, opr_key=None):
    """
    Predict the output of a given URL
    Parameters:
        model (tf.keras.models.Model): the model to use for prediction
        url (str): the URL to predict the output for
        opr_key (str): an API key for page_rank lookup (if not provided, default to -1)
    Returns:
        np.ndarray: a numpy array of the prediction
    """
    features = extract_features_from_url(url, opr_key)
    features = features.reshape(1, -1)
    predictions = model.predict(features)
    return predictions
    # return 0


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python inferences.py <url>")
        sys.exit(1)
    input_url = sys.argv[1]
    # Optionally provide your OPR API key for page_rank computation:
    opr_key = "so0kwk4448ck8ggwsogwo8kswgs08kwc4gk8s844"  # Replace with your key or leave as None

    model_rl = load_model_rl()
    model = load_model()
    prediction_rl = predict(model_rl, input_url, opr_key)
    prediction = predict(model, input_url, opr_key)
    print("Predicted output:", prediction)
    print("rl Predicted output:", prediction_rl)
