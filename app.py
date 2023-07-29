from flask import Flask,request,jsonify,render_template
from sources.prediction_pipline import PredictPipline,CustomData
from logger import logging

application = Flask(__name__)
app = application


@app.route("/",methods=["GET","POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")

    else:
        data = CustomData(
        ssc_p = float(request.form.get("ssc_p")),
        hsc_p = float(request.form.get("hsc_p")),
        hsc_s = int(request.form.get("hsc_s")),
        degree_p = float(request.form.get("degree_p")),
        degree_t = int(request.form.get("degree_t")),
        workex = int(request.form.get("workex")),
        etest_p = float(request.form.get("etest_p")),
        specialisation = int(request.form.get("specialisation")),
        mba_p = float(request.form.get("mba_p")),
        )

    final_data = data.get_data_as_data_frame()
    predict_pipline = PredictPipline()
    pred = predict_pipline.predict(final_data)

    result = pred

        
    if result == 1:
        return render_template("form.html",final_result = "congratulations You Are Placed:{}".format(result))

    elif result == 0:
        return render_template("form.html",final_result = "Best OF Luck Try Next Time, You Not  Placed:{}".format(result))



if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
