# ❤️ Heart Disease Prediction System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![ML](https://img.shields.io/badge/Machine%20Learning-KNN-green)
![Backend](https://img.shields.io/badge/FastAPI-API-orange)
![Deployment](https://img.shields.io/badge/Deployed-Vercel-black)

---

## 🌐 Live Demo

🔗 https://heart-disease-ml-system-9rts.vercel.app/

---

## 📌 Project Overview

The **Heart Disease Prediction System** is a Machine Learning-powered web application that predicts the likelihood of heart disease using clinical data.

It leverages a **K-Nearest Neighbors (KNN)** model along with preprocessing techniques to provide fast and accurate predictions through an interactive web interface.

---

## 🎯 Features

- ❤️ Predict heart disease risk (High / Low)
- ⚡ FastAPI backend (high-performance API)
- 🌐 Clean and responsive frontend
- 📊 Real-time prediction system
- 🧠 ML model with preprocessing pipeline
- 🚀 Deployed on Vercel (live project)

---

## 🧰 Tech Stack

### 🔹 Backend
- Python
- FastAPI
- Scikit-learn

### 🔹 Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

### 🔹 Machine Learning
- NumPy
- Pandas
- StandardScaler
- KNN Algorithm

### 🔹 Tools & Deployment
- Git & GitHub
- Postman
- Vercel

---

## 📂 Project Structure
heart-disease-ml-system/
│
├── api/
│ └── index.py # Vercel serverless backend
│
├── models/
│ ├── KNN_heart.pkl
│ ├── scaler_heart.pkl
│ └── columns.pkl
│
├── public/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
├── requirements.txt
├── vercel.json
└── README.md

---

## 📊 Dataset

- **Source:** UCI Heart Disease Dataset  
- **Features:** Age, Blood Pressure, Cholesterol, Chest Pain, etc.  
- **Target:**  
  - `0` → No Heart Disease  
  - `1` → Heart Disease  

---

## 🔄 Machine Learning Pipeline

1. Data Cleaning  
2. Handling Missing Values  
3. Feature Encoding  
4. Feature Scaling (StandardScaler)  
5. Model Training (KNN)  
6. Model Evaluation  

---

## 🤖 Model Details

- **Algorithm:** K-Nearest Neighbors (KNN)  
- **Distance Metric:** Euclidean Distance  
- **K Value:** Optimized for best accuracy  

---

## 📈 Model Performance

- **Accuracy:** ~88%  
- **Precision:** 0.87  
- **Recall:** 0.91  
- **F1 Score:** 0.89  

✅ High recall ensures fewer missed high-risk patients.

---

## 🧪 Sample Prediction

**Input:**
Age: 63
BP: 145
Cholesterol: 233
Oldpeak: 2.3

**Output:**
High Risk of Heart Disease


---

## 🌐 System Architecture

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/heart-disease-ml-system.git
cd heart-disease-ml-system
pip install -r requirements.txt
uvicorn api.index:app --reload

⚠️ Limitations
Small dataset (~1000 samples)
Not a medical diagnosis tool
Limited real-world validation
🚀 Future Improvements
🔥 Deep Learning (ANN / Neural Networks)
☁️ Cloud deployment (AWS / Render)
🔐 User authentication system
📊 Explainable AI (SHAP / LIME)
📱 Mobile app integration
