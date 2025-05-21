# --Libraries--

# -For data manipulation and DataFrame support
import pandas as pd

# -For numerical operations and handling NaN values
import numpy as np

# -For static visualizations (histograms, scatter plots,...)
import matplotlib.pyplot as plt

# -For advanced visualizations like boxplots and heatmaps
import seaborn as sns

# -To manage and suppress unwanted warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# -Sklearn tool for encoding categorical variables into numeric labels
from sklearn.preprocessing import LabelEncoder

# --Load dataset--

# -Load the CSV file into a pandas DataFrame
dataset = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
dataset

# --Initial structural and statistical overview--

dataset.info()
dataset.describe()
dataset.head()

# --For quick reference--

dataset_types = dataset.dtypes
dataset_types

dataset_missing = dataset.isnull().sum()
dataset_missing

dataset_unique = dataset.nunique()
dataset_unique

dataset_shape = dataset.shape
dataset_shape

dataset_summary = {
    'Data Types': dataset_types,
    'Missing Values': dataset_missing,
    'Uniques Values': dataset_unique,
    'shape': dataset_shape
}
dataset_summary

# --Data Cleaning & Feature Engineering--

dataset.isnull().sum()
dataset['Sleep Disorder'].isnull().sum()
# -Replace string "None" with np.nan
dataset['Sleep Disorder'] = dataset['Sleep Disorder'].replace('None', np.nan)
# -Split 'Blood Pressure' into two numerical columns (Systolic and Diastolic)
dataset['Blood Pressure'].head(20)
dataset[['Systolic BP', 'Diastolic BP']] = dataset['Blood Pressure'].str.split(
    '/', expand=True).astype(int)
# -Drop the 'Blood Pressure' column after decomposition
dataset.drop(columns=['Blood Pressure'], inplace=True)

# -One-hot encode categorical with drop_first=True
dataset_encoded = pd.get_dummies(
    dataset, columns=['Gender', 'BMI Category', 'Sleep Disorder'], drop_first=True)
dataset_encoded.isnull().sum()
dataset_encoded

# -Encode 'Occupation' using LabelEncoder (ordinal values assigned alphabetically)
le = LabelEncoder()
le.fit(dataset['Occupation'])

# -Create a dictionary to document the mapping of occupation names to numeric codes
occupation_mapping = {occupation: code for code,
                      occupation in enumerate(le.classes_)}
occupation_mapping

# -Apply encoded values to dataset_encoded
dataset_encoded['Occupation'] = le.fit_transform(dataset['Occupation'])

# -Final Check for Missing Values
dataset_encoded.isnull().mean().sort_values(ascending=False)
dataset_encoded.head()

# --Univariate Distribution Analysis (Histograms)--

# -Set default plot size for all visualizations
plt.rcParams["figure.figsize"] = (10, 6)

# -Define list of numerical columns to analyze
numerical_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                  'Stress Level', 'Heart Rate', 'Daily Steps', 'Systolic BP', 'Diastolic BP']

# -Loop for each numerical feature and plot histogram
for col in numerical_cols:
    plt.figure()
    plt.hist(dataset_encoded[col], bins=20, edgecolor='black')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # --Bivariate Analysis: Boxplots between Key Variables--


dataset_encoded['Stress Group'] = pd.cut(dataset_encoded['Stress Level'], bins=[
                                         0, 3, 6, 10], labels=['Low', 'Medium', 'High'])
dataset_encoded['Stress Group']

# -Boxplot 1: Physical Activity Level in relation to Stress Level
plt.figure(figsize=(10, 6))
sns.boxplot(x='Stress Level', y='Physical Activity Level',
            data=dataset_encoded)
plt.title("Physical Activity Level vs Stress Level")
plt.grid(True)
plt.tight_layout()
plt.show()

# -Boxplot 2: Sleep Duration across different Stress Levels
plt.figure(figsize=(10, 6))
sns.boxplot(x='Stress Level', y='Sleep Duration', data=dataset_encoded)
plt.title("Sleep Duration vs Stress Level")
plt.grid(True)
plt.tight_layout()
plt.show()

# -Boxplot 3: Sleep Duration across different values of Quality of Sleep
plt.figure(figsize=(10, 6))
sns.boxplot(x='Quality of Sleep', y='Sleep Duration', data=dataset_encoded)
plt.title("Sleep Duration vs Quality of Sleep")
plt.grid(True)
plt.tight_layout()
plt.show()

# -Boxplot 4: Sleep Duration across different levels of Physical Activity
plt.figure(figsize=(10, 6))
sns.boxplot(x='Physical Activity Level',
            y='Sleep Duration', data=dataset_encoded)
plt.title("Sleep Duration vs Physical Activity Level")
plt.grid(True)
plt.tight_layout()
plt.show()

# --Bivariate Scatter Plots & Correlation Heatmap--

# -Scatter Plot 1: Sleep Duration vs Daily Steps
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Daily Steps', y='Sleep Duration', data=dataset_encoded)
plt.title("Sleep Duration vs Daily Steps")
plt.grid(True)
plt.tight_layout()
plt.show()

# -Scatter Plot 2: Stress Level vs Heart Rate
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Stress Level', y='Heart Rate', data=dataset_encoded)
plt.title("Stress Level vs Heart Rate")
plt.grid(True)
plt.tight_layout()
plt.show()

# -Correlation Heatmap (Target: Sleep Duration)
plt.figure(figsize=(12, 8))
corr = dataset_encoded.corr(numeric_only=True)
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
