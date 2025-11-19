# ⚡ Electric Vehicle (EV) Range Prediction – Complete Project (Week 1, 2 & 3)

This repository contains my **Shell Internship project**, completed across **three structured weeks**, covering the full lifecycle of an EV Range Prediction system:

- **Week 1 → Data Understanding & Problem Definition**
- **Week 2 → Model Building, Training & Evaluation**
- **Week 3 → Chatbot + Streamlit Frontend Application**

The goal is to predict the **driving range (km)** of Electric Vehicles using Machine Learning and expose the model through an interactive **web-based chatbot application**.

---

# 🧠 Week 1 – Problem Definition, Dataset Study, and Setup

## 🚗 Project Overview
Electric Vehicles (EVs) are the future of sustainable mobility, but **range anxiety** is a major concern among users.  
To solve this, the project aims to build a Machine Learning model that can predict **how far an EV can travel** based on its parameters like battery capacity, weight, efficiency, etc.

### ❓ Problem Statement
The EV range depends on:
- Battery size  
- Temperature  
- Weight  
- Speed  
- Road conditions  
- Motor efficiency  

Traditional methods are Not accurate → So we use **Machine Learning** to predict range more intelligently.

---

## 📊 Dataset (Kaggle)
Dataset: **Electric Vehicle Range Prediction — Regression Analysis**  
Contains features like:

- Battery Capacity (kWh)  
- Range (km)  
- Efficiency  
- Acceleration  
- Top Speed  
- Weight  

### ✔ Week 1 Tasks Completed
- Understood dataset & problem  
- Identified features and target variable  
- Installed required libraries  
- Setup development environment (Colab + Python)  
- Researched EV range factors

---

# 🧪 Week 2 – Data Preprocessing, Model Training & Evaluation

## 🛠 Preprocessing Steps
- Loaded dataset into Pandas  
- Cleaned data (handled missing values)  
- Encoded categorical columns  
- Normalized numeric features  
- Split into **80% train** and **20% test**

---

## 🤖 ML Models Used
Two models were trained:

| Model | R² Score | MAE | RMSE | Notes |
|-------|----------|------|--------|-------|
| **Linear Regression** | 0.29 | 65.8 km | 97.0 km | Baseline model |
| **Random Forest Regressor** | **0.84** | **15.2 km** | **25.6 km** | Best performing |

✔ **Winner Model: Random Forest Regressor**  
✔ Saved as `ev_range_model.joblib`  
✔ Feature order saved as `feature_list.pkl`

---

## 📈 Visualizations Included
- Range Distribution  
- Feature Importance (Random Forest)  
- Heatmap correlation  
- Actual vs Predicted scatter plot  

---

## 📄 Week-2 Deliverables
- `EV_Range_Prediction.ipynb`  
- `ElectricCarData_Clean.csv`  
- `ev_range_model.joblib`  
- `feature_list.pkl`  
- `ev_range_predictions.csv`  
- Model evaluation metrics  

---

# 🧩 Week 3 – Streamlit Frontend + AI Chatbot

## 🎯 Goal
Convert the ML model into a **user-friendly application** with:

- 🔹 Streamlit UI  
- 🔹 EV Chatbot (NLU-based)  
- 🔹 Range Predictor form  
- 🔹 Public deployment using ngrok/Streamlit Cloud  

---

## 💬 Chatbot Features
The chatbot understands:

- Free text like:  
  *"battery 75 speed 80 weight 1600"*  
  *"I drive in eco mode, what is the range?"*

- Extracts numbers using regex  
- Maps driving styles (`eco`, `normal`, `sport`)  
- Detects:
  - greeting  
  - predict intent  
  - FAQ questions  

✔ Predicts EV range through the conversation  
✔ Uses same model backend (`ev_range_model.joblib`)

---

## 🖥 Streamlit Frontend Features
- Two main tabs:
  - 💬 **Chatbot Interface**  
  - 📈 **Predict Form**  

- Shows:
  - Predicted range  
  - Missing features  
  - Friendly UI messages  

✔ Works locally  
✔ Works in Google Colab using ngrok  
✔ Fully integrated with ML model  

---

# 📦 Technologies Used

### **Programming**
Python

### **Libraries**
- Streamlit  
- pandas  
- numpy  
- scikit-learn  
- joblib  
- pyngrok  
- regex / NLU patterns  

### **Environment**
- Google Colab  
- Jupyter Notebook  
- Streamlit browser app  

---

# 🚀 How to Run Locally

```bash
pip install streamlit pandas numpy scikit-learn joblib
streamlit run app.py
