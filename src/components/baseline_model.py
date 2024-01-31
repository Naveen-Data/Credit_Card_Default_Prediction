# import os
# import sys
# import pandas as pd
# from dataclasses import dataclass
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
# from sklearn.ensemble import (
#     RandomForestClassifier,
# )

# from sklearn.metrics import f1_score
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier


# from src.exception import CustomException
# from src.logger import logging

# from src.utils import save_object,evaluate_models

# def base_model():
#     train_data =os.path.join('artifacts',"train_base.csv")
#     test_data = os.path.join('artifacts',"test_base.csv")
#     X_train = (pd.read_csv(train_data))[:,:-1]
#     y_train = (pd.read_csv(train_data))[:,-1]
#     X_test = (pd.read_csv(test_data))[:,:-1]
#     y_test = (pd.read_csv(test_data))[:,-1]


#     model = LogisticRegression()
#     model.fit(X_train,y_train)
#     y_pred = model.predict(X_test)
#     print(f1_score(y_test,y_pred))
#     print(model.score(X_train,y_train))
#     logging.info(f"Base model f1 score: {f1_score(y_test,y_pred)}")
#     logging.info(f"Base model accuracy: {model.score(X_train,y_train)}")