## Day 1 — Bitcoin Data Cleaning

- Converted timestamp to datetime
- Handled missing values using forward fill
- Sorted data by time
- Set timestamp as index

Dataset: Bitcoin Historical Data
Output: cleaned_btc_data.csv

## Day 2 — EDA

Performed exploratory data analysis on Bitcoin dataset:
- Visualized price trends
- Analyzed volatility (returns)
- Applied moving averages (MA7, MA30)

Key Insight:
Bitcoin is highly volatile but shows long-term growth patterns.

## Day 3 — Data Visualization

In this stage, I created visual representations of Bitcoin price data to better understand trends and patterns.

### Visualizations
- Price trend over time
- Moving averages (7-day & 30-day)
- Volatility (returns)
- Price distribution
- Log-scale price growth

### Insights
- Bitcoin shows exponential growth over time
- High volatility indicates market instability
- Moving averages help identify trend direction

### Tools
- Matplotlib
- Pandas

## Day 4 — Feature Engineering

In this stage, I transformed raw Bitcoin data into meaningful features for machine learning.

### Features Created
- Returns (price change)
- Moving averages (MA7, MA30)
- Lag features (previous prices)
- Volatility (rolling standard deviation)

### Purpose
To prepare structured data for predictive modeling.

### Tools
- Pandas

## Day 5 — Machine Learning Modeling

In this stage, I built a machine learning model to predict Bitcoin prices.

### Model
- Linear Regression

### Features Used
- Lag features (previous prices)
- Moving averages (MA7, MA30)
- Volatility

### Objective
Predict Bitcoin closing price based on historical patterns.

### Result
The model shows a reasonable ability to follow price trends.

### Tools
- Scikit-learn
- Pandas

## Day 6 — Model Evaluation

In this stage, I evaluated the performance of the machine learning model.

### Metrics Used
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R2 Score

### Results
The model shows reasonable performance but still has prediction errors due to high market volatility.

### Insight
Bitcoin is highly unpredictable, making accurate prediction challenging.

### Tools
- Scikit-learn
- NumPy
