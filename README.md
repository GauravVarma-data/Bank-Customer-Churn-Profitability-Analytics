🏦 Bank Customer Churn & Profitability Analytics

Python | SQL | Power BI | Excel | Streamlit | Customer Segmentation

📌 Project Overview

Customer retention is a major challenge for retail banks because losing customers can also mean losing significant account balances and future business value.

This project analyzes a **10,000-customer synthetic retail banking dataset** to identify customer churn patterns, evaluate customer value, quantify financial exposure, and prioritize customers for retention efforts.

The analysis combines **Python, SQL, Excel, Power BI, and Streamlit** to demonstrate an end-to-end Data Analytics workflow — from data quality and feature engineering to business insights and interactive reporting.

# 🎯 Business Problem

A retail bank is experiencing customer attrition and wants to understand:

* Which customer segments are most likely to churn?
* Does customer activity influence churn?
* How does the number of products relate to churn?
* Which geographic segments have higher churn?
* How much account balance is associated with churned customers?
* Which high-value customers should the retention team prioritize?

The objective is to transform customer-level data into **actionable retention and profitability insights**.

---

# 📊 Key Business Metrics

The project focuses on the following KPIs:

| KPI                      | Description                                      |
| ------------------------ | ------------------------------------------------ |
| **Total Customers**      | Total number of customers in the portfolio       |
| **Churned Customers**    | Number of customers who exited                   |
| **Churn Rate**           | Percentage of customers who churned              |
| **Total Balance**        | Total account balance across customers           |
| **Balance at Risk**      | Balance belonging to churned customers           |
| **Average Balance**      | Average customer account balance                 |
| **Average Credit Score** | Average customer credit score                    |
| **Customer Value**       | Composite measure used for customer segmentation |

---

# 🧠 Analytical Approach

The project follows a complete analytics lifecycle:

```text
Raw Customer Data
        ↓
Data Quality Assessment
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
SQL Business Analysis
        ↓
Customer Segmentation
        ↓
KPI Development
        ↓
Dashboard Development
        ↓
Business Recommendations
```

---

# 🗂️ Dataset

The dataset contains **10,000 synthetic customer records** with attributes covering:

### Customer Information

* Customer ID
* Geography
* Gender
* Age
* Tenure

### Financial Information

* Credit Score
* Account Balance
* Estimated Salary

### Banking Information

* Number of Products
* Credit Card Ownership
* Active Membership

### Outcome

* Churn / Exit Status

---

# 🛠️ Technologies Used

### Python

Used for:

* Data cleaning
* Data validation
* Exploratory Data Analysis
* Feature engineering
* Customer segmentation
* Statistical analysis
* Visualization

Libraries:

```text
Pandas
NumPy
Matplotlib
```

### SQL

Used for:

* KPI calculations
* Customer segmentation
* Conditional aggregation
* CTEs
* Window functions
* Ranking
* Business analysis

### Power BI

Used for:

* Interactive dashboards
* KPI cards
* Customer segmentation
* Risk analysis
* Geographic analysis
* Drill-down analysis

### Excel

Used for:

* Data validation
* PivotTables
* Cross-checking analytical results
* Formula-based analysis

### Streamlit

Used to create a lightweight interactive web dashboard for customer exploration.

---

# 🔍 Data Preparation

Before analysis, the dataset was evaluated for:

* Missing values
* Duplicate customer IDs
* Invalid credit scores
* Invalid ages
* Invalid tenure values
* Negative balances
* Invalid product counts
* Incorrect data types

Business validation rules were applied before creating analytical features.

---

# ⚙️ Feature Engineering

Several new analytical variables were created.

### Age Group

Customers were categorized into:

```text
<30
30–39
40–49
50–59
60+
```

### Balance Segment

Customers were divided into balance quartiles:

```text
Low
Medium
High
Very High
```

### Customer Value

A composite customer-value score was developed using:

* Account balance
* Estimated salary
* Number of products
* Credit score

Customers were then divided into value quartiles.

### Activity Status

```text
Active
Inactive
```

### Churn Status

```text
Retained
Churned
```

---

# 🚨 Customer Risk Segmentation

One of the key components of the project is customer risk segmentation.

Customers are classified into:

### 🔴 High Value – High Risk

High-value customers who have churned.

These represent the highest-priority group for retention analysis.

### 🟢 High Value – Low Risk

High-value customers who remain active.

These customers represent an important group for relationship management.

### 🟠 Low Value – High Risk

Lower-value customers who have churned.

### ⚪ Low Value – Low Risk

Customers with lower estimated value and lower churn exposure.

---

# 📈 Key Findings

Based on the included synthetic dataset:

### Overall Portfolio

* **10,000 customers** were analyzed.
* The overall churn rate is approximately **19.33%**.
* Approximately **137.29M** in account balance is associated with churned customers.

### Geographic Risk

**Germany** shows the highest churn rate among the three geographic segments in the generated dataset.

### Customer Value

The **High Value – High Risk** segment represents the most important segment from a financial-exposure perspective.

