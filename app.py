
import os
import sys
# from src.logger import loggin
from src.exception import CustomException
from flask import Flask, render_template, request
import pandas as pd
from flask_pymongo import PyMongo
from pipeline.predict_pipeline import PredictPipeline
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()
app= Flask(__name__)
URI = {{secrets.MONGO_URI}}
# Create a new client and connect to the server
client = MongoClient(URI)

# Send a ping to confirm a successful connection
db = client['cluster0']
collection = db['Test']

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
            collection.insert_one(data.to_dict())
            default = PredictPipeline().predict(data)
            if default[0] == 1:
                prediction_text = "The credit card holder will be Default in the next month"
            else:
                prediction_text = "The Credit card holder will not be Default in the next month"
            print(prediction_text)
            return render_template('index.html', prediction_text = prediction_text)    
    except Exception as e:
        raise CustomException(e,sys)
#     '''
#     for rendering results on HTML
#     '''
#     features = [int(x) for x in request.form.values()]

#     # re-arranging the list as per data set
#     feature_list = [features[4]] + features[:4] + features[5:11][::-1] + features[11:17][::-1] + features[17:][::-1]
#     features_arr = [np.array(feature_list)]

#     prediction = model.predict(features_arr)

#     print(features_arr)
#     #newdb.insert_one(d)
#     print("features is :",features)
#     default_payment=prediction.tolist()
#     New_database={'Gender':features[0],
#                  'Education':features[1],
#                  'Marrital Status':features[2],
#                  'Age':features[3],
#                  'Limit Balance':features[4],
#                  'PAY_1':features[5],
#                  'PAY_2':features [6],
#                  'PAY_3':features [7],
#                  'PAY_4':features [8],
#                  'PAY_5':features [9],
#                  'PAY_6':features [10],
#                  'BILL_AMT1':features [11],
#                  'BILL_AMT2':features [12],
#                  'BILL_AMT3':features [13],
#                  'BILL_AMT4':features [14],
#                  'BILL_AMT5':features [15],
#                  'BILL_AMT6':features [16],
#                  'PAY_AMT1':features[17],
#                  'PAY_AMT2':features[18],
#                  'PAY_AMT3':features [19],
#                  'PAY_AMT4':features[20],
#                  'PAY_AMT5':features[21],
#                  'PAY_AMT6':features[22],
#                  'Prediction':default_payment[0]}
#     database.insert_one(New_database)
   
#     print("prediction value: ", prediction)

#     result = ""
#     if prediction == 1:
#         result = "The credit card holder will be Defaulter in the next month"
#     else:
#         result = "The Credit card holder will not be Defaulter in the next month"
# return render_template('index.html', prediction_text = 'Predicted')


if __name__=="__main__":
   
    app.run(debug=True)
    print("App is running")