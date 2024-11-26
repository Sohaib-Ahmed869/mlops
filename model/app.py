from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

# Get the absolute path to the directory where app.py is located
model_dir = os.path.dirname(os.path.abspath(__file__))

# Load your pre-trained model and label encoder using absolute paths
model = joblib.load(os.path.join(model_dir, "weather_condition_model.pkl"))
label_encoder_city = joblib.load(os.path.join(model_dir, "label_encoder_city.pkl"))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        # Extract features from request
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        wind_speed = float(data['windSpeed'])
        city = data['city']
        day = int(data['day'])
        hour = int(data['hour'])

        # Encode the city
        encoded_city = label_encoder_city.transform([city])[0]

        # Prepare input for the model
        input_data = {
            'temperature': [temperature],
            'humidity': [humidity],
            'windSpeed': [wind_speed],
            'city': [encoded_city],
            'day': [day],
            'hour': [hour]
        }
        X = pd.DataFrame(input_data)

        # Make prediction
        prediction = model.predict(X)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
