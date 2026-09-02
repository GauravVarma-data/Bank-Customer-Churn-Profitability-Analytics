from pathlib import Path
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
df = pd.read_csv(BASE / "bank_customer_churn.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nMissing values:")
print(df.isna().sum())
print("\nDuplicate customer IDs:", df["CustomerId"].duplicated().sum())

print("\nExecutive KPIs")
print("Customers:", len(df))
print("Churn rate: {:.2%}".format(df["Exited"].mean()))
print("Balance at risk: {:,.2f}".format(df.loc[df["Exited"].eq(1),"Balance"].sum()))

print("\nChurn by geography")
print(df.groupby("Geography")["Exited"].mean().sort_values(ascending=False))

print("\nChurn by product count")
print(df.groupby("NumOfProducts")["Exited"].mean().sort_values(ascending=False))

print("\nRisk segments")
print(df.groupby("RiskSegment").agg(
    Customers=("CustomerId","nunique"),
    ChurnRate=("Exited","mean"),
    BalanceAtRisk=("BalanceAtRisk","sum")
).sort_values("BalanceAtRisk", ascending=False))
