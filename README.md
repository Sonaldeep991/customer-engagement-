Customer Engagement and Churn Analysis
Project Overview

This project analyzes customer engagement patterns and identifies factors influencing customer churn in the banking sector. Using Python and data analysis techniques, the project segments customers based on their engagement levels, evaluates retention strength, detects at-risk premium customers, and generates business insights to improve customer retention strategies.

Objectives
Analyze customer engagement behavior.
Identify factors contributing to customer churn.
Segment customers based on activity and product usage.
Detect high-value customers who are at risk of leaving.
Develop custom KPIs to measure customer relationship strength and retention.
Dataset

The analysis uses a banking customer dataset containing information such as:

Customer demographics
Account balance
Number of products used
Credit card ownership
Active membership status
Estimated salary
Customer churn status (Exited)
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Key Features
1. Data Cleaning and Validation
Removed unnecessary columns (e.g., Surname).
Checked for missing values.
Validated binary columns:
HasCrCard
IsActiveMember
Exited
2. Customer Engagement Analysis
Created an Engagement Score using:
Active membership status
Number of products owned
Credit card ownership
3. Customer Segmentation

Customers were classified into categories such as:

Active Engaged
Inactive Disengaged
Active Low Product
Inactive High Balance
Other
4. Churn Analysis
Calculated churn rate by number of products.
Compared retention rates between single-product and multi-product customers.
Analyzed the relationship between product depth and churn.
5. Balance and Activity Analysis
Categorized customers based on account balance.
Performed cross-analysis between balance levels and customer activity status.
6. Salary-Balance Mismatch Detection

Identified unusual customer profiles:

High Salary – Low Balance
Low Salary – High Balance
7. At-Risk Premium Customer Identification

Detected premium customers based on:

Top 25% balance
Top 25% salary

Flagged customers as at-risk if they were:

Inactive members
Using one or fewer products
Already churned
8. Retention Strength Assessment

Calculated engagement-based metrics to classify customers as:

Sticky Customers
Non-Sticky Customers
Analyzed churn trends across different engagement tiers.
Key Performance Indicators (KPIs)Engagement Retention Ratio
Compares churn rates between active and inactive customers.
Product Depth Index
Measures the average number of products used by retained customers.
High-Balance Disengagement Rate
Identifies disengagement among high-value customers.
Credit Card Stickiness Score
Measures retention among customers with credit cards.
Relationship Strength Index (RSI)
Combines engagement and product usage scores to estimate customer relationship strength.


