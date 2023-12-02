import os
import sys
import pandas as pd
from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise CustomException(e, sys)