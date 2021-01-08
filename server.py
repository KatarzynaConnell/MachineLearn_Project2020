# flask for web app.
import flask
from flask import Flask, request, jsonify
# numpy for numerical work.
import requests
import joblib
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pickle

# load the model
with open('polynomial_model.pkl', 'rb') as file:  
    Pickled_polyn_model = pickle.load(file)

Pickled_LR_Model


# Create a new web app.
app = Flask(__name__)

# Add root route for the home page.
@app.route("/")
def home():

# Add polynomial regression model (json)
@app.route('polynomial_model', method=['POST'])
def polynomial_model():
    wind = request.form['input']
# for wind speeds that are less than 0.3 and above 24.499 return 0 
        if wind > 24.5:  
            power = 0
        return jsonify({'name' : float(power)})
    
  # pass to model for wind speeds between 0.3 and 24.499	
        if 0.3 < wind < 24.5:
            power = polyn_model.predict(polyn_features.fit_transform([[wind]]))
            power = power.item(0)
        return jsonify({'name' : float(power)})
 
        if wind < 0.3: 
            print("Missing data!")

if __name__ == '__main__':
    app.run(debug = True)