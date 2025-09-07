# Predicting Mood from Smartphone Data
# Project Summary
This project was a collaborative effort to explore the use of smartphone-derived behavioral data and self-reported information to predict a user's next-day mood. It was part of the Data Mining Techniques course at the Vrije Universiteit, Amsterdam. 
Following the CRISP-DM process model, we conducted a comprehensive analysis of the "dataset_mood_smartphone.csv" dataset, which contained a variety of behavioral data points like screen usage and physical activity, along with self-reported mood ratings. 
Our objective was to develop a successful predictive model that could offer valuable, personalized insights.
A comprehensive report detailing the methodology, results, and discussion can be found in the repository in the ["Report"](Report) folder.

# Research Question
The core research question of this project was to determine if next-day mood could be predicted from a combination of behavioral and self-reported smartphone data, and to identify the most influential factors in this prediction.

# Data
The "dataset_mood_smartphone.csv" dataset was used, consisting of 376,912 records from 27 unique users. The data included both behavioral metrics (such as screen usage, physical activity, and app usage) and self-reported mood ratings.

# Methodology
1. Data Preparation
   - Exploratory Data Analysis (EDA): We performed an initial analysis to understand the dataset's structure, identify patterns, and check for data quality issues.
   - Data Cleaning & Imputation: Missing values were handled using forward-fill and backward-fill methods to ensure a complete time series for each user.
   - Feature Engineering: We created several new features, including various time-based features to capture daily and weekly patterns as well as a Circumplex Quadrant attribute created by combing valence and arousal.

2. Modeling
   - We experimented with a range of machine learning techniques for both classification (predicting a categorical mood) and regression (predicting a numerical mood score).
   - Models included Gradient Boosting, Random Forest, and other classifiers and regressors.
   - The models were evaluated using standard metrics such as Mean Absolute Error (MAE) and Mean Squared Error (MSE) for regression, and accuracy and F1-score for classification.

# Key Findings and Conclusions
Our analysis showed that behavioral data from smartphones, such as screen usage and activity levels, can be used to predict next-day mood with a reasonable degree of accuracy. We found that Gradient Boosting achieved the lowest MAE and MSE scores, indicating it was the most successful model in our study. 
Interestingly, we also observed that the MAE was numerically higher than the MSE, which we attributed to the nature of the errors being mostly less than one. This project demonstrates the potential of smartphone data in the realm of mental health and personalized well-being, although limitations such as a small user base mean the results are not yet generalizable.

# Authors
Urban Sirca

Matus Halak

Kieran Keesmaat
