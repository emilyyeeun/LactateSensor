import numpy as np
from flask import Flask, abort, jsonify, request
# import pickle as pickle

from lactate_model import predict_lactate as model_predict

# model = pickle.load(open("lactate_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def make_predict():
    data = request.get_json(force=True)
    predict_request = [np.float32(data["Age"]), np.float(data["Male"]), np.float(data["Height"]), np.float(data["Glucose"]), np.float(data["Weight"]), np.float(data["Sp02"]), np.float(data["HeartRate"])]
    print(type(predict_request))
    predict_request = np.array(predict_request)
    predict_request = predict_request.reshape(-1, 7) #1d to 2d array
    y_hat = model.predict(predict_request)
    output = [y_hat[0]]
    output = str(output)
    return jsonify(result = output)

@app.route('/hello', methods=['POST'])
def return_hello():
    return jsonify(result = "hello")

@app.route('/predict_lactate', methods=['POST'])
def predict_lactate():
    """
    @param: json: {
        'age': <INT> (years), 
        'gender': <STRING> ('Male' or 'Female'), 
        'height': <DOUBLE> (inches),`
        'glucose': <DOUBLE> (mg/dL),
        'weight': <DOUBLE> (lbs),
        'sp02': <DOUBLE> (%),
        'heart_rate': <DOUBLE> (bpm) }

    """
    lactate_params = request.get_json(force=True)

    age = lactate_params.get('age')
    gender = lactate_params.get('gender')
    height = lactate_params.get('height')
    glucose = lactate_params.get('glucose')
    weight = lactate_params.get('weight')
    sp02 = lactate_params.get('sp02')
    heart_rate = lactate_params.get('heart_rate')

    predicted_lactate = model_predict(
        gender, age, height, weight, sp02, heart_rate, glucose)
    
    return jsonify({'predicted_lactate': predicted_lactate})


if __name__ == '__main__':
    app.run(port=9000, debug=True)
