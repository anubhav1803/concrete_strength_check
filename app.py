# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:54:51 2021

@author: ANUBHAV CHAUHAN
"""

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html', template_folder='Templates')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    if request.method == 'POST':
        Cement = float(request.form['Cement'])
        Blast_Furnace_Slag=float(request.form['Blast_Furnace_Slag'])
        Fly_Ash=float(request.form['Fly_Ash'])
        Water=float(request.form['Water'])
        Superplasticizer=float(request.form['Superplasticizer'])
        Coarse_Aggregate=float(request.form['Coarse_Aggregate'])
        Fine_Aggregate = float(request.form['Fine_Aggregate'])
        Age_in_days=int(request.form['Age_in_days'])
       
       
        prediction=model.predict([[Cement, Blast_Furnace_Slag, Fly_Ash, Water, Superplasticizer,
       Coarse_Aggregate, Fine_Aggregate, Age_in_days]])
        output=round(prediction[0],2)
        
        return render_template('index.html',prediction_text="Strength of Concrete is {} MPa".format(output))

if __name__=="__main__":
    app.run(debug=True)