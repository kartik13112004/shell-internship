# EV Range Advisor - Week 3

## Overview
This project is an Electric Vehicle (EV) Range Advisor application built using Streamlit. It provides users with an interactive interface to predict EV range based on vehicle specifications and offers AI-powered insights, recommendations, maintenance tips, and charging strategies.

## Features
- **Range Prediction**: Predicts EV range using a machine learning model based on battery capacity and efficiency.
- **Vehicle Inputs**: Allows users to input battery capacity, efficiency, MSRP, daily driving distance, make, and model name.
- **AI Chat Assistant**: Integrated AI assistant for answering questions about EVs, providing recommendations, maintenance tips, and charging strategies.
- **Interactive UI**: User-friendly Streamlit interface with sidebar status and result display.

## Technologies Used
- **Streamlit**: For building the web application.
- **Scikit-learn / Joblib**: For loading and using the pre-trained machine learning model.
- **Pandas**: For data manipulation in predictions.
- **AI API**: Custom AI assistant for generating insights and responses.

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/kartik13112004/shell-internship.git
   cd EV_RANGE_PROJECT
   ```

2. Install dependencies:
   ```
   pip install streamlit pandas joblib scikit-learn
   ```

3. Ensure the model file `ev_range_model.joblib` and `feature_list.pkl` are in the project directory.

## Usage
1. Run the Streamlit app:
   ```
   streamlit run streamlit_app_enhanced.py
   ```

2. Open the provided URL in your browser.

3. Enter vehicle details in the left column and click "Predict Range" to get predictions and AI insights.

4. Use the AI Chat Assistant in the right column to ask questions about EVs.

## Files Description
- `streamlit_app_enhanced.py`: Main Streamlit application file.
- `model_utils.py`: Utilities for loading the model and making predictions.
- `AIapi.py`: AI assistant implementation.
- `ev_range_model.joblib`: Pre-trained machine learning model.
- `feature_list.pkl`: Feature list for the model.
- `ElectricCarData_Clean.csv`: Dataset used for training (if applicable).

## Model Details
The model predicts EV range based on features like battery capacity, efficiency, acceleration, top speed, etc. It uses a regression model trained on electric car data.

## Contributing
Feel free to fork the repository and submit pull requests for improvements.

## License
This project is for educational purposes.
