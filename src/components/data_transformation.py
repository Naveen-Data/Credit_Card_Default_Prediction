import os
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging


from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        
        '''
        try:
            numerical_features = [
                                'LIMIT_BAL', 'AGE', 'PAY_SEPT', 'PAY_AUG', 'PAY_JUL', 'PAY_JUN',
                                'PAY_MAY', 'PAY_APR', 'BILL_AMT_SEPT', 'BILL_AMT_AUG', 'BILL_AMT_JUL',
                                'BILL_AMT_JUN', 'BILL_AMT_MAY', 'BILL_AMT_APR', 'PAY_AMT_SEPT',
                                'PAY_AMT_AUG', 'PAY_AMT_JUL', 'PAY_AMT_JUN', 'PAY_AMT_MAY','PAY_AMT_APR'
                ]
            categorical_features = [
                                'SEX_1', 'SEX_2', 'EDUCATION_1', 'EDUCATION_2',
                            'EDUCATION_3', 'EDUCATION_4', 'MARRIAGE_1', 'MARRIAGE_2', 'MARRIAGE_3'
                                ]
            
            

            num_pipeline= Pipeline(
                steps=[
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                # ("one_hot_encoder",OneHotEncoder()),
                ("scaler",StandardScaler())
                ]

            )

            logging.info(f"Categorical columns: {categorical_features}")
            logging.info(f"Numerical columns: {numerical_features}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_features),
                ("cat_pipelines",cat_pipeline,categorical_features)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)



            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")
            logging.info(f"{train_df.head()}")
            logging.info(f"Train columns: {len(train_df.columns)}")
            logging.info(f"Test columns: {test_df.columns}")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name='Defaulter'
            
            input_feature_train_df=train_df.drop(['Defaulter'],axis=1)
            logging.info(f"Input feature train dataframe: {input_feature_train_df.columns}")
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(['Defaulter'],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )
            logging.info(f"Input feature train dataframe: {len(input_feature_train_df.columns)}")
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info(f"Input feature train array: {input_feature_train_arr}")

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object.")

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )
            logging.info(f"Saved preprocessing object.")

            return (
                train_arr,
                test_arr
                # self.data_transformation_config.preprocessor_obj_file_path,
            )
        except Exception as e:
            raise CustomException(e,sys)