import numpy as np
from flask import Flask, abort, jsonify, request
import pickle as pickle

model = pickle.load(open("lactate_model.pkl", "rb"))

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

if __name__ == '__main__':
    app.run(port=9000, debug=True)
