import streamlit as st
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "bank_customer_churn.csv")

st.set_page_config(page_title="Bank Churn Analytics", layout="wide")

# -----------------------------
# Independent Risk Score
# -----------------------------
df["RiskScore"] = (
    (df["IsActiveMember"] == 0).astype(int) * 2 +
    (df["Age"] >= 50).astype(int) +
    (df["Balance"] > df["Balance"].median()).astype(int) +
    (df["CreditScore"] < 600).astype(int) +
    (df["Tenure"] <= 2).astype(int) +
    ((df["NumOfProducts"] == 1) | (df["NumOfProducts"] >= 3)).astype(int)
)

df["RiskSegment"] = pd.cut(
    df["RiskScore"],
    bins=[-1, 2, 4, 10],
    labels=["Low Risk", "Medium Risk", "High Risk"]
)

df["BalanceAtRisk"] = df["Balance"].where(
    df["RiskSegment"].eq("High Risk"), 0
)

# -----------------------------
# Dashboard
# -----------------------------
st.title("Bank Customer Churn & Profitability Analytics")
st.caption(
    "Portfolio project | Synthetic banking dataset | "
    "Risk score based on customer characteristics"
)

total = len(df)
churned = int(df["Exited"].sum())
churn = df["Exited"].mean()
risk_balance = df.loc[
    df["RiskSegment"].eq("High Risk"), "Balance"
].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", f"{total:,}")
c2.metric("Churned", f"{churned:,}")
c3.metric("Churn Rate", f"{churn:.1%}")
c4.metric("High-Risk Balance", f"{risk_balance:,.0f}")

# -----------------------------
# Churn by Geography
# -----------------------------
st.subheader("Churn by Geography")

geo = df.groupby("Geography", as_index=False).agg(
    Customers=("CustomerId", "nunique"),
    ChurnRate=("Exited", "mean"),
    BalanceAtRisk=("BalanceAtRisk", "sum")
)

st.bar_chart(
    geo.set_index("Geography")["ChurnRate"]
)

st.dataframe(
    geo,
    use_container_width=True
)

# -----------------------------
# Risk Segments
# -----------------------------
st.subheader("Risk Segments")

seg = df.groupby(
    "RiskSegment",
    observed=False,
    as_index=False
).agg(
    Customers=("CustomerId", "nunique"),
    ChurnRate=("Exited", "mean"),
    BalanceAtRisk=("BalanceAtRisk", "sum")
)

st.dataframe(
    seg,
    use_container_width=True
)

# -----------------------------
# Customer Explorer
# -----------------------------
st.subheader("Customer Explorer")

country = st.selectbox(
    "Geography",
    ["All"] + sorted(df["Geography"].unique().tolist())
)

status = st.selectbox(
    "Churn Status",
    ["All", "Retained", "Churned"]
)

risk_filter = st.selectbox(
    "Risk Segment",
    ["All", "Low Risk", "Medium Risk", "High Risk"]
)

view = df.copy()

if country != "All":
    view = view[view["Geography"] == country]

if status != "All":
    view = view[view["ChurnStatus"] == status]

if risk_filter != "All":
    view = view[view["RiskSegment"] == risk_filter]

st.dataframe(
    view[
        [
            "CustomerId",
            "Geography",
            "Gender",
            "Age",
            "CreditScore",
            "Balance",
            "NumOfProducts",
            "IsActiveMember",
            "ChurnStatus",
            "RiskSegment",
            "RiskScore",
            "BalanceAtRisk"
        ]
    ]
    .sort_values("Balance", ascending=False)
    .head(100),
    use_container_width=True
)
