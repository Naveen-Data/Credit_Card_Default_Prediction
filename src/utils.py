import os
import sys
import warnings
import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.exceptions import ConvergenceWarning
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params, n_jobs=-1):
    try:
        report = {}

        for model_name, model in models.items():
            # Check if the model has tuning parameters
            if model_name in params:
                tuning_params = params[model_name]
                if tuning_params:
                    # Use GridSearchCV for hyperparameter tuning
                    gs = GridSearchCV(model, tuning_params, cv=5, n_jobs=n_jobs)
                    gs.fit(X_train, y_train)

                    # Update the model with the best parameters
                    model.set_params(**gs.best_params_)
                    model.fit(X_train, y_train)
                else:
                    # No tuning parameters for this model, directly fit the model
                    model.fit(X_train, y_train)

                # Predictions on training and test sets
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)

                # F1 scores
                train_model_score = accuracy_score(y_train, y_train_pred)
                test_model_score = accuracy_score(y_test, y_test_pred)

                report[model_name] = test_model_score

        return report


    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)