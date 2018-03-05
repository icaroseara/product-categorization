import pandas as pd
import autosklearn.classification
import sklearn.model_selection
import sklearn.metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfTransformer

def train_model():
    df = pd.read_csv('data/raw/dataset.csv')
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
        df[['name', 'description']],
        df.category,
        random_state=1
    )

    X_train.loc[:,"name"] = X_train.name.apply(lambda x : str.lower(x))
    X_train.loc[:,"description"] = X_train.description.apply(lambda x : str.lower(x))

    count_vect = CountVectorizer(stop_words=get_stop_words('pt'))
    X_train_counts = count_vect.fit_transform(X_train)

    # tfidf_transformer = TfidfVectorizer(
    #     stop_words=get_stop_words('pt'),
    #     preprocessor=None,
    #     lowercase=False
    # )
    # X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)
    X_train_tf.shape

    labels = LabelEncoder()
    y = labels.fit_transform(y)

    cls = autosklearn.classification.AutoSklearnClassifier()
    cls.fit(X_train_tfidf, y)
    y_hat = cls.predict(X_test)
    print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))

train_model()
