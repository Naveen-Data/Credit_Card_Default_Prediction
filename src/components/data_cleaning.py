import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE    
from dataclasses import dataclass

@dataclass
class DataCleaningConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    train_base_path: str= os.path.join('artifacts','train_base.csv')
    test_base_path: str= os.path.join('artifacts','test_base.csv')

class DataCleaning:
    def __init__(self):
        self.cleaning_config=DataCleaningConfig()

    def DataCleaningConfig(self,raw_path):
        logging.info("Data Cleaning Started")
        try:
            df=pd.read_csv(raw_path)
            logging.info('Read the raw_dataset as dataframe')
            df.drop('ID',axis=1,inplace=True)
            df.rename(columns={'default.payment.next.month' : 'Defaulter'}, inplace=True)
            df.rename(columns={'PAY_0' : 'PAY_1'}, inplace=True)
            logging.info('Renamed the columns (default.payment.next.month to Defaulter) and (PAY_0 to PAY_1)')
                

            df.rename(columns={'PAY_1':'PAY_SEPT','PAY_2':'PAY_AUG','PAY_3':'PAY_JUL','PAY_4':'PAY_JUN','PAY_5':'PAY_MAY','PAY_6':'PAY_APR'},inplace=True)
            df.rename(columns={'BILL_AMT1':'BILL_AMT_SEPT','BILL_AMT2':'BILL_AMT_AUG','BILL_AMT3':'BILL_AMT_JUL','BILL_AMT4':'BILL_AMT_JUN','BILL_AMT5':'BILL_AMT_MAY','BILL_AMT6':'BILL_AMT_APR'}, inplace = True)
            df.rename(columns={'PAY_AMT1':'PAY_AMT_SEPT','PAY_AMT2':'PAY_AMT_AUG','PAY_AMT3':'PAY_AMT_JUL','PAY_AMT4':'PAY_AMT_JUN','PAY_AMT5':'PAY_AMT_MAY','PAY_AMT6':'PAY_AMT_APR'},inplace=True)
            logging.info('Renamed the columns')

            df['EDUCATION'].replace([0, 5, 6], 4, inplace=True)
            df['MARRIAGE'].replace(0, 3, inplace=True)
            for i in ['PAY_SEPT','PAY_AUG','PAY_JUL','PAY_JUN','PAY_MAY','PAY_APR']:
                df[i].replace([-1,-2],0,inplace=True)
            logging.info('Replaced the values of EDUCATION and MARRIAGE columns')
            


            df['SEX'] = df['SEX'].astype('object')
            df['EDUCATION'] = df['EDUCATION'].astype('object')
            df['MARRIAGE'] = df['MARRIAGE'].astype('object')
            logging.info('Converted EDUCATION, SEX and MARRIAGE features to categorical')
            
            df = pd.get_dummies(df)
            cat_features =  [
                            'SEX_1', 'SEX_2', 'EDUCATION_1', 'EDUCATION_2',
                            'EDUCATION_3', 'EDUCATION_4', 'MARRIAGE_1', 'MARRIAGE_2', 'MARRIAGE_3'
                            ]
            for i in cat_features:
                df[i] = df[i].astype('int64')
            logging.info(f"Converted cat---- {df.isna().sum()}")
            
            logging.info('Data Balancing Started')
            sm = SMOTE(random_state=42)
            x_smote,y_smote = sm.fit_resample(df.drop('Defaulter',axis=1),df['Defaulter'])
            logging.info(f"x_smote {x_smote.columns}")

            df_smote = pd.concat([x_smote,y_smote],axis=1)
            logging.info('Data Cleaning Completed Successfully')


            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df_smote,test_size=0.3,random_state=42)
            # train_base,test_base=train_test_split(df,test_size=0.3,random_state=42)
            


            
            train_set.to_csv(self.cleaning_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.cleaning_config.test_data_path,index=False,header=True)
            # train_base.to_csv(self.cleaning_config.train_base_path,index=False,header=True)
            # test_base.to_csv(self.cleaning_config.test_base_path,index=False,header=True)

            logging.info("Train test split completed")
            logging.info(f"train data path: {self.cleaning_config.train_data_path}")

            return(
                self.cleaning_config.train_data_path,
                self.cleaning_config.test_data_path
                

            )
        except Exception as e:
            raise CustomException(e,sys)
    
    
 