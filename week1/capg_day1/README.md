CAPGEMINI-DAY 1

Data Cleaning & Preprocessing – Customer Dataset                  
**Overview**
  This project focuses on cleaning and preprocessing a customer dataset to ensure data quality, consistency, and usability for further analysis or modeling.               
**Dataset Description**
  The dataset contains the following columns:    
  CustomerID – Unique identifier for each customer    
  Name – Customer name    
  Country – Customer location    
  JoinDate – Date when the customer joined    
  Sales – Sales amount    
  Category – Customer category    
**Data Cleaning Steps Performed**    
  1. Handling Missing Values    
  Replaced blank values in Category with "Unknown"
  Replaced blank or missing values in Sales with 0
  Handled missing dates in JoinDate appropriately
  2. Date Formatting        
  Standardized the JoinDate column into a consistent date format
  Fixed inconsistent formats such as DD-MM-YYYY and MM-DD-YYYY
  3. Removing Duplicates      
  Identified and removed duplicate records to maintain data integrity
  4. Data Standardization    
  Ensured consistency in text fields (e.g., India, india, INDIA)
  Cleaned inconsistent entries in the Country column
**Final Outcome**          
  Cleaned dataset with no duplicate records
  Consistent date format across all rows
  No missing or ambiguous categorical values
  Sales column standardized with numeric values
**Usage**    
  This cleaned dataset can now be used for:    
  Data analysis
  Visualization
  Machine learning models
  Business insights generation
