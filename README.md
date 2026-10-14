# ⚡ Electric Vehicle (EV) Range Prediction Using Machine Learning

A machine learning project developed during my **Shell Internship**, covering data preprocessing, regression model training, evaluation, and an interactive Streamlit application with an AI-powered EV assistant.

**Technologies:** Python, Pandas, NumPy, Scikit-learn, Random Forest Regression, Streamlit, Joblib

## 🎯 Project Overview

Electric vehicle range is an important factor when choosing an EV. This project uses machine learning to estimate the driving range of electric vehicles based on vehicle specifications.

The project covers the complete workflow, from dataset preparation and model evaluation to integrating the trained model into a web application.

## 📊 Dataset

- **Dataset:** Electric Vehicle Specifications
- **Source:** Kaggle dataset used in the project
- **Records:** 103
- **Features:** 14 columns
- **Target variable:** `Range_Km`

The dataset includes vehicle specifications such as acceleration, top speed, energy efficiency, fast-charging speed, powertrain, body style, seating capacity, and price.

## 🛠️ Data Preprocessing

- Loaded and inspected the dataset using Pandas.
- Handled missing values and missing-value markers.
- Separated the target variable, `Range_Km`, from the input features.
- Applied median imputation and standardization to numerical features.
- Applied most-frequent-value imputation and one-hot encoding to categorical features.
- Split the data into training and testing sets using an 80:20 ratio.

## 🤖 Model Training and Evaluation

A Random Forest Regressor was trained to predict EV range. The evaluation was performed on a held-out test set.

| Evaluation metric | Result |
|---|---:|
| Algorithm | Random Forest Regressor |
| Training records | 82 |
| Testing records | 21 |
| R² score | 0.4019 |
| Mean Absolute Error (MAE) | 55.915 km |
| Root Mean Squared Error (RMSE) | 89.132 km |

### Understanding the results

- **R² score:** 0.4019 on the test set.
- **MAE:** The average absolute difference between actual and predicted range was approximately 55.915 km.
- **RMSE:** The root mean squared prediction error was approximately 89.132 km.

These metrics correspond to the newly trained model using an 80:20 train-test split with `random_state=42`. Performance may vary with different data splits, particularly because the dataset is small.

## 🖥️ Streamlit Application

The project includes an interactive web application that integrates the trained machine learning pipeline with an EV assistant.

Application features:

- Vehicle specification input form.
- Machine learning-based EV range prediction.
- Estimated days between charges based on daily driving distance.
- AI assistant for EV-related questions.
- Vehicle recommendations and maintenance guidance.
- Charging strategy suggestions.

The application uses a saved model artifact to generate predictions from the supplied vehicle specifications.

## 🧰 Technologies and Libraries

- **Python:** Core programming language.
- **Pandas and NumPy:** Data processing and numerical operations.
- **Scikit-learn:** Preprocessing, model training, and evaluation.
- **Random Forest Regressor:** Range prediction algorithm.
- **Joblib:** Saving and loading the trained model.
- **Streamlit:** Interactive web interface.

## 📁 Project Structure

```text
shell-internship/
├── app.py
├── AIapi.py
├── model_utils.py
├── model.ipynb
├── ElectricCarData_Clean.csv
├── ev_range_model.joblib
├── ev_range_model_v2.joblib
├── feature_list.pkl
├── ev_range_predictions.csv
├── ev_range_report .txt
├── requirements.txt
└── README.md
```

**Note:** Keep `ev_range_model_v2.joblib` in the project only after confirming that it is the model used by the current application. Update or remove obsolete model artifacts and reports to avoid confusion.

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/kartik13112004/shell-internship.git
cd shell-internship
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Start the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

Ensure that the model file expected by `model_utils.py` is present in the project directory.

## 🔮 Future Improvements

- Evaluate model performance using cross-validation.
- Compare Random Forest with gradient-boosting regression algorithms.
- Collect a larger and more diverse EV dataset.
- Investigate additional factors such as temperature, terrain, driving style, and battery degradation.
- Improve prediction reliability through feature engineering and hyperparameter tuning.

## 👨‍💻 Project Outcome

Developed an end-to-end EV range prediction workflow combining data preprocessing, regression modelling, model evaluation, and an interactive application.

The project demonstrates practical experience with Python, Scikit-learn, regression metrics, model persistence, and Streamlit application development.

## 🔗 Repository

[Shell Internship – EV Range Prediction](https://github.com/kartik13112004/shell-internship)
