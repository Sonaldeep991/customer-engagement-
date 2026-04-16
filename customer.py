# import libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# load dataset
data=pd.read_csv(r"C:/Users/Sonal deep Gupta/Desktop/customer engagement.csv")
# Drop unnecessary column---------

data = data.drop(columns=["Surname"])
# DATA VALIDATION
# Check missing values------

print(data.isnull().sum())

# Ensure binary columns are correct----------

data['HasCrCard'] = data['HasCrCard'].astype(int)
data['IsActiveMember'] = data['IsActiveMember'].astype(int)
data['Exited'] = data['Exited'].astype(int)

# Engagement Score (basic)----------

data['EngagementScore'] = (
    data['IsActiveMember'] +
    data['NumOfProducts'] +
    data['HasCrCard']
)
# Engagement Category-------

def classify_customer(row):
    if row['IsActiveMember'] == 1 and row['NumOfProducts'] >= 2:
        return 'Active Engaged'
    elif row['IsActiveMember'] == 0 and row['NumOfProducts'] <= 1:
        return 'Inactive Disengaged'
    elif row['IsActiveMember'] == 1 and row['NumOfProducts'] <= 1:
        return 'Active Low Product'
    elif row['IsActiveMember'] == 0 and row['Balance'] > 100000:
        return 'Inactive High Balance'
    else:
        return 'Other'
data['EngagementSegment'] = data.apply(classify_customer, axis=1)

# Churn rate by number of products--------

churn_by_products = data.groupby('NumOfProducts')['Exited'].mean()
data['Product_Category'] = data['NumOfProducts'].apply(
    lambda x: 'Single Product' if x == 1 else 'Multi Product'
)
churn_trend = data.groupby('NumOfProducts')['Exited'].mean()
retention_rate = 1 - churn_by_products
print("Retention Rate:")
print(retention_rate)
print("Churn Rate by Number of Products:")
print(churn_by_products)
print("Product Depth vs Churn Rate:")
print(churn_trend)

# Plot
churn_by_products.plot(kind='bar')
plt.title("Churn Rate by Number of Products")
plt.xlabel("Number of Products")
plt.ylabel("Churn Rate")
plt.show()
retention_rate.plot(kind='bar')
plt.title("Single vs Multi Product Retention")
plt.xlabel("Customer Category")
plt.ylabel("Retention Rate")
plt.show()
churn_trend.plot(marker='o')
plt.title("Product Depth vs Churn Relationship")
plt.xlabel("Number of Products")
plt.ylabel("Churn Rate")
plt.show()

# Create activity category
data['Activity_Level'] = data['IsActiveMember'].map({1: 'Active', 0: 'Inactive'})
# Create balance category
data['Balance_Category'] = pd.cut(
    data['Balance'],
    bins=[-1, 0, 50000, 100000, 200000],
    labels=['Zero', 'Low', 'Medium', 'High']
)
# Cross-analysis table
cross_analysis = pd.crosstab(
    data['Balance_Category'],
    data['Activity_Level']
)

print("Balance vs Activity Cross Analysis:")
print(cross_analysis)

#Salary–balance mismatch detection.
def mismatch_type(row):
    if row['EstimatedSalary'] > 100000 and row['Balance'] < 10000:
        return 'High Salary - Low Balance'
    elif row['EstimatedSalary'] < 30000 and row['Balance'] > 150000:
        return 'Low Salary - High Balance'
    else:
        return 'Normal'

data['Mismatch_Type'] = data.apply(mismatch_type, axis=1)

print(data['Mismatch_Type'].value_counts())

 #Identification of “at-risk premium customers"
premium_threshold_balance = data['Balance'].quantile(0.75)
premium_threshold_salary = data['EstimatedSalary'].quantile(0.75)

data['Premium'] = (
    (data['Balance'] >= premium_threshold_balance) &
    (data['EstimatedSalary'] >= premium_threshold_salary)
)
data['At_Risk'] = (
    (data['IsActiveMember'] == 0) |   # inactive
    (data['NumOfProducts'] <= 1) |    # low product usage
    (data['Exited'] == 1)             # churned
)
data['At_Risk_Premium'] = (
    (data['Premium'] == True) &
    (data['At_Risk'] == True)
)
premium_churn_rate = data[data['Premium']]['Exited'].mean()
print("Premium Customer Churn Rate:", premium_churn_rate)
at_risk_premium_count = data['At_Risk_Premium'].sum()
print("At-Risk Premium Customers:", at_risk_premium_count)

