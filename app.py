
import os
import sys
from src.logger import logging
from src.exception import CustomException
from flask import Flask, render_template, request
import pandas as pd
from flask_pymongo import PyMongo
from pipeline.predict_pipeline import PredictPipeline
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()
app= Flask(__name__)
uri = os.getenv('uri')
client = MongoClient(uri)
coll = client.db.test
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST','GET'])
def predict():
    try:
        if request.method == 'POST':
            LIMIT_BAL= request.form.get('LIMIT_BAL')
            AGE= request.form.get('AGE')
            PAY_SEPT= request.form.get('PAY_SEPT')
            PAY_AUG= request.form.get('PAY_AUG')
            PAY_JUL= request.form.get('PAY_JUL')
            PAY_JUN= request.form.get('PAY_JUN')
            PAY_MAY= request.form.get('PAY_MAY')
            PAY_APR= request.form.get('PAY_APR')
            BILL_AMT_SEPT= request.form.get('BILL_AMT_SEPT')
            BILL_AMT_AUG= request.form.get('BILL_AMT_AUG')
            BILL_AMT_JUL= request.form.get('BILL_AMT_JUL')
            BILL_AMT_JUN= request.form.get('BILL_AMT_JUN')
            BILL_AMT_MAY= request.form.get('BILL_AMT_MAY')
            BILL_AMT_APR= request.form.get('BILL_AMT_APR')
            PAY_AMT_SEPT= request.form.get('PAY_AMT_SEPT')
            PAY_AMT_AUG= request.form.get('PAY_AMT_AUG')
            PAY_AMT_JUL= request.form.get('PAY_AMT_JUL')
            PAY_AMT_JUN= request.form.get('PAY_AMT_JUN')
            PAY_AMT_MAY= request.form.get('PAY_AMT_MAY')
            PAY_AMT_APR= request.form.get('PAY_AMT_APR')
            EDUCATION = request.form.get('EDUCATION')
            MARRIAGE = request.form.get('MARRIAGE')
            SEX = request.form.get('SEX')
            SEX_1 = 0
            SEX_2 = 0
            if SEX == 1:
                SEX_1 = 1
            else:
                SEX_2 = 1

            EDUCATION_1 = 0
            EDUCATION_2 = 0
            EDUCATION_3 = 0
            EDUCATION_4 = 0
            if EDUCATION == 1:
                EDUCATION_1 = 1
            elif EDUCATION == 2:
                EDUCATION_2 = 1
            elif EDUCATION == 3:
                EDUCATION_3 = 1
            else:
                EDUCATION_4 = 1

            MARRIAGE_1 = 0
            MARRIAGE_2 = 0
            MARRIAGE_3 = 0
            if MARRIAGE == 1:
                MARRIAGE_1 = 1
            elif MARRIAGE == 2:
                MARRIAGE_2 = 1
            else:
                MARRIAGE_3 = 1
            columns = [ "LIMIT_BAL", "AGE",
                        "PAY_SEPT", "PAY_AUG", "PAY_JUL", "PAY_JUN", "PAY_MAY", "PAY_APR",
                        "BILL_AMT_SEPT", "BILL_AMT_AUG", "BILL_AMT_JUL", "BILL_AMT_JUN", "BILL_AMT_MAY", "BILL_AMT_APR",
                        "PAY_AMT_SEPT", "PAY_AMT_AUG", "PAY_AMT_JUL", "PAY_AMT_JUN", "PAY_AMT_MAY", "PAY_AMT_APR",
                        "SEX_1", "SEX_2", 
                        "EDUCATION_1", "EDUCATION_2", "EDUCATION_3", "EDUCATION_4",
                        "MARRIAGE_1", "MARRIAGE_2", "MARRIAGE_3"
                        ]

            features = [
                        LIMIT_BAL, AGE, 
                        PAY_SEPT, PAY_AUG, PAY_JUL, PAY_JUN, PAY_MAY, PAY_APR,
                        BILL_AMT_SEPT, BILL_AMT_AUG, BILL_AMT_JUL, BILL_AMT_JUN, BILL_AMT_MAY, BILL_AMT_APR,
                        PAY_AMT_SEPT, PAY_AMT_AUG, PAY_AMT_JUL, PAY_AMT_JUN, PAY_AMT_MAY, PAY_AMT_APR,
                        SEX_1,SEX_2,
                        EDUCATION_1, EDUCATION_2, EDUCATION_3, EDUCATION_4,
                        MARRIAGE_1, MARRIAGE_2, MARRIAGE_3
                        ]
            data = pd.DataFrame([features], columns=columns)
            data_dict = {col: val for col, val in zip(columns, features)}
            coll.insert_one(data_dict)
            default = PredictPipeline().predict(data)
            if default[0] == 1:
                prediction_text = "The credit card holder will be Default in the next month"
            else:
                prediction_text = "The Credit card holder will not be Default in the next month"
            print(prediction_text)
            return render_template('index.html', prediction_text = prediction_text)    
    except Exception as e:
        raise CustomException(e,sys)

if __name__=="__main__":
    print('app is up')
    app.run(port=5001,debug=True)
    print('run app')
    