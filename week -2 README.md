# ⚡ Predicting Electric Vehicle (EV) Range using Machine Learning

This project was developed as part of my **Shell Internship** to predict the **driving range of Electric Vehicles (EVs)** using Machine Learning techniques.  
The project demonstrates the complete data science workflow — from data preprocessing to model building, evaluation, and deployment readiness.

---

## 🚗 Project Overview

Electric Vehicles (EVs) are a key component of sustainable transportation.  
However, one common issue is **range anxiety** — the fear that an EV might run out of charge before reaching its destination.  

To solve this, I built a **Machine Learning model** that accurately predicts the **driving range (in km)** of an EV based on its specifications such as battery capacity, weight, energy consumption, and efficiency.

---

## 🧠 Objectives

- To analyze EV data and identify key factors affecting range.  
- To train ML models to predict the **driving range** of an electric vehicle.  
- To evaluate and compare model performance (Linear Regression vs Random Forest).  
- To visualize the importance of different EV features.

---

## 📊 Dataset Information

- **Source:** [Kaggle - Electric Vehicle Dataset](https://www.kaggle.com/)  
- **File Used:** `ElectricCarData_Clean.csv`
- **Target Variable:** `Range (km)` (dependent variable)
- **Feature Variables:**
  - Battery Capacity (kWh)
  - Energy Consumption (Wh/km)
  - Vehicle Weight (kg)
  - Efficiency
  - Acceleration (0–100 km/h)
  - Top Speed

---

## 🧩 Data Preprocessing

1. Imported dataset using **Pandas**  
2. Handled missing values (if any)  
3. Encoded categorical features using **LabelEncoder / OneHotEncoder**  
4. Normalized numerical columns  
5. Split data into:
   - **80% Training set**
   - **20% Test set**

---

## ⚙️ Machine Learning Models Used

| Model | Description | R² Score | MAE (km) | RMSE (km) |
|:------|:-------------|:---------:|:---------:|:----------:|
| **Linear Regression** | Simple baseline model | 0.29 | 65.8 | 97.0 |
| **Random Forest Regressor** | Ensemble model (best performer) | 0.84 | 15.2 | 25.6 |

✅ **Best Model:** Random Forest Regressor  
✅ **Evaluation Metrics:** R², MAE, RMSE  
✅ **Tools Used:** Python, Scikit-learn, Pandas, Matplotlib, Seaborn, Google Colab

---

## 📈 Visualizations

The notebook includes the following plots:

- 📊 **Actual vs Predicted Range** (Scatter Plot)  
- 🌲 **Feature Importance Chart** (Random Forest)  
- 📉 **Distribution of Range Values** (Histogram)  
- 🔍 **Correlation Heatmap** between features  

All plots were created using `Matplotlib` and `Seaborn`.

---

## 🧾 Results Summary

- Random Forest achieved **R² = 0.84**, significantly outperforming Linear Regression.  
- **Battery capacity** and **energy consumption** were the most important predictors of EV range.  
- **Vehicle weight** and **efficiency** also had strong correlations with range.  
- The model generalizes well and can be used to estimate range for new EV specifications.

---

## 🚀 Project Files

| File | Description |
|------|--------------|
| `ElectricCarData_Clean.csv` | Cleaned dataset used for training |
| `ev_range_model.joblib` | Trained Random Forest model |
| `ev_range_predictions.csv` | Contains actual vs predicted test results |
| `ev_range_report.txt` | Text summary report of results |
| `EV_Range_Prediction.ipynb` | Colab notebook with full code |
| `README.md` | Project documentation (this file) |

---

## 🧠 How the Model Works

1. Input EV specs (battery, weight, etc.)  
2. Model preprocesses inputs to the same format as training data  
3. Random Forest algorithm predicts the expected driving range (km)  
4. Output: **Predicted Range** with reasonable accuracy  

Example (Python code):
```python
import joblib
model = joblib.load('ev_range_model.joblib')

# Example new EV specs: [battery, weight, top_speed, efficiency]
new_ev = [[75, 1800, 160, 0.85]]
prediction = model.predict(new_ev)
print("Predicted EV Range (km):", round(prediction[0], 2))
