# Power BI Dashboard Specification

Import:
- bank_customer_churn.csv
- churn_by_geography.csv
- churn_by_age_group.csv
- churn_by_products.csv
- risk_segments.csv

## KPI cards
Total Customers = DISTINCTCOUNT(CustomerId)
Churned Customers = CALCULATE([Total Customers], Exited = 1)
Churn Rate = DIVIDE([Churned Customers], [Total Customers])
Total Balance = SUM(Balance)
Balance at Risk = CALCULATE([Total Balance], Exited = 1)

## Page 1 — Executive Overview
Cards + churn by geography + churn by age group + churn by products.

## Page 2 — Risk & Retention
RiskSegment table with Customers, ChurnRate, BalanceAtRisk.
Scatter: Balance vs CreditScore, legend ChurnStatus.
Slicers: Geography, Gender, AgeGroup, ActivityStatus.

## Page 3 — Customer Explorer
Table of CustomerId, Geography, Age, CreditScore, Balance, NumOfProducts,
IsActiveMember, ChurnStatus, RiskSegment.

Use the Streamlit dashboard as the immediately runnable dashboard; Power BI is an optional
presentation layer.
