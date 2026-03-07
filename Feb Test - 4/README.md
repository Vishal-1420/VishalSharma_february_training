# House Price Prediction using Supervised Machine Learning

## Project Title

House Price Prediction using Supervised Learning Algorithms

---

## Problem Statement

The objective of this project is to predict house prices using supervised machine learning techniques. The project involves data preprocessing, model training, and evaluating multiple regression algorithms to determine which model performs best.

---

## Dataset Description

The dataset contains information about different houses and their characteristics. These features are used to predict the selling price of a house.

Some important features in the dataset include:

* Bedrooms
* Bathrooms
* Square footage of living area
* Square footage of lot
* Number of floors
* Waterfront availability
* View rating
* House condition
* Square footage above ground
* Square footage basement
* Year built
* Year renovated
* Year and month of sale

The **target variable** is:

**Price → House selling price**

---

## Files Included in the Project

The repository contains the following files:

* **house price.csv**
  Dataset used for training and testing the machine learning models.

* **ml_models.ipynb**
  Google Colab / Jupyter Notebook containing all the code for:

  * Data preprocessing
  * Model training
  * Model evaluation

* **README.md**
  Documentation explaining the project, dataset, preprocessing steps, algorithms used, and results.

---

## Data Preprocessing

Before applying machine learning algorithms, several preprocessing steps were performed:

### Handling Missing Values

Checked the dataset for missing values and handled them appropriately.

### Removing Duplicate Records

Duplicate records were removed to maintain dataset quality.

### Removing Irrelevant Features

Text-based columns such as street, city, statezip, and country were removed because they are not useful for numerical prediction models.

### Data Type Checking

Ensured that all features used for training were numeric.

### Feature Scaling

Standardization was applied using **StandardScaler** to normalize feature values.

### Train-Test Split

The dataset was divided into:

* **80% Training Data**
* **20% Testing Data**

---

## Algorithms Used

Three supervised machine learning algorithms were implemented:

### Linear Regression

A basic regression model used to understand the linear relationship between features and house price.

### Decision Tree Regressor

A tree-based algorithm that splits the data into different branches to make predictions.

### Random Forest Regressor

An ensemble learning method that builds multiple decision trees and combines their predictions for improved accuracy.

---

## Evaluation Metrics

The models were evaluated using the following regression metrics:

* **R² Score**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Error (MAE)**

These metrics help compare how accurately each model predicts house prices.

---

## Results and Observations

After training and evaluating the models:

* **Random Forest Regressor** achieved the best performance.
* **Decision Tree Regressor** performed reasonably well but may overfit.
* **Linear Regression** provided a simple baseline model.

---

## Libraries Used

The project was implemented using the following Python libraries:

* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn

---

## Conclusion

This project demonstrates how supervised machine learning algorithms can be applied to predict house prices. Proper data preprocessing, feature selection, and model evaluation are important for building accurate predictive models.

Among the models tested, **Random Forest Regressor produced the most accurate predictions**, making it the best-performing algorithm for this dataset.

---

## Author

Vishal Sharma