### Product Ownership

Customers with different numbers of products demonstrate materially different churn behavior, making product engagement an important dimension for retention analysis.

> **Important:** These findings apply only to the synthetic dataset included in this repository and should not be interpreted as real banking-industry statistics.

---

# 📊 Dashboard

The project includes an interactive Streamlit dashboard and a Power BI dashboard specification.

## Dashboard — Executive Overview

The dashboard provides:

* Total Customers
* Churned Customers
* Churn Rate
* Total Balance
* Balance at Risk
* Churn by Geography
* Churn by Product Count
* Customer Risk Segments

---

## Dashboard — Customer Risk

The analysis allows users to explore:

* Customer balance
* Credit score
* Age
* Geography
* Activity status
* Product ownership
* Churn status
* Customer risk segment

---

## Dashboard — Retention Prioritization

The retention view focuses on:

```text
Customer Segment
        ↓
Customer Count
        ↓
Churn Rate
        ↓
Balance at Risk
```

This allows a retention team to prioritize segments based on both **customer churn and financial exposure**.

---

# 💻 Project Structure

```text
Bank_Customer_Churn_Profitability_Analytics/
│
├── data/
│   └── bank_customer_churn.csv
│
├── python/
│   └── 01_analysis.py
│
├── sql/
│   └── 01_analysis.sql
│
├── dashboard/
│   ├── app.py
│   ├── POWER_BI_SPEC.md
│   ├── 01_churn_by_geography.png
│   ├── 02_balance_at_risk.png
│   ├── 03_churn_by_products.png
│   ├── 04_churn_by_age.png
│   └── 05_balance_vs_age.png
│
├── outputs/
│   ├── executive_kpis.csv
│   ├── churn_by_geography.csv
│   ├── churn_by_age_group.csv
│   ├── churn_by_products.csv
│   ├── churn_by_activity.csv
│   ├── risk_segments.csv
│   ├── top_50_high_value_churners.csv
│   ├── churn_correlations.csv
│   └── bank_analytics.sqlite
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ▶️ How to Run the Project

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/bank-customer-churn-profitability-analytics.git
```

Navigate into the project:

```bash
cd bank-customer-churn-profitability-analytics
```

---

## 2. Create a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Python Analysis

Run:

```bash
python python/01_analysis.py
```

The script performs:

```text
Data Loading
     ↓
Data Validation
     ↓
EDA
     ↓
Feature Engineering
     ↓
KPI Calculation
     ↓
Customer Segmentation
     ↓
Analysis Outputs
```

---

# 📊 Run the Dashboard

Start Streamlit:

```bash
streamlit run dashboard/app.py
```

The application will open in your browser.

---

# 🗄️ SQL Analysis

The project includes a SQLite database:

```text
outputs/bank_analytics.sqlite
```

The SQL analysis contains queries for:

* Executive KPIs
* Churn by geography
* Churn by product count
* Churn by activity
* Customer risk segmentation
* Top churned customers
* Geographic risk ranking

SQL techniques demonstrated include:

```text
SELECT
WHERE
GROUP BY
CASE
CTE
Aggregations
DENSE_RANK()
Window Functions
Conditional Aggregation
```

---

# 💼 Business Recommendations

Based on the analysis framework, a bank could:

### 1. Prioritize High-Value Churners

Customers with high balances and churn status should receive priority in retention programs.

### 2. Improve Engagement

Inactive customers should be evaluated for targeted engagement campaigns.

### 3. Investigate Product Relationships

Significant differences in churn across product counts can help the bank evaluate whether customers are appropriately served or potentially over/under-productized.

### 4. Develop Geographic Retention Strategies

Geographies with elevated churn should receive deeper customer-behavior analysis and targeted retention initiatives.

### 5. Monitor Balance Exposure

Retention teams should prioritize customers based on **both churn likelihood and financial exposure**, rather than customer count alone.

---

# ⚠️ Limitations

This project has several limitations:

* The dataset is synthetic.
* Churn relationships are observational and do not establish causality.
* "Balance at Risk" represents the balance associated with churned customers; it is **not a forecast of lost revenue**.
* The customer-value score is a portfolio analytical construct and not a bank-approved credit or profitability model.
* Additional variables would be required for production-level churn prediction.

---

# 🚀 Future Improvements

Potential extensions include:

* Logistic regression churn prediction
* Machine-learning-based churn probability
* Customer Lifetime Value (CLV)
* Retention campaign ROI analysis
* Time-series churn monitoring
* Automated Power BI refresh
* Advanced customer segmentation
* Model explainability using SHAP
* Deployment through a cloud platform

---

# 👨‍💻 Skills Demonstrated

This project demonstrates practical experience with:

```text
Python
Pandas
NumPy
Data Cleaning
Exploratory Data Analysis
Feature Engineering
SQL
CTEs
Window Functions
Customer Segmentation
KPI Development
Financial Analytics
Power BI
Dashboard Design
Excel
Business Analysis
Data Storytelling
```

---


