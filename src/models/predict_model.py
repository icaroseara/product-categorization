import pandas as pd

from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from src.config.settings import FEATURES, MODELS_DIR, MODELS_FILE

def predict(product):
    cls = joblib.load(MODEL_DIR + MODELS_FILE)
    count_vect = CountVectorizer(lowercase=False)
    tfidf_transformer = TfidfTransformer()

    df_product = pd.DataFrame([dict(product)])
    df_product = df_product[FEATURES]
    X_prod_counts = count_vect.transform(df_product)
    X_prod_tfidf = tfidf_transformer.transform(X_prod_counts)
    prediction = clf.predict(X_prod_tfidf)

    return prediction[:, 1][0]
