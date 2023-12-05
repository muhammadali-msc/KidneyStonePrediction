import os
import sys
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor


from src.KidneyStonePrediction.execption import CustomException
from src.KidneyStonePrediction.logger import logging
from src.KidneyStonePrediction.utils import save_object

from tensorflow import keras
import tensorflow as tf
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score


from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainerConfig()

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            model = keras.Sequential()
            model.add(keras.Input(shape=(6,)))
            model.add(keras.layers.Dense(256, activation= 'relu'))
            model.add(keras.layers.Dense(1,  activation='sigmoid'))

            model.summary()
            # Compile the model for binary classification
            model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

            # Train the model
            model.fit(X_train, y_train, epochs=15, batch_size=32)

            # Evaluate the model on the test set
            loss, accuracy = model.evaluate(X_test, y_test)


            # Make predictions on new data
            perdict_y = model.predict(X_test)
            #perdict_y = tf.squeeze(y_test)
            perdict_y = np.array([1 if x >= 0.5 else 0 for x in perdict_y])
            
            #confusion_metrics = confusion_matrix(test_y['target'].to_numpy(), perdict_y)
            accurr = accuracy_score(y_test, perdict_y)
            recall = recall_score(y_test, perdict_y, average='weighted')

            print(accurr)
            print(recall)


            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model
            )

            
            return accurr, recall
        except Exception as e:
            raise CustomException(e,sys)