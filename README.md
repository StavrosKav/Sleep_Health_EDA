# Sleep_health_EDA
Sleep Health and Lifestyle | Exploratory Data Analysis

This project performs an end-to-end Exploratory Data Analysis (EDA) on a health dataset that includes biometric, lifestyle, and sleep-related data. The aim is to uncover patterns between stress, activity level, and sleep behaviors.

# A simple Dataset Overview

From            : https://www.kaggle.com/datasets/orvile/health-and-sleep-relation-2024

Source dataset  : 'Sleep_health_and_lifestyle_dataset.csv'

Entries         :  374 

Variables       : 'Gender,Age,Occupation,Sleep Duration,Quality of Sleep,Stress Level,BMI Category,Blood Pressure,Heart Rate,Daily Steps,Sleep Disorder'

# Preprocessing Steps 

## 1| Missing Values Handling

-Checked missing values using .isnull().sum()

-Treated "None" in the 'Sleep Disorder' column as a missing value by replacing it with np.nan.

## 2| Feature Engineering

-Split compound feature 'Blood Pressure' like '120/80' into two new numeric features: 'Systolic BP'='120' and 'Diastolic BP'='80'

## 3| Categorical Encoding

-One-Hot Encoded the following columns with drop_first=True : Gender | BMI Category | Sleep Disorder

## 4| Final Cleanup

Verified that all missing values have been handled

# Exploratory Data Analysis (EDA)

## Univariate Analysis

Histograms for: Age,Sleep Duration,Quality of Sleep,Physical Activity Level,Stress Level,Heart Rate,Daily Steps,Systolic BP,Diastolic BP

## Bivariate Analysis

--Boxplots:

/Physical Activity Level vs Stress Level

/Sleep Duration vs Stress Level

/Sleep Duration vs Quality of Sleep

/Sleep Duration vs Physical Activity Level

--Scatter Plots:

/Sleep Duration vs Daily Steps

/Stress Level vs Heart Rate

--Correlation Heatmap:

/Focused on relationships with Sleep Duration.

# Insights from EDA

## From Histograms :

Age                     | Most individuals are between 25 and 45 years old

Sleep Duration          | The majority sleep around 6–8 hours

Quality of Sleep        | Sleep quality mostly around values 6 to 8

Physical Activity Level | Many participants have low to moderate activity levels.

Stress Level            | Stress levels are fairly distributed, with a slight concentration around mid-level stress (4–6)

Heart Rate              | Most heart rates are between 60 and 80 bpm, consistent with a healthy resting heart rate range

Daily Steps             | Many individuals walk fewer than 8,000 steps daily, suggesting a sedentary to moderately active lifestyle

Systolic BP             | Systolic blood pressure commonly ranges between 110 and 130, aligning slightly with normal blood pressure values

Diastolic BP            | Diastolic readings mostly lie between 70 and 90, indicating controlled or normal diastolic pressure

## From Boxplots :

Physical Activity Level vs Stress Level   | Individuals with higher stress levels tend to have lower physical activity

Sleep Duration vs Stress Level            | Higher stress levels are associated with shorter sleep duration

Sleep Duration vs Quality of Sleep        | Better sleep quality corresponds to longer sleep duration

Sleep Duration vs Physical Activity Level | Moderate physical activity is linked to longer sleep duration

## Scatter Plots :

Sleep Duration vs Daily Steps | People who take more steps per day tend to sleep a bit longer

Stress Level vs Heart Rate    | Higher stress levels are often accompanied by higher heart rates

## Correlation Heatmap :

--Focused on relationships with Sleep Duration--

Sleep Duration shows:

Strongest correlation | Quality of Sleep 

Moderate correlation  | Daily Steps and Physical Activity Level ,more active individuals tend to sleep slightly more

Negative correlation  | Stress Level wich means higher stress is linked to shorter sleep duration

# Conclusion from Insights

The findings emphasize the importance of maintaining an active lifestyle and managing stress to improve both sleep duration and quality.


