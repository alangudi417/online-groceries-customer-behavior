# Instacart Customer Behavior Analysis

## 📊 Project Overview
This project analyzes customer purchasing behavior using transactional data from Instacart, an online grocery delivery platform. The objective is to identify patterns in how, when, and what customers purchase to generate insights that support marketing optimization and operational decision-making.

Using five interconnected datasets: 
- orders
- products 
- order_products 
- aisles 
- departments 

The project performs extensive data preprocessing and exploratory data analysis (EDA) to uncover consumer habits, product popularity trends, and reorder behavior.
The analysis simulates real-world data challenges, including missing values, duplicate records, and data inconsistencies, providing a practical demonstration of data cleaning and analytical problem-solving skills.

## 💼 Business Problem

Instacart processes thousands of grocery orders from customers with different purchasing habits, shopping frequencies, and product preferences. Without a clear understanding of customer behavior, it can be difficult to identify what drives purchases, when customers are most likely to shop, and which products contribute most to customer engagement and repeat orders.

The business needs to answer questions such as:
- When are customers most likely to place their orders?
- How frequently do customers return to shop?
- Which products and categories are purchased most often?
- Which products are most likely to be reordered?
- How large are typical customer baskets?
- Are there distinct customer purchasing patterns or segments?
- Which products can act as "anchor" products that encourage additional purchases?
- How can customer behavior insights be used to improve marketing and shopping experiences?

Without this analysis, marketing campaigns may rely on generalized assumptions rather than actual purchasing behavior, while operational teams may have limited visibility into demand patterns and customer shopping cycles.

## ⚙️ Skills Developed

#### 🛠️ Tools

`Python` `Pandas` `NumPy` `Jupyter` `Matplotlib` `Git` `GitHub`

#### Data Analysis & Python
- Pandas & NumPy
- Data Cleaning & Validation
- Exploratory Data Analysis (EDA)
- Statistical Analysis
- Data Aggregation
- Data Visualization with Matplotlib
- Behavioral Data Analysis

#### Data Preprocessing
- Missing Value Analysis
- Business-Logic-Based Imputation
- Duplicate Detection & Removal
- Data Consistency Validation
- Outlier Analysis
- Data Quality Assessment
- Data Type Validation
- Data Integrity Checks

#### Relational Data Analysis
- Multi-Table Data Analysis
- Data Integration
- Relational Dataset Analysis
- Table Relationships
- Merging & Joining Datasets
- Cross-Dataset Validation
- Product & Customer Hierarchy Analysis

#### Customer Behavior Analysis
- Customer Purchasing Behavior
- Order Frequency Analysis
- Shopping Cycle Analysis
- Basket Size Analysis
- Reorder Behavior Analysis
- Customer Purchasing Patterns
- Customer Segmentation
- Customer Loyalty Analysis

#### Exploratory Data Analysis
- Time-Based Analysis
- Day-of-Week Analysis
- Hourly Purchase Patterns
- Product Popularity Analysis
- Product Category Analysis
- Order Size Distribution
- Frequency Distribution Analysis
- Trend Identification

#### Business Analytics
- Customer Behavior Insights
- Product Performance Analysis
- Anchor Product Identification
- Customer Segmentation Strategy
- Marketing Opportunity Analysis
- Operational Demand Analysis
- Business Problem Translation
- Data-Driven Decision Making

## 📊 Dataset Description
The project uses five relational datasets:

- orders: Customer order history and timing information
- products: Product catalog details
- order_products: Mapping between orders and purchased products
- aisles: Product aisle categorization
- departments: High-level product groupings

These datasets enable multi-dimensional analysis of customer purchasing patterns and product relationships.

## ⚙️ Methodology
The project follows a structured data analysis workflow:

1. Data Preprocessing
- Identified and corrected dataset formatting issues
- Removed duplicate order records
- Handled missing values through business-logic-based imputation
- Validated dataset consistency across relational tables

2. Exploratory Data Analysis
- Customer order frequency analysis
- Product popularity and reorder behavior evaluation
- Shopping time and day pattern analysis
- Cart behavior and order size distribution analysis

3. Data cleaning highlights
- Duplicated orders
    - Identified 15 exact duplicate orders occurring on Wednesdays at 2:00 AM
    - Removed duplicates to ensure data reliability
- Missing product names
    - 1,258 missing product names, all belonged to a placeholder aisle and department
    - Imputed values as "Unknown" to preserve dataset integrity
- Days since prior order
    - 28,817 missing values corresponded exclusively to first-time customer orders
    - Provided valuable insight into new customer onboarding behavior
- Cart order missing values
    - 836 missing entries linked to unusually large orders (more than 64 items)
    - Imputed with outlier value to maintain ordering logic

## 📈 Project Highlights
- Performed real-world data cleaning and preprocessing
- Conducted multi-table relational data analysis
- Identified customer segmentation patterns
- Generated business-driven recommendations from behavioral data
- Demonstrated strong exploratory data analysis workflow

## 📈 Key Insights
1. Shopping Time Behavior
- Peak ordering occurs between 10:00AM and 4:00PM
- This pattern remains consistent across both high-demand and low-demand days

2. Customer purchasing frequency
- 2 types of customers were detected
    - Weekly shoppers (peak around 7 days)
    - Monthly shoppers (peak around 30 days)

3. Order size and customer loyalty
- Most customers place small orders (5 items)
- A smaller segment of loyal customers generates significantly larger baskets

## 📈 Results
After evaluating the customer behavior in general, the analysis reveals that certain products act as primary purchase drivers.
- Top examples: Bananas, Organic Bananas, Strawberries, Avocados. 
- This suggests that customers often start their shopping sessions with staple produce items
- Recommended to highlight anchor products early in the shopping, to increase conversion rates and reduce purchase friction. 
- Personalized marketing by customer segmentation.  

## ▶️ How to Run the Project
1. Clone this repository: git clone https://github.com/alangudi417/online-groceries-customer-behavior.git

2. Navigate to the project folder: cd online-groceries-customer-behavior

3. Create and activate virtual environment: python -m venv venv venv\Scripts\activate # Windows source venv/bin/activate # Mac/Linux

4. Install dependencies: pip install -r requirements.txt

5. Launch Jupyter Notebook: jupyter notebook

6. Open notebooks/online_groceries.ipynb