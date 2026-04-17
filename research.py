
'''1.Problem Statement------

Lack of clarity on how engagement impacts churn
Limited understanding of product utilization and retention
Over-reliance on financial indicators for loyalty prediction.

2.Objectives----
Evaluate the relationship between engagement and churn
Measure the impact of product usage on retention
Identify high-value but disengaged customers.

3.Dataset Description

Column Name	      Description---
CustomerId	      Unique identifier
Surname	          Customer name
CreditScore	      Creditworthiness
Geography	      Customer location
Gender	          Male/Female
Age	              Age of customer
Tenure	          Years with bank
Balance	          Account balance
NumOfProducts	  Number of products used
HasCrCard	      Credit card ownership
IsActiveMember	  Activity status
EstimatedSalary	  Annual income
Exited	          Churn indicator

4.Methodology----

Loaded dataset into analysis environment (Python/SQL)
Checked missing values and inconsistencies
Validated binary fields (IsActiveMember, HasCrCard)
Ensured churn variable (Exited) correctness

5.Engagement Classification----

Active Engaged Customers
Active users with multiple products
Inactive Disengaged Customers
No activity and low product usage
Active Low-Product Customers
Active but limited engagement depth
Inactive High-Value Customers
High balance but low activity

6.Product Utilization Analysis----
Calculated churn rate by number of products
Compared:
Single-product customers vs multi-product customers
Observed relationship:
More products → lower churn probability

7.Financial vs Engagement Analysis---
Cross-analyzed balance and activity
Identified:
High balance + inactive = high churn risk
Salary vs balance mismatch used to detect:
Underutilized premium customers

8.Retention Strength Assessment----

Defined “sticky customers” as:

Active users
Using 2+ products
Consistent engagement

Measured churn stability across:

Engagement tiers
Product count groups

9.Key Performance Indicators (KPIs)---

  Engagement Retention Ratio
Measures churn difference between active and inactive customers
Finding: Active customers churn significantly less

10.Product Depth Index----
Number of products vs retention strength
Finding: Customers with ≥2 products show strong loyalty
    
11.High-Balance Disengagement Rate----
% of high-balance inactive customers who churn
Finding: Financial strength alone does NOT ensure retention

12.Credit Card Stickiness Score----
Impact of credit card ownership on retention
Finding: Card users are slightly more retained due to frequent interaction

13.Relationship Strength Index----
Composite metric combining:

Engagement
Product usage
Financial commitment


Streamlit Dashboard Implementation----

Core Modules:
Engagement vs churn visualization
Product usage impact analysis
High-value customer risk detection
Retention scoring panel


User Controls:
Filters for engagement
Product sliders
Balance & salary thresholds

conclusion

This study highlights that customer retention is primarily driven by behavioral 
engagement and product utilization rather than financial indicators alone.
Banks must shift from static analysis to dynamic behavioral tracking to effectively reduce churn. 
By leveraging engagement metrics and product depth insights, institutions can design more
targeted and efficient retention strategies.'''