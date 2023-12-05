import sys
import os
import numpy as np

from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.logger import logging

import pickle

class PredictionPipline:
    def __init__(self):
        
        logging.info("Init the Prediction Pipline")
        
        self.pickled_model = pickle.load(open('artifacts/model.pkl', 'rb'))
    
    def model_predict(self, x_test):
        try:

            perdict_y = self.pickled_model.predict(x_test)
            
            perdict_y = np.array([1 if x >= 0.5 else 0 for x in perdict_y])
            
            if perdict_y == 1:
                return True
            else:
                return False
            
        except Exception as e:
            raise CustomException(e,sys)