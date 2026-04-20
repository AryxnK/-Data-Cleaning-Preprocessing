# 🧹 Data Cleaning & Preprocessing – Titanic Dataset

## 📌 Overview

This project focuses on cleaning and preparing raw data for machine learning.
The Titanic dataset is used to demonstrate essential preprocessing steps such as handling missing values, encoding categorical variables, feature scaling, and outlier removal.

---

## 🎯 Objective

To transform raw, unstructured data into a clean and usable format suitable for machine learning models.

---

## 🛠️ Tools & Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## 📂 Dataset

* Dataset Used: Titanic Dataset
* Contains passenger details such as Age, Sex, Fare, Cabin, Embarked, etc.

---

## 🔄 Steps Performed

### 1. Data Exploration

* Loaded dataset using Pandas
* Checked data types and structure
* Identified missing values

---

### 2. Handling Missing Values

* Filled missing **Age** values using median
* Filled missing **Embarked** values using mode
* Dropped **Cabin** column due to excessive missing data

---

### 3. Encoding Categorical Data

* Converted **Sex** column into numerical values (male = 0, female = 1)
* Applied one-hot encoding to **Embarked** column

---

### 4. Feature Scaling

* Standardized **Age** and **Fare** using StandardScaler
* Ensured all features are on a similar scale

---

### 5. Outlier Detection & Removal

* Used boxplot visualization to identify outliers
* Applied IQR (Interquartile Range) method to remove extreme values

---

## 📊 Results

* Successfully removed missing values
* Converted categorical data into numerical format
* Scaled features for better model performance
* Removed outliers to improve data quality

---

## 📈 Output

* Cleaned dataset ready for machine learning
* Reduced dataset size after removing outliers
* No missing values remaining

---

## 🧠 Key Learnings

* Importance of data preprocessing in ML
* Handling missing values effectively
* Difference between encoding techniques
* Role of feature scaling
* Detecting and removing outliers using IQR

---

## 🚀 Future Improvements

* Apply machine learning models on cleaned data
* Perform feature selection
* Try different scaling techniques
* Build a predictive model (e.g., survival prediction)

---

## 👨‍💻 Author

Aryan Kathuria
AI/ML Intern – Elevate Labs
