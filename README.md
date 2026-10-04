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

## Linear Regression Workflow

1. Load the dataset
2. Inspect and prepare the data
3. Select input and target variables
4. Split the data into training and testing sets
5. Train the Linear Regression model
6. Generate predictions
7. Evaluate the model results

## Model Evaluation

- Evaluate predictions using regression performance metrics
- Compare predicted values with actual target values
- Analyze model performance on test data
- Use evaluation results to understand prediction quality

## Dataset

- Contains the data used for training and testing the regression model
- Includes input features and the target variable
- Dataset is prepared before model training
- Organized inside the dataset directory

## Model Training

- Training data is used to fit the linear regression model
- Model learns the relationship between input features and the target value
- Training process prepares the model for prediction
- Trained model results are used during evaluation

## Prediction

- The trained model generates predictions from input feature values
- Predictions are produced using the learned linear relationship
- Input data is processed before generating the predicted value
- Prediction results can be reviewed in the output directory

## Project Output

- Stores generated prediction results and model outputs
- Output files help review the results of the regression model
- Results can be used to verify model predictions
- Output artifacts are organized inside the output directory

## Project Limitations

- Linear regression assumes a suitable relationship between features and the target
- Model performance depends on the quality of the dataset
- Outliers and noisy data can affect prediction accuracy
- Results may vary when the model is applied to different datasets

## Model Performance

- Model performance is evaluated using the test dataset
- Evaluation metrics help measure prediction quality
- Performance results can be used to understand model behavior
- Evaluation supports comparison between predicted and actual values

## Technologies Used

- Python for model development and data processing
- Pandas for dataset handling and analysis
- NumPy for numerical operations
- Scikit-learn for building and evaluating the linear regression model

## How to Run

1. Clone the repository
2. Create and activate a Python virtual environment
3. Install the required dependencies
4. Run the main Python program
5. Review the generated prediction and evaluation results

## Future Improvements

- Experiment with additional regression algorithms
- Add more feature engineering techniques
- Improve model evaluation and visualization
- Expand the dataset for broader testing

## Project Structure

- dataset/ - stores project dataset files
- logs/ - stores execution and processing logs
- output/ - stores generated model results
- main.py - contains the main project workflow
- README.md - provides project documentation

## Usage

- Prepare the required input dataset
- Run the project workflow through the main Python program
- Train the linear regression model using the prepared data
- Generate predictions for the test data
- Review the model evaluation and output results

## Conclusion

- This project demonstrates the basic workflow of linear regression
- It covers data preparation, model training, prediction, and evaluation
- The project provides a foundation for exploring regression-based machine learning
- The documented workflow can be extended with additional datasets and models

## Requirements

- Python 3.x
- Pandas for data processing
- NumPy for numerical operations
- Scikit-learn for machine learning
- A compatible dataset for training and testing
