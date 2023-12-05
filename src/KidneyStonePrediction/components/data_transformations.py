import sys
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.KidneyStonePrediction.utils import save_object

from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.logger import logging

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation
        '''
        try:
            numerical_columns = ["gravity", "ph", "osmo", "cond", "urea", "calc"]
           
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('normalize',StandardScaler())
            ])
            
            logging.info(f"Numerical Columns:{numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                ]

            )
            return preprocessor
            

        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transormation(self,train_path,test_path):
        try:

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Reading the train and test file")

            preprocessing_obj=self.get_data_transformer_object()
        
            ## divide the train dataset to independent and dependent feature

            train_x_df = train_df.iloc[:,:-1]
            train_y_df = train_df.iloc[:,-1:]

            ## divide the test dataset to independent and dependent feature

            test_x_df = test_df.iloc[:,:-1]
            test_y_df = test_df.iloc[:,-1:]

            logging.info("Applying Preprocessing on training and test dataframe")

            train_x_norm = preprocessing_obj.fit_transform(train_x_df)
            test_x_norm = preprocessing_obj.fit_transform(test_x_df)
            
            logging.info(train_x_norm)
            
            train_arr = np.c_[
                train_x_norm, train_y_df
            ]
            test_arr = np.c_[test_x_norm, test_y_df]

            logging.info(f"Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (

                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise CustomException(e,sys)