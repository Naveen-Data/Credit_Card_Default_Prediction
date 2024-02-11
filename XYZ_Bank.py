import os
import sys
import streamlit as st
import pandas as pd
from src.exception import CustomException
from pipeline.predict_pipeline import PredictPipeline
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv

load_dotenv()

st.title('Credit Card Default Prediction')

# MongoDB connection
uri = os.getenv('uri')
client = MongoClient(uri)
coll = client.db.test

LIMIT_BAL = st.text_input('LIMIT_BAL', '')
AGE = st.text_input('AGE', '')

PAY_SEPT_options = {'Duly Paid': -1, '1 Month Delay': 1, '2 Month Delay': 2, '3 Month Delay': 3, '4 Month Delay': 4, '5 Month Delay': 5, '6 Month Delay': 6, '7 Month Delay': 7, '8 Month Delay': 8, '9 Month Delay': 9}
PAY_AUG_options = PAY_JUL_options = PAY_JUN_options = PAY_MAY_options = PAY_APR_options = PAY_SEPT_options
PAY_SEPT = st.selectbox('Repayment Status in September', list(PAY_SEPT_options.keys()))
PAY_AUG = st.selectbox('Repayment Status in August', list(PAY_AUG_options.keys()))
PAY_JUL = st.selectbox('Repayment Status in July', list(PAY_JUL_options.keys()))
PAY_JUN = st.selectbox('Repayment Status in June', list(PAY_JUN_options.keys()))
PAY_MAY = st.selectbox('Repayment Status in May', list(PAY_MAY_options.keys()))
PAY_APR = st.selectbox('Repayment Status in April', list(PAY_APR_options.keys()))

BILL_AMT_SEPT = st.number_input('Amount of Bill Statement in September', value=0)
BILL_AMT_AUG = st.number_input('Amount of Bill Statement in August', value=0)
BILL_AMT_JUL = st.number_input('Amount of Bill Statement in July', value=0)
BILL_AMT_JUN = st.number_input('Amount of Bill Statement in June', value=0)
BILL_AMT_MAY = st.number_input('Amount of Bill Statement in May', value=0)
BILL_AMT_APR = st.number_input('Amount of Bill Statement in April', value=0)

PAY_AMT_SEPT = st.number_input('Amount of Previous Payment in September', value=0)
PAY_AMT_AUG = st.number_input('Amount of Previous Payment in August', value=0)
PAY_AMT_JUL = st.number_input('Amount of Previous Payment in July', value=0)
PAY_AMT_JUN = st.number_input('Amount of Previous Payment in June', value=0)
PAY_AMT_MAY = st.number_input('Amount of Previous Payment in May', value=0)
PAY_AMT_APR = st.number_input('Amount of Previous Payment in April', value=0)

EDUCATION_options = ['Graduate School', 'University', 'High School', 'Others']
MARRIAGE_options = ['Single', 'Married', 'Others']
SEX_options = ['Male', 'Female']

EDUCATION = st.selectbox('Education', EDUCATION_options)
MARRIAGE = st.selectbox('Marriage', MARRIAGE_options)
SEX = st.selectbox('Sex', SEX_options)

submit_button = st.button('Predict')

# JavaScript to check and highlight empty fields
script = """
<script>
document.getElementById("submit_button").onclick = function() {
    var requiredFields = ["LIMIT_BAL", "AGE", "PAY_SEPT", "PAY_AUG", "PAY_JUL", "PAY_JUN", "PAY_MAY", "PAY_APR",
                           "BILL_AMT_SEPT", "BILL_AMT_AUG", "BILL_AMT_JUL", "BILL_AMT_JUN", "BILL_AMT_MAY", "BILL_AMT_APR",
                           "PAY_AMT_SEPT", "PAY_AMT_AUG", "PAY_AMT_JUL", "PAY_AMT_JUN", "PAY_AMT_MAY", "PAY_AMT_APR",
                           "EDUCATION", "MARRIAGE", "SEX"];

    var highlightColor = "#FFD700";

    for (var i = 0; i < requiredFields.length; i++) {
        var fieldId = requiredFields[i];
        var fieldValue = document.getElementById(fieldId).value.trim();
        if (fieldValue === "") {
            document.getElementById(fieldId).style.backgroundColor = highlightColor;
        } else {
            document.getElementById(fieldId).style.backgroundColor = "";
        }
    }
};
</script>
"""

