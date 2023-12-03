import os
import sys
import pandas as pd
from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.components.data_ingestion import DataIngestion
from src.KidneyStonePrediction.components.data_transformations import DataTransformation

if __name__ == "__main__":
    try:
        
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

        data_transformation = DataTransformation()
        data_transformation.initiate_data_transormation(train_data_path, test_data_path)

    except Exception as e:
        raise CustomException(e, sys)