import os
import sys
import numpy as np
from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.components.data_ingestion import DataIngestion
from src.KidneyStonePrediction.components.data_transformations import DataTransformation
from src.KidneyStonePrediction.components.model_trainer import ModelTrainer
from src.KidneyStonePrediction.logger import logging

class TrainingPipline():


    def __init__(self):
        logging.info("Setting TrainingPipeline")

    def init_training_pipline(self):

        try: 

            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

            data_transformation = DataTransformation()
            train_data, test_data, _ = data_transformation.initiate_data_transormation(train_data_path, test_data_path)

            model_trainer = ModelTrainer()
            accurr, recall = model_trainer.initiate_model_trainer(train_data,test_data)

            return model_trainer, accurr, recall
        
        except Exception as e:
            raise CustomException(e,sys)