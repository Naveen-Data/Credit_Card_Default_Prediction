


import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_cleaning import DataCleaning
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    def __init__(self):
        self.data_ingestion=DataIngestion()
        self.data_cleaning=DataCleaning()
        self.data_transformation=DataTransformation()
        self.model_trainer=ModelTrainer()

    def initiate_train_pipeline(self):
        try:
            logging.info("Entered the train pipeline")
            raw_data_path=self.data_ingestion.initiate_data_ingestion('data')
            train_data_path,test_data_path=self.data_cleaning.DataCleaningConfig(raw_data_path)
            return train_data_path,test_data_path
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            logging.info("Entered the data transformation method")
            train_arr,test_arr = self.data_transformation.initialize_data_transformation(train_data_path,test_data_path)
            return train_arr,test_arr
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_model_training(self,train_arr,test_arr):
        try:
            logging.info("Entered the model training method")
            return self.model_trainer.initate_model_training(train_arr,test_arr)
        except Exception as e:
            raise CustomException(e,sys)


    def run_train_pipeline(self):
        try:
            train_data_path,test_data_path=self.initiate_train_pipeline()
            train_arr,test_arr=self.initiate_data_transformation(train_data_path,test_data_path)
            return self.initiate_model_training(train_arr,test_arr)
        except Exception as e:
            raise CustomException(e,sys)
