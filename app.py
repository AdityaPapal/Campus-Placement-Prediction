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


@app.route('/predict_api',methods = ['post'])
def predict_api():
    data=request.json['data']
    print(data)
    print((list(data.values())))
    new_data = scalar.transformnp.array((list(data.values())).reshape(-1, 1))
    output = model.predict(new_data.reshape(-1, 1))
    print(output)
    return jsonify(output)

if __name__=="__main__":
    app.run(debug=True)

'''
{
    "data": {
        "gender": 0,
        "ssc_p": 67.0,
        "hsc_p": 91.0,
        "hsc_s": 1,
        "degree_p": 58.0,
        "degree_t": 2,
        "workex": 0,
        "etest_p": 55.0,
        "specialisation": 1,
        "mba_p": 58.8 
    }
}

'''