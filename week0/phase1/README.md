PHASE 1

---SparkSession Initialization      
  Created a Spark environment using SparkSession which acts as the entry point for working with PySpark. It is used to create DataFrames, execute SQL queries, and manage the      overall data processing workflow.
  
---Problem Statement            
  Retrieved all customer records, filtered customers based on city (Chennai) and age (>25), selected specific columns (customer_name, city), and performed aggregation to count    customers per city using SQL queries.
  
---Approach & Methods Used          
  Loaded data into a DataFrame and displayed it using show() for visualization. Applied filtering using both WHERE in SQL and filter() in PySpark, selected columns using          SELECT, and performed aggregation using GROUP BY with COUNT() to analyze grouped data.
  
---Key Learnings                  
  Gained understanding of working with PySpark and SQL together, executing queries on DataFrames, applying filtering and aggregation techniques, and building a simple data        analysis workflow efficiently.
