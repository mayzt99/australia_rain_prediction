import pickle
from flask import Flask
from flask import request
from flask import jsonify

model_file = f'rain_model.bin'

with open(model_file, 'rb') as f_in:
    dv, scaler, model = pickle.load(f_in)

app = Flask('rain')

@app.route('/predict_rain', methods=['POST'])
def predict():
    weather_info = request.get_json()

    X = dv.transform(weather_info)
    X = scaler.transform(X)
    y_pred = model.predict_proba(X)[0, 1]
    rain = y_pred >= 0.5
    result = {
        "rain_probability" : float(y_pred),
        "rain" : bool(rain)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)