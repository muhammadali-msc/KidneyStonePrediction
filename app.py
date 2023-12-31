import os
import sys
import numpy as np
from src.KidneyStonePrediction.execption import CustomException

from src.KidneyStonePrediction.piplines.training_pipline import TrainingPipline
from src.KidneyStonePrediction.piplines.prediction_pipline import PredictionPipline
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, static_url_path='/assets', static_folder='assets')

@app.route("/", methods = ['GET'])
def index():

        return render_template('/index.html', result = "")
    
@app.route("/predict", methods = ['POST'])
def predict():
    results = ""
    gravity = float(request.form['gravity'])
    ph = float(request.form['ph'])
    osmo = float(request.form['osmo'])
    cond = float(request.form['cond'])
    urea = float(request.form['urea'])
    calc = float(request.form['calc'])
    
    prediction_pipline = PredictionPipline()
    
    predict = prediction_pipline.model_predict(np.array([[gravity,ph,osmo,cond,urea,calc]]))
    
    if predict:
        results = "\nFrom these parameters—Gravity: {}, pH: {}, Osmo: {}, Cond: {}, Urea: {}, and Calc: {}\n the prediction strongly indicates the presence of kidney stones.".format(gravity,ph,osmo,cond,urea,calc)
    else:
        results = "\nFrom these parameters—Gravity: {}, pH: {}, Osmo: {}, Cond: {}, Urea: {}, and Calc: {}\n the prediction strongly indicates the absense of kidney stones.".format(gravity,ph,osmo,cond,urea,calc)
    
    return render_template('/index.html', result = results)

if __name__ == "__main__":
    
    training_pipline = TrainingPipline()

    model_trainer, accurr, recall = training_pipline.init_training_pipline()

    app.run(host='0.0.0.0', port = 8080)

    
    