from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pickle

app = Flask(__name__)

# Load model & scaler
model = tf.keras.models.load_model("model/model.keras")

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs
        radius = float(request.form['radius'])
        texture = float(request.form['texture'])
        perimeter = float(request.form['perimeter'])

        # Convert to array
        input_data = np.array([[radius, texture, perimeter]])

        # Scale
        input_data_std = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_data_std)

        prob = prediction[0][0]

        # FIXED LABEL LOGIC (IMPORTANT)
        if prob < 0.5:
            result = "Malignant"
            confidence = (1 - prob) * 100
        else:
            result = "Benign"
            confidence = prob * 100

        return render_template('index.html',
                               prediction_text=f"Result: {result}",
                               confidence=f"Confidence: {confidence:.2f}%")

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)