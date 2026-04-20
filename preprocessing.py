# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("titanic.csv")

print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)

df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

df.drop(columns=['Cabin'], inplace=True)

df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})


df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])


print("\nBoxplot for Fare (Before removing outliers):")
sns.boxplot(x=df['Fare'])
plt.show()


Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1

df = df[(df['Fare'] >= Q1 - 1.5 * IQR) & (df['Fare'] <= Q3 + 1.5 * IQR)]

print("\nFinal Dataset:")
print(df.head())

print("\nFinal Shape (rows, columns):")
print(df.shape)

print("\nNo. of Missing Values after cleaning:")
print(df.isnull().sum())