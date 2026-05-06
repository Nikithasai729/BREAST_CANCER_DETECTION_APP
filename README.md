# 🧠 Breast Cancer Detection using Neural Network

## 📌 Project Overview
This project is a Machine Learning + Deep Learning based web application that predicts whether a tumor is **Benign or Malignant** using patient data.

It uses a simple Neural Network trained on 3 key medical features and provides real-time predictions through a Flask web app.

---

## 📊 Dataset Used
Breast Cancer Wisconsin Dataset

Features used:
- Mean Radius
- Mean Texture
- Mean Perimeter

Target:
- 0 → Malignant
- 1 → Benign

---

## ⚙️ Tech Stack
- Python
- TensorFlow / Keras
- Scikit-learn
- Flask
- HTML, CSS

---

## 🧠 Model Architecture
- Input Layer: 3 features
- Hidden Layer 1: 16 neurons (ReLU)
- Hidden Layer 2: 8 neurons (ReLU)
- Output Layer: 1 neuron (Sigmoid)

Loss Function: Binary Crossentropy  
Optimizer: Adam  
Epochs: 20  

---

## 🚀 How to Run the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/breast-cancer-app.git
cd breast-cancer-app
Breast Cancer Detection using Machine Learning &amp; Neural Networks  This project is a simple AI-powered web application that predicts whether a tumor is Benign or Malignant using a trained neural network model.

2️⃣ Install dependencies
pip install numpy pandas tensorflow scikit-learn flask

3️⃣ Run the Flask app
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000

📌 Example Inputs:

🔴 Malignant Case
Radius: 17.99
Texture: 10.38
Perimeter: 122.8

🟢 Benign Case
Radius: 11.76
Texture: 21.6
Perimeter: 74.72

📂 Project Structure
breast_cancer_app/
│
├── app.py
├── data.csv
├── model/
│   ├── model.keras
│   ├── scaler.pkl
│
├── templates/
│   └── index.html
│
└── README.md
