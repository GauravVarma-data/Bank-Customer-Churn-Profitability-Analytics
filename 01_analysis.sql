-- Bank Customer Churn & Profitability Analytics
-- SQLite-compatible SQL. The same logic can be adapted to PostgreSQL/MySQL.

-- 01. Executive KPIs
SELECT
    COUNT(*) AS total_customers,
    SUM(Exited) AS churned_customers,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(Balance), 2) AS total_balance,
    ROUND(SUM(CASE WHEN Exited = 1 THEN Balance ELSE 0 END), 2) AS balance_at_risk
FROM customers;

-- 02. Churn by geography
SELECT
    Geography,
    COUNT(*) AS customers,
    SUM(Exited) AS churned,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(CASE WHEN Exited=1 THEN Balance ELSE 0 END),2) AS balance_at_risk
FROM customers
GROUP BY Geography
ORDER BY churn_rate_pct DESC;

-- 03. Churn by product count
SELECT
    NumOfProducts,
    COUNT(*) AS customers,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct,
    ROUND(AVG(Balance), 2) AS avg_balance
FROM customers
GROUP BY NumOfProducts
ORDER BY NumOfProducts;

-- 04. Churn by activity
SELECT
    ActivityStatus,
    COUNT(*) AS customers,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(BalanceAtRisk), 2) AS balance_at_risk
FROM customers
GROUP BY ActivityStatus
ORDER BY churn_rate_pct DESC;

-- 05. High-value/high-risk prioritization
SELECT
    RiskSegment,
    COUNT(*) AS customers,
    ROUND(AVG(Exited) * 100, 2) AS churn_rate_pct,
    ROUND(SUM(BalanceAtRisk), 2) AS balance_at_risk
FROM customers
GROUP BY RiskSegment
ORDER BY balance_at_risk DESC;

-- 06. Top 20 churned customers by balance
SELECT
    CustomerId, Geography, Age, CreditScore, Balance,
    NumOfProducts, IsActiveMember, Exited
FROM customers
WHERE Exited = 1
ORDER BY Balance DESC
LIMIT 20;

-- 07. Rank geographies by balance at risk
WITH geography_risk AS (
    SELECT Geography,
           SUM(CASE WHEN Exited=1 THEN Balance ELSE 0 END) AS balance_at_risk
    FROM customers
    GROUP BY Geography
)
SELECT *,
       DENSE_RANK() OVER (ORDER BY balance_at_risk DESC) AS risk_rank
FROM geography_risk;

-- 08. Active vs inactive customers
SELECT
    IsActiveMember,
    COUNT(*) AS customers,
    ROUND(AVG(Exited)*100,2) AS churn_rate_pct,
    ROUND(AVG(Balance),2) AS avg_balance
FROM customers
GROUP BY IsActiveMember;
