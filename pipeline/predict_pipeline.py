import os
import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,data):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(data)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



# class CustomData:
#     def __init__(  self,
#         LIMIT_BAL:float,
#         AGE:int,
#         PAY_SEPT:int,
#         PAY_AUG:int,
#         PAY_JUL:int,
#         PAY_JUN:int,
#         PAY_MAY:int,
#         PAY_APR:int,
#         BILL_AMT_SEPT:float,
#         BILL_AMT_AUG:float,
#         BILL_AMT_JUL:float,
#         BILL_AMT_JUN:float,
#         BILL_AMT_MAY:float,
#         BILL_AMT_APR:float,
#         PAY_AMT_SEPT:float,
#         PAY_AMT_AUG:float,
#         PAY_AMT_JUL:float,
#         PAY_AMT_JUN:float,
#         PAY_AMT_MAY:float,
#         PAY_AMT_APR:float,
#         SEX_1:int,
#         SEX_2:int,
#         EDUCATION_1:int,
#         EDUCATION_2:int,
#         EDUCATION_3:int,
#         EDUCATION_4:int,
#         MARRIAGE_1:int,
#         MARRIAGE_2:int,
#         MARRIAGE_3:int
#         ):


#         self.LIMIT_BAL=LIMIT_BAL
#         self.AGE=AGE
#         self.PAY_SEPT=PAY_SEPT
#         self.PAY_AUG=PAY_AUG
#         self.PAY_JUL=PAY_JUL
#         self.PAY_JUN=PAY_JUN
#         self.PAY_MAY=PAY_MAY
#         self.PAY_APR=PAY_APR
#         self.BILL_AMT_SEPT=BILL_AMT_SEPT
#         self.BILL_AMT_AUG=BILL_AMT_AUG
#         self.BILL_AMT_JUL=BILL_AMT_JUL
#         self.BILL_AMT_JUN=BILL_AMT_JUN
#         self.BILL_AMT_MAY=BILL_AMT_MAY
#         self.BILL_AMT_APR=BILL_AMT_APR
#         self.PAY_AMT_SEPT=PAY_AMT_SEPT
#         self.PAY_AMT_AUG=PAY_AMT_AUG
#         self.PAY_AMT_JUL=PAY_AMT_JUL
#         self.PAY_AMT_JUN=PAY_AMT_JUN
#         self.PAY_AMT_MAY=PAY_AMT_MAY
#         self.PAY_AMT_APR=PAY_AMT_APR
#         self.SEX_1=SEX_1
#         self.SEX_2=SEX_2
#         self.EDUCATION_1=EDUCATION_1
#         self.EDUCATION_2=EDUCATION_2
#         self.EDUCATION_3=EDUCATION_3
#         self.EDUCATION_4=EDUCATION_4
#         self.MARRIAGE_1=MARRIAGE_1
#         self.MARRIAGE_2=MARRIAGE_2
#         self.MARRIAGE_3=MARRIAGE_3



#     def get_data_as_data_frame(self):
#         try:
#             custom_data_input_dict = {
#                 'LIMIT_BAL':[self.LIMIT_BAL],
#                 'AGE':[self.AGE],
#                 'PAY_SEPT':[self.PAY_SEPT],
#                 'PAY_AUG':[self.PAY_AUG],
#                 'PAY_JUL':[self.PAY_JUL],
#                 'PAY_JUN':[self.PAY_JUN],
#                 'PAY_MAY':[self.PAY_MAY],
#                 'PAY_APR':[self.PAY_APR],
#                 'BILL_AMT_SEPT':[self.BILL_AMT_SEPT],
#                 'BILL_AMT_AUG':[self.BILL_AMT_AUG],
#                 'BILL_AMT_JUL':[self.BILL_AMT_JUL],
#                 'BILL_AMT_JUN':[self.BILL_AMT_JUN],
#                 'BILL_AMT_MAY':[self.BILL_AMT_MAY],
#                 'BILL_AMT_APR':[self.BILL_AMT_APR],
#                 'PAY_AMT_SEPT':[self.PAY_AMT_SEPT],
#                 'PAY_AMT_AUG':[self.PAY_AMT_AUG],
#                 'PAY_AMT_JUL':[self.PAY_AMT_JUL],
#                 'PAY_AMT_JUN':[self.PAY_AMT_JUN],
#                 'PAY_AMT_MAY':[self.PAY_AMT_MAY],
#                 'PAY_AMT_APR':[self.PAY_AMT_APR],
#                 'SEX_1':[self.SEX_1],
#                 'SEX_2':[self.SEX_2],
#                 'EDUCATION_1':[self.EDUCATION_1],
#                 'EDUCATION_2':[self.EDUCATION_2],
#                 'EDUCATION_3':[self.EDUCATION_3],
#                 'EDUCATION_4':[self.EDUCATION_4],
#                 'MARRIAGE_1':[self.MARRIAGE_1],
#                 'MARRIAGE_2':[self.MARRIAGE_2],
#                 'MARRIAGE_3':[self.MARRIAGE_3]
                
#             }

#             return pd.DataFrame(custom_data_input_dict)

#         except Exception as e:
#             raise CustomException(e, sys)
