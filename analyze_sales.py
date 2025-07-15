import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Thanuja/OneDrive/Desktop/sales.csv", parse_dates=["Date"])

df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum()


monthly_sales.plot(kind="bar", title="Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
