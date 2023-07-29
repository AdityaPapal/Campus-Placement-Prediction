import pickle
from flask import Flask, request, jsonify, render_template
from prediction_pipline import PredictPipline, CustomData
from logger import logging

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            ssc_p=float(request.form.get("ssc_p")),
            hsc_p=float(request.form.get("hsc_p")),
            hsc_s=int(request.form.get("hsc_s")),
            degree_p=float(request.form.get("degree_p")),
            degree_t=int(request.form.get("degree_t")),
            workex=int(request.form.get("workex")),
            etest_p=float(request.form.get("etest_p")),
            specialisation=int(request.form.get("specialisation")),
            mba_p=float(request.form.get("mba_p")),
        )

        final_data = data.get_data_as_data_frame()
        predict_pipline = PredictPipline()
        pred = predict_pipline.predict(final_data)
        # pred = predict_pipline.(final_data)
        result = pred

        if result == 1:
            return render_template("home.html", final_result="The Probability of getting placement is {}".format(result))
        elif result == 0:
            return render_template("home.html", final_result="The Probability of getting placement is low WORK HARD!{}".format(result))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
