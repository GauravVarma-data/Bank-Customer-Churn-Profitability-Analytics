import streamlit as st
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "bank_customer_churn.csv")

st.set_page_config(page_title="Bank Churn Analytics", layout="wide")
st.title("Bank Customer Churn & Profitability Analytics")
st.caption("Portfolio project | Synthetic banking dataset generated with a fixed seed for reproducibility")

total = len(df)
churned = int(df["Exited"].sum())
churn = df["Exited"].mean()
risk = df.loc[df["Exited"].eq(1), "Balance"].sum()

c1,c2,c3,c4 = st.columns(4)
c1.metric("Customers", f"{total:,}")
c2.metric("Churned", f"{churned:,}")
c3.metric("Churn Rate", f"{churn:.1%}")
c4.metric("Balance at Risk", f"{risk:,.0f}")

st.subheader("Churn by Geography")
geo = df.groupby("Geography", as_index=False).agg(
    Customers=("CustomerId","nunique"),
    ChurnRate=("Exited","mean"),
    BalanceAtRisk=("BalanceAtRisk","sum")
)
st.bar_chart(geo.set_index("Geography")["ChurnRate"])

st.subheader("Balance at Risk by Segment")
seg = df.groupby("RiskSegment", as_index=False).agg(
    Customers=("CustomerId","nunique"),
    ChurnRate=("Exited","mean"),
    BalanceAtRisk=("BalanceAtRisk","sum")
).sort_values("BalanceAtRisk", ascending=False)
st.dataframe(seg, use_container_width=True)

st.subheader("Customer Explorer")
country = st.selectbox("Geography", ["All"] + sorted(df["Geography"].unique().tolist()))
status = st.selectbox("Churn status", ["All","Retained","Churned"])
view = df.copy()
if country != "All":
    view = view[view["Geography"] == country]
if status != "All":
    view = view[view["ChurnStatus"] == status]
st.dataframe(
    view[["CustomerId","Geography","Gender","Age","CreditScore",
          "Balance","NumOfProducts","IsActiveMember","ChurnStatus","RiskSegment"]]
    .sort_values("Balance", ascending=False).head(100),
    use_container_width=True
)
