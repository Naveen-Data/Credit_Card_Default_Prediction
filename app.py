


import os
import sys
from src.logger import logging
# from src.exception import CustomException/
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_cleaning import DataCleaning
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.utils import evaluate_models
# from src.components.baseline_model import base_model


if __name__=="__main__":
    logging.info("Entered the train pipeline")

    obj=DataIngestion()
    raw_data_path=obj.initiate_data_ingestion('data')

    DataCleaning_obj=DataCleaning()
    train_data_path,test_data_path=DataCleaning_obj.DataCleaningConfig(raw_data_path)

    data_transformation=DataTransformation()
    train_arr,test_arr=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    model_trainer_obj=ModelTrainer()
    print(model_trainer_obj.initiate_model_trainer(train_arr,test_arr))

    # base_model = base_model()
    # print(base_model)

    