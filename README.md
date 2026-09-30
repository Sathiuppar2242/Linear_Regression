# 🏠 House Price Prediction using Linear Regression

## 📌 Project Overview

This project implements a Machine Learning model to predict house prices using Linear Regression.

The model learns the relationship between different house features and the price of the house. It includes data preprocessing, model training, evaluation, and visualization.

---

## 🎯 Objectives

- Understand Simple and Multiple Linear Regression
- Perform data preprocessing
- Train a Linear Regression model using Scikit-learn
- Evaluate model performance using MAE, MSE, RMSE, and R² Score
- Visualize predictions and feature impact

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📂 Project Structure
Linear_Regression/

│
├── dataset/
│ └── housing.csv
│
├── output/
│ ├── actual_vs_predicted.png
│ ├── feature_importance.png
│ ├── model_metrics.txt
│ └── predictions.csv
│
├── screenshots/
│
├── report/
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE


---

## 📊 Dataset Description

The dataset contains housing information such as:

- Area
- Number of bedrooms
- Number of bathrooms
- Stories
- Parking availability
- Air conditioning
- Furnishing status
- Location preferences

### Target Variable:
price

The model predicts house prices based on these features.

---

## ⚙️ Project Workflow
Dataset
|
↓
Data Cleaning
|
↓
Feature Encoding
|
↓
Train-Test Split
|
↓
Linear Regression Model
|
↓
Prediction
|
↓
Model Evaluation
|
↓
Visualization


---

## 📈 Model Evaluation Metrics

The model is evaluated using:

### MAE
Measures average prediction error.

### MSE
Measures squared prediction errors.

### RMSE
Shows error magnitude in the same unit as the target.

### R² Score
Shows how well the model explains the data.

---

## 📊 Results

The project generates:

- Actual vs Predicted Price Graph
- Feature Importance Graph
- Model Evaluation Metrics
- Prediction Results

---

## 🚀 How to Run the Project

### 1. Clone Repository
git clone <your-github-link>

### 2. Install Requirements
pip install -r requirements.txt

### 3. Run Application
python main.py


---

## 🔮 Future Improvements

- Try advanced regression algorithms
- Improve accuracy using feature engineering
- Deploy model using Flask/FastAPI
- Create a web-based prediction interface
## 📸 Project Screenshots

### Dataset Exploration

![Dataset Exploration](screenshots/01_dataset_exploration.png)


### Data Quality Check

![Data Quality Check](screenshots/02_data_quality_check.png)


### Features and Target Selection

![Features Target](screenshots/03_features_target.png)


### Data Encoding

![Encoding](screenshots/04_encoding.png)


### Train Test Split

![Train Test Split](screenshots/05_train_test_split.png)


### Model Training

![Model Training](screenshots/06_model_training.png)


### Predictions

![Predictions](screenshots/07_predictions.png)


### Model Evaluation

![Model Evaluation](screenshots/08_model_evaluation.png)


### Actual vs Predicted Graph

![Actual vs Predicted](screenshots/09_actual_vs_predicted.png)


### Feature Importance

![Feature Importance](screenshots/11_feature_importance.png)


### Final Execution

![Final Execution](screenshots/13_final_execution.png)

---

## 👨‍💻 Author

**Sathish R**

B.E Computer Science Engineering
## Project Objectives

- Build a simple linear regression model using Python
- Understand the relationship between input and target variables
- Train the model using prepared dataset features
- Generate predictions using the trained regression model

## Key Features

- Load and prepare dataset for regression analysis
- Train a Linear Regression model
- Generate predictions from input data
- Evaluate model performance using regression metrics
- Save generated results for further analysis
