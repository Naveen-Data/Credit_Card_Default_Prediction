


import os
import sys
sys.path.append('/Users/naveenchaudhary/Documents/ML_Projects/CCDP')
from src.logger import logging
# from src.exception import CustomException/
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_cleaning import DataCleaning
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__=="__main__":
    logging.info("Entered the train pipeline")

    obj=DataIngestion()
    raw_data_path=obj.initiate_data_ingestion()

    DataCleaning_obj=DataCleaning()
    train_data_path,test_data_path=DataCleaning_obj.DataCleaningConfig(raw_data_path)

    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)

    model_trainer_obj=ModelTrainer()
    model_trainer_obj.initate_model_training(train_arr,test_arr)

        # model_eval_obj = ModelEvaluation()
        # model_eval_obj.initiate_model_evaluation(train_arr,test_arr)