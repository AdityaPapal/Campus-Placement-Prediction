import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict_api',methods = ['get','post'])
def predict_api():
    data = request.get_json()
    gender = data['gender']
    ssc_p = data['ssc_p']
    hsc_p = data['hsc_p']
    hsc_s = data['hsc_s']
    degree_p = data['degree_p']
    degree_t = data['degree_t']
    workex = data['workex']
    etest_p = data['etest_p']
    specialisation = data['specialisation']
    mba_p = data['mba_p']

    features = [[gender, ssc_p, hsc_p, hsc_s, degree_p, degree_t, workex, etest_p, specialisation, mba_p]]
    output = model.predict(features)
    probability = model.predict_proba(features)
    return jsonify(round(probability[0][1], 2) * 100)
    
if __name__=="__main__":
    app.run(debug=True) 