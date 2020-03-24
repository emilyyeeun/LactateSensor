import numpy as np
from flask import Flask, abort, jsonify, request
import pickle as pickle

model = pickle.load(open("lactate_model.pkl", "rb"))

app = Flask(__name__)

@app.route('/api', methods=['POST', 'GET'])
def make_predict():
    if (request.method == 'POST'):
        dataOne = request.get_json(force=True)
        return jsonify(dataOne)
    else:
        dataTwo = request.get_json(force=True)
        predict_request = [data['Age'], data['Male'], data['Height'], data['Glucose'], data['Weight'], data['Sp02'], data['HeartRate']]
        predict_request = np.array(predict_request)
        predict_request = predict_request.reshape(-1, 7)
        y_hat = model.predict(predict_request)
        output = [y_hat[0]]
        output = str(output)
        return jsonify(result = output)


if __name__ == '__main__':
    app.run(port=9000, debug=True)
