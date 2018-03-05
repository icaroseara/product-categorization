import pandas as pd

from sklearn.externals import joblib
from src.config.settings import FEATURES, MODELS_DIR, MODELS_FILE

def predict(data):
    cls = joblib.load(MODEL_DIR + MODELS_FILE)
    df = pd.DataFrame([dict(data)])
    prediction = cls.predict(df[FEATURES])[:, 1][0]
    return prediction
