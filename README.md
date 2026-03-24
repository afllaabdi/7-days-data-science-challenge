## Day 1 — Bitcoin Data Cleaning

- Converted timestamp to datetime
- Handled missing values using forward fill
- Sorted data by time
- Set timestamp as index

Dataset: Bitcoin Historical Data
Output: cleaned_btc_data.csv
## Day 2 — Exploratory Data Analysis (EDA)

In this stage, I explored the Bitcoin dataset to understand price behavior, trends, and volatility over time.

### Objectives
- Analyze Bitcoin price trends
- Identify patterns in time series data
- Measure volatility and market movement
- Apply basic financial analysis techniques

---

### Steps Performed

1. **Load Cleaned Data**
   - Imported cleaned dataset from Day 1

2. **Time Series Preparation**
   - Converted timestamp to datetime
   - Set timestamp as index

3. **Price Visualization**
   - Plotted Bitcoin price over time
   - Observed long-term trends (bullish/bearish phases)

4. **Resampling Data**
   - Converted minute-level data into daily averages
   - Improved readability of trends

5. **Statistical Summary**
   - Analyzed mean, max, min, and distribution of prices

6. **Volatility Analysis**
   - Calculated daily returns using percentage change
   - Observed how unstable the market can be

7. **Moving Average Analysis**
   - Applied 7-day and 30-day moving averages
   - Identified trend direction and potential signals

---

### Key Insights

- Btcoin shows **high volatility**, making it a high-risk asset
- There is a **long-term upward trend** despite short-term fluctuations
- Moving averages help identify **trend direction**
- Daily aggregation makes patterns easier to interpret

---

### Tools & Libraries
- Python
- Pandas
- Matplotlib

---

### Output
- Time series plots of Bitcoin price
- Volatility graph (returns)
- Moving average visualization