# View them
at_risk_premium_df = data[data['At_Risk_Premium']]
cross_analysis.plot(kind='bar')
plt.title("Balance vs Activity")
plt.xlabel("Balance Category")
plt.ylabel("Customer Count")
plt.show()

#Retention Strength Assessment
data['Engagement_Score'] = (
    data['IsActiveMember'] * 0.5 +
    (data['NumOfProducts'] / data['NumOfProducts'].max()) * 0.5
)
data['Customer_Type'] = data.apply(
    lambda x: 'Sticky' if (x['Engagement_Score'] > 0.6 and x['Exited'] == 0) else 'Non-Sticky',
    axis=1
)
sticky_summary = data['Customer_Type'].value_counts(normalize=True)
print(sticky_summary)
data['Engagement_Tier'] = pd.cut(data['Engagement_Score'], bins=4, labels=['Low', 'Medium', 'High', 'Very High'])

# Churn rate per tier
churn_by_tier = data.groupby('Engagement_Tier')['Exited'].mean().reset_index()

print(churn_by_tier)
sns.barplot(x='Engagement_Tier', y='Exited', data=churn_by_tier)
plt.title('Churn Rate Across Engagement Tiers')
plt.ylabel('Churn Rate')
plt.show()
# Sort by engagement score
threshold_analysis = data.sort_values('Engagement_Score')

# Create bins for smoother trend
threshold_analysis['Score_Bin'] = pd.cut(
    threshold_analysis['Engagement_Score'], bins=10
)

# Calculate churn rate per bin
threshold_churn = threshold_analysis.groupby('Score_Bin')['Exited'].mean().reset_index()

print(threshold_churn)
plt.figure()
plt.plot(threshold_churn['Score_Bin'].astype(str), threshold_churn['Exited'], marker='o')
plt.xticks(rotation=45)
plt.title('Engagement Threshold vs Churn')
plt.ylabel('Churn Rate')
plt.xlabel('Engagement Score Bins')
plt.show()

            # KPL CALCULATION
# 1. Engagement Retention Ratio------
active_churn = data[data['IsActiveMember'] == 1]['Exited'].mean()
inactive_churn = data[data['IsActiveMember'] == 0]['Exited'].mean()

engagement_retention_ratio = active_churn / inactive_churn

print("Engagement Retention Ratio:", engagement_retention_ratio)

# 2. Product Depth Index----------
# Avg products used by retained customers
retained = data[data['Exited'] == 0]
product_depth_index = retained['NumOfProducts'].mean()

print("Product Depth Index:", product_depth_index)

# 3. High-Balance Disengagement Rate
# Define high balance threshold (top 25%)
threshold = data['Balance'].quantile(0.75)

high_balance_customers = data[data['Balance'] >= threshold]
high_balance_inactive = high_balance_customers[high_balance_customers['IsActiveMember'] == 0]

high_balance_disengagement_rate = len(high_balance_inactive) / len(high_balance_customers)

print("High-Balance Disengagement Rate:", high_balance_disengagement_rate)

# 4. Credit Card Stickiness Score----------------
cc_customers = data[data['HasCrCard'] ==1]
cc_retention_rate = 1 - cc_customers['Exited'].mean()

print("Credit Card Stickiness Score:", cc_retention_rate)

# 5. Relationship Strength Index----------------
# Combine engagement + product usage (normalized)

# Normalize columns
data['Engagement_Score'] = data['IsActiveMember']
data['Product_Score'] = data['NumOfProducts'] / data['NumOfProducts'].max()

# Weighted score (you can adjust weights)
data['Relationship_Strength_Index'] = (
    0.5 * data['Engagement_Score'] +
    0.5 * data['Product_Score']
)

# Average RSI
RSI = data['Relationship_Strength_Index'].mean()

print("Relationship Strength Index:", RSI)
print(data)
