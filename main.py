# ==========================================
# House Price Prediction using Linear Regression
# ==========================================

# Import Libraries
import os

# Create logs folder automatically
os.makedirs("logs", exist_ok=True)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. Load Dataset
# ==========================================

df = pd.read_csv("dataset/housing.csv")

print("Dataset Loaded Successfully")
# Save dataset exploration report

with open("logs/01_dataset_exploration.txt", "w") as file:
    file.write("Dataset Exploration Report\n")
    file.write("=========================\n\n")

    file.write("First 5 Rows:\n")
    file.write(str(df.head()))

    file.write("\n\nDataset Shape:\n")
    file.write(str(df.shape))

    file.write("\n\nColumns:\n")
    file.write(str(df.columns.tolist()))

    file.write("\n\nData Types:\n")
    file.write(str(df.dtypes))

    # ==========================================
# Data Quality Check
# ==========================================

with open("logs/02_data_quality_check.txt", "w") as file:

    file.write("Data Quality Report\n")
    file.write("==================\n\n")

    file.write("Missing Values:\n")
    file.write(str(df.isnull().sum()))

    file.write("\n\nDuplicate Rows:\n")
    file.write(str(df.duplicated().sum()))


# ==========================================
# 2. Data Preprocessing
# ==========================================

X = df.drop("price", axis=1)
y = df["price"]
# Save Feature Selection Report

with open("logs/03_feature_selection.txt", "w") as file:

    file.write("Feature Selection Report\n")
    file.write("=======================\n\n")

    file.write("Input Features (X):\n")
    file.write(str(X.columns.tolist()))

    file.write("\n\nTarget Variable:\n")
    file.write("price")


# ==========================================
# 2. Data Preprocessing
# ==========================================

# Separate Features and Target

X = df.drop("price", axis=1)
y = df["price"]


# Convert categorical values into numerical values

X = pd.get_dummies(X, drop_first=True)
# Save Encoding Report

with open("logs/04_encoding_report.txt", "w") as file:

    file.write("Data Encoding Report\n")
    file.write("===================\n\n")

    file.write("Features After Encoding:\n")
    file.write(str(X.columns.tolist()))

    file.write("\n\nSample Encoded Data:\n")
    file.write(str(X.head()))


# ==========================================
# 3. Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 4. Train Linear Regression Model
# ==========================================

model = LinearRegression()

model.fit(X_train, y_train)

print("Model Training Completed")

# Save Model Training Report

with open("logs/05_model_training.txt", "w") as file:

    file.write("Linear Regression Model Training Report\n")
    file.write("=====================================\n\n")

    file.write("Algorithm Used:\n")
    file.write("Linear Regression\n")

    file.write("\nTraining Status:\n")
    file.write("Model trained successfully\n")

    file.write("\nTraining Data Shape:\n")
    file.write(str(X_train.shape))

    file.write("\n\nTesting Data Shape:\n")
    file.write(str(X_test.shape))


# ==========================================
# 5. Prediction
# ==========================================

y_pred = model.predict(X_test)


# ==========================================
# 6. Model Evaluation
# ==========================================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)
# Save Model Evaluation Report

with open("logs/06_model_evaluation.txt", "w") as file:

    file.write("Linear Regression Model Evaluation Report\n")
    file.write("=======================================\n\n")

    file.write(f"Mean Absolute Error (MAE): {mae}\n")

    file.write(f"Mean Squared Error (MSE): {mse}\n")

    file.write(f"Root Mean Squared Error (RMSE): {rmse}\n")

    file.write(f"R2 Score: {r2}\n")


print("\nModel Performance")

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)


# ==========================================
# 7. Actual vs Predicted Graph
# ==========================================

plt.figure(figsize=(8,5))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")

plt.title("Actual vs Predicted House Prices")

plt.savefig("output/actual_vs_predicted.png")

plt.show()


# ==========================================
# 8. Feature Coefficients
# ==========================================

coefficients = pd.DataFrame({

    "Feature": X.columns,

    "Coefficient": model.coef_

})


coefficients = coefficients.sort_values(
    by="Coefficient",
    ascending=False
)


print("\nFeature Coefficients")

print(coefficients)


# ==========================================
# 9. Feature Importance Graph
# ==========================================

plt.figure(figsize=(10,6))

plt.barh(
    coefficients["Feature"],
    coefficients["Coefficient"]
)

plt.xlabel("Coefficient Value")

plt.ylabel("Features")

plt.title("Feature Impact on House Price")

plt.tight_layout()

plt.savefig("output/feature_importance.png")

plt.show()


# ==========================================
# 10. Save Results
# ==========================================

with open("output/model_metrics.txt", "w") as file:

    file.write("Linear Regression Evaluation\n")
    file.write("---------------------------\n")
    file.write(f"MAE: {mae}\n")
    file.write(f"MSE: {mse}\n")
    file.write(f"RMSE: {rmse}\n")
    file.write(f"R2 Score: {r2}\n")


results = pd.DataFrame({

    "Actual Price": y_test,

    "Predicted Price": y_pred

})


results.to_csv(
    "output/predictions.csv",
    index=False
)


print("\nResults Saved Successfully!")