# Inject the JavaScript into the HTML
st.markdown(script, unsafe_allow_html=True)

# ...

# Check if all fields are filled before proceeding with prediction
if submit_button:
    required_fields = [str(LIMIT_BAL), str(AGE), PAY_SEPT, PAY_AUG, PAY_JUL, PAY_JUN, PAY_MAY, PAY_APR,
                       str(BILL_AMT_SEPT), str(BILL_AMT_AUG), str(BILL_AMT_JUL), str(BILL_AMT_JUN),
                       str(BILL_AMT_MAY), str(BILL_AMT_APR), str(PAY_AMT_SEPT), str(PAY_AMT_AUG),
                       str(PAY_AMT_JUL), str(PAY_AMT_JUN), str(PAY_AMT_MAY), str(PAY_AMT_APR),
                       EDUCATION, MARRIAGE, SEX]

    if all(field.strip() for field in required_fields):
        SEX_1 = 1 if SEX == 'Male' else 0
        SEX_2 = 1 if SEX == 'Female' else 0

        EDUCATION_mapping = {'Graduate School': 1, 'University': 2, 'High School': 3, 'Others': 4}
        MARRIAGE_mapping = {'Single': 1, 'Married': 2, 'Others': 3}

        EDUCATION_selected = EDUCATION_mapping.get(EDUCATION, 1)
        MARRIAGE_selected = MARRIAGE_mapping.get(MARRIAGE, 1)

        EDUCATION_1 = 1 if EDUCATION_selected == 1 else 0
        EDUCATION_2 = 1 if EDUCATION_selected == 2 else 0
        EDUCATION_3 = 1 if EDUCATION_selected == 3 else 0
        EDUCATION_4 = 1 if EDUCATION_selected == 4 else 0

        MARRIAGE_1 = 1 if MARRIAGE_selected == 1 else 0
        MARRIAGE_2 = 1 if MARRIAGE_selected == 2 else 0
        MARRIAGE_3 = 1 if MARRIAGE_selected == 3 else 0

        try:
            features = [
                LIMIT_BAL, AGE,
                PAY_SEPT_options[PAY_SEPT], PAY_SEPT_options[PAY_AUG], PAY_SEPT_options[PAY_JUL],
                PAY_SEPT_options[PAY_JUN], PAY_SEPT_options[PAY_MAY], PAY_SEPT_options[PAY_APR],
                BILL_AMT_SEPT, BILL_AMT_AUG, BILL_AMT_JUL, BILL_AMT_JUN, BILL_AMT_MAY, BILL_AMT_APR,
                PAY_AMT_SEPT, PAY_AMT_AUG, PAY_AMT_JUL, PAY_AMT_JUN, PAY_AMT_MAY, PAY_AMT_APR,
                SEX_1, SEX_2,
                EDUCATION_1, EDUCATION_2, EDUCATION_3, EDUCATION_4,
                MARRIAGE_1, MARRIAGE_2, MARRIAGE_3
            ]
            columns = [ "LIMIT_BAL", "AGE",
                        "PAY_SEPT", "PAY_AUG", "PAY_JUL", "PAY_JUN", "PAY_MAY", "PAY_APR",
                        "BILL_AMT_SEPT", "BILL_AMT_AUG", "BILL_AMT_JUL", "BILL_AMT_JUN", "BILL_AMT_MAY", "BILL_AMT_APR",
                        "PAY_AMT_SEPT", "PAY_AMT_AUG", "PAY_AMT_JUL", "PAY_AMT_JUN", "PAY_AMT_MAY", "PAY_AMT_APR",
                        "SEX_1", "SEX_2", 
                        "EDUCATION_1", "EDUCATION_2", "EDUCATION_3", "EDUCATION_4",
                        "MARRIAGE_1", "MARRIAGE_2", "MARRIAGE_3"
                        ]
            data = pd.DataFrame([features],columns=columns)
            data_dict = {col: val for col, val in zip(columns, features)}
            coll.insert_one(data_dict)
            default = PredictPipeline().predict(data)
            if default[0] == 1:
                prediction_text = "The credit card holder will be Default in the next month"
            else:
                prediction_text = "The Credit card holder will not be Default in the next month"
            st.write(prediction_text)
        except Exception as e:
            raise CustomException(e, sys)
    else:
        st.error('All fields are required!')

