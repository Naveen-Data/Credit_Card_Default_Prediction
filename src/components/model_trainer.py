import os
import sys
from dataclasses import dataclass
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import (
    RandomForestClassifier,
)

from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object, evaluate_models


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            models = {
                # "SVC": SVC(),
                'GaussianNB': GaussianNB(),
                'XGBClassifier': XGBClassifier(objective='binary:logistic'),
                "Decision Tree": DecisionTreeClassifier(),
                "Logistic Regression": LogisticRegression(),
            }
            params = {
                "Decision Tree": {
                    'criterion': ['gini', 'entropy'],
                    'max_depth': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                },
                # "XGBoost": {
                #     'learning_rate': [0.01, 0.1, 0.2],
                #     'n_estimators': [50, 100, 200],
                #     'max_depth': [3, 5, 7],
                #     'min_child_weight': [1, 3, 5],
                #     'subsample': [0.8, 0.9, 1.0],
                #     'colsample_bytree': [0.8, 0.9, 1.0],
                #     'gamma': [0, 1, 5],
                #     'reg_alpha': [0, 0.1, 1],
                #     'reg_lambda': [0, 0.1, 1],
                #     'scale_pos_weight': [1, 2, 3],
                # },
                "KNN": {
                    'n_neighbors': [2, 3, 4, 5, 6, 7, 8, 9, 10]
                },
                "SVC": {
                    'kernel': ['rbf'],
                    'C': [0.1, 1, 10, 100]
                },
                "Logistic Regression": {
                    'penalty': ['l2'],
                    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000],
                },
                "Random Forest": {
                    'n_estimators': [100, 200, 300, 400, 500, 1000],
                    # 'criterion':['gini','entropy'],


                }

            }

            model_report: dict = evaluate_models(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                                                 models=models, params=params)

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            if best_model_score < 0.7:
                raise CustomException("No best model found")
            logging.info(
                f"Best found model on both training and testing dataset")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            predicted = best_model.predict(X_test)
            y_pred = best_model.predict(X_train)
            training_score = f1_score(y_train, y_pred)
            f1 = f1_score(y_test, predicted)
            return f1, training_score

        except Exception as e:
            raise CustomException(e, sys)
