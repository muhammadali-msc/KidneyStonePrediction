import os
import sys
import numpy as np
from src.KidneyStonePrediction.execption import CustomException

from src.KidneyStonePrediction.piplines.training_pipline import TrainingPipline
from src.KidneyStonePrediction.piplines.prediction_pipline import PredictionPipline
from flask import Flask, redirect, render_template, request

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('/index.html', result = 0)
    else:

        gravity = float(request.form['gravity'])
        ph = float(request.form['ph'])
        osmo = float(request.form['osmo'])
        cond = float(request.form['cond'])
        urea = float(request.form['urea'])
        calc = float(request.form['calc'])
        
        prediction_pipline = PredictionPipline()
        predict = prediction_pipline.model_predict(np.array([[gravity,ph,osmo,cond,urea,calc]]))
        if predict:
            results = "KidneyStone is present"
        else:
            results = "KidneyStone is not present"

        
        return render_template('/index.html',result=results)
    
    
if __name__ == "__main__":
    
    app.run(debug = True, host='0.0.0.0')

    training_pipline = TrainingPipline()
    model_trainer, accurr, recall = training_pipline.init_training_pipline()
    