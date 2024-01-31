import os 
import sys 
import pickle
from src.logger import logging
from src.exception import CustomException
import numpy as np
import pandas as pd

import pandas as pd

# Column names
columns = [ "LIMIT_BAL", "AGE", "PAY_SEPT", "PAY_AUG", "PAY_JUL", "PAY_JUN", "PAY_MAY", "PAY_APR", "BILL_AMT_SEPT", "BILL_AMT_AUG", "BILL_AMT_JUL", "BILL_AMT_JUN", "BILL_AMT_MAY", "BILL_AMT_APR", "PAY_AMT_SEPT", "PAY_AMT_AUG", "PAY_AMT_JUL", "PAY_AMT_JUN", "PAY_AMT_MAY", "PAY_AMT_APR", "SEX_1", "SEX_2", "EDUCATION_1", "EDUCATION_2", "EDUCATION_3", "EDUCATION_4", "MARRIAGE_1", "MARRIAGE_2", "MARRIAGE_3"]

# Data
data = [20000.0,42,2,2,2,2,2,2,18333.43394085532,19032.229717868126,19569.449818269466,19835.76081636225,20281.131537803776,20693.084195804127,1297.3634390686198,1145.8703553501487,885.1493083718472,978.3831027906157,886.4675888375372,345.8703553501487,0,1,0,1,0,0,1,0,0]
# Create DataFrame
df = pd.DataFrame([data], columns=columns)

# print(df)
# data = [500000.0,39,0,0,0,0,0,0,4419.0,2584.0,4524.0,3518.0,2208.0,2550.0,2584.0,4524.0,3518.0,2208.0,2550.0,5953.0,0,1,1,0,0,0,1,0,0]


def transform_data(data):
    # Perform data transformation here
    # data = np.array(data).reshape(1, -1)
    transformed_data = df
    # print(transformed_data)
    return transformed_data

def predict(data):
    transformed_data = transform_data(data)
    
    # Load processor and model from pickle files
    with open('artifacts/proprocessor.pkl', 'rb') as f:
        processor = pickle.load(f)
    with open('artifacts/model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    # Perform prediction using transformed data
    preprocessed_data = processor.transform(transformed_data)
    print(preprocessed_data)
    prediction = model.predict(preprocessed_data)
    
    
    return prediction
print(predict(data))
