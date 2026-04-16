import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:/Users/Sonal deep Gupta/Desktop/customer engagement.csv")

st.subheader("📊 Engagement vs Churn Overview")

# Calculate churn rate
engagement_churn = data.groupby("IsActiveMember")["Exited"].mean().reset_index()

engagement_churn["IsActiveMember"] = engagement_churn["IsActiveMember"].map({
    0: "Inactive",
    1: "Active"
})

# Plot
fig, ax = plt.subplots()
sns.barplot(data=engagement_churn, x="IsActiveMember", y="Exited", ax=ax)

ax.set_title("Churn Rate by Engagement")
ax.set_xlabel("Customer Status")
ax.set_ylabel("Churn Rate")

st.pyplot(fig)

# Show values
st.dataframe(engagement_churn)

  # Product Utilization Impact
       
st.header("Product Utilization Impact Analysis")

usage_bins = pd.cut(data['NumOfProducts'], bins=5)
churn_by_usage = data.groupby(usage_bins)['HasCrCard'].mean()

fig2, ax2 = plt.subplots()
churn_by_usage.plot(kind='bar', ax=ax2)
ax2.set_title("Churn vs NumOfProducts")
st.pyplot(fig2)

#  High-Value Disengaged Customers
  
st.header(" High-Value Disengaged Customers")

high_value = data[
(data['Balance'] > data['Balance'].quantile(0.75)) &
(data['IsActiveMember'] < data['IsActiveMember'].quantile(0.25))
]

st.write(f"Total High-Risk Customers: {len(high_value)}")
st.dataframe(high_value)

# --- Module 4: Retention Strength Scoring ---
st.header(" Retention Strength Scoring Panels")

# Simple scoring formula
data['retention_score'] = (
    0.4 * data['IsActiveMember'] +
    0.3 * data['Exited'] +
    0.3 * (100 - data['HasCrCard'] * 100)
)

fig3, ax3 = plt.subplots()
ax3.hist(data['retention_score'], bins=20)
ax3.set_xlabel("Retention Score")
ax3.set_ylabel("Exited")
st.pyplot(fig3)

st.write("Customer Retention Scores:")
st.dataframe(data[['retention_score']].head())

# Engagement Filter
engagement_range = st.sidebar.slider(
    "Engagement Score",
    min_value=0,
    max_value=100,
    value=(20, 80)
)

# Product Count Slider
product_range = st.sidebar.slider(
    "Number of Products",
    min_value=int(data["HasCrCard"].min()),
    max_value=int(data["HasCrCard"].max()),
    value=(1, 5)
)

# Balance Threshold
balance_threshold = st.sidebar.slider(
    "Minimum Account Balance",
    min_value=int(data["IsActiveMember"].min()),
    max_value=int(data["IsActiveMember"].max()),
    value=20000
)


# -----------------------------
# Apply Filters
# -----------------------------
filtered_data = data[
    (data["IsActiveMember"].between(*engagement_range)) &
    (data["HasCrCard"].between(*product_range)) &
    (data["IsActiveMember"] >= balance_threshold)
]

# -----------------------------
# Main Dashboard
# -----------------------------
st.title(" Customer Engagement Dashboard")

st.subheader("Filtered Customer Data")
st.dataframe(filtered_data)

# -----------------------------
# Metrics
# -----------------------------
st.subheader(" Key Insights")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(filtered_data))
col2.metric("Avg Engagement", round(filtered_data["IsActiveMember"].mean(), 2))
col3.metric("Avg Balance", round(filtered_data["IsActiveMember"].mean(), 2))

# -----------------------------
# Visualization
# -----------------------------
st.subheader("📊 Engagement vs Product Count")

st.scatter_chart(
    filtered_data[["IsActiveMember", "HasCrCard"]]
)
