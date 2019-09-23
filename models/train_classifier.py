# import libraries
import sys
import pandas as pd
import os
import re
import pickle
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, make_scorer
import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])


def load_data(database_filepath):
    """
    INPUT:
    database_filepath - path to the database

    OUTPUT:
    X - the message
    Y - the categories of the message
    category_names - the columns of the categories (the columns of Y)
    """
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('df', engine)
    X = df['message']
    Y = df.iloc[:, 4:]
    category_names = Y.columns
    return X, Y, category_names


def tokenize(text):
    """
    INPUT:
    text - raw messages

    OUTPUT:
    clean_tokens - cleaned tokenized messages
    """
    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """
    INPUT:
    none

    OUTPUT:
    pipeline - the ML model
    """
    pipeline = Pipeline([
        ('features', FeatureUnion([

            # Commented due to some 'unknown' problem
            # ('starting_verb', StartingVerbExtractor())

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ]))

        ])),

        ('clf', MultiOutputClassifier(AdaBoostClassifier()))

    ])

    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    """
    INPUT:
    model - ML model
    X_test - test messages
    Y_test - the categories of the test messages
    category_names - the columns of the categories

    OUTPUT:
    none - print the overall accuracy and classification report of each category
    """
    y_pred = model.predict(X_test)
    y_pred_df = pd.DataFrame(y_pred, columns=category_names)
    overall_accuracy = (y_pred == Y_test).mean().mean()
    print('Overall accuracy = {0:.2f}%\n'.format(overall_accuracy * 100))

    for column in Y_test.columns:
        print('CATEGORY: {}'.format(column))
        print(classification_report(Y_test[column], y_pred_df[column]))


def save_model(model, model_filepath):
    """
    INPUT:
    model - ML model
    model_filepath - path to save the model

    OUTPUT:
    none
    """
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()