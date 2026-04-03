
PHASE3

## SparkSession Initialization             
Created a Spark environment using SparkSession to process large-scale customer and sales data efficiently. It was used to load CSV files into DataFrames and perform transformations and actions for analysis.
## Problem Statement 
Cleaned and analyzed customer and sales datasets by handling null values and invalid records. Computed key metrics like daily sales, total spending, order count, and identified repeat and top customers along with city-wise revenue insights.
## Approach & Methods Used
Loaded datasets into DataFrames and performed data cleaning using dropna(), filter(), and type casting with withColumn() and cast(). Combined datasets using join() (inner join), applied aggregations using groupBy() with sum(), avg(), and count(), used col(), alias(), and displayed outputs with show().
## Key Learnings
Understood the importance of data cleaning before processing and preparing datasets before joins. Learned how to apply aggregations and transformations to build an end-to-end PySpark pipeline for generating meaningful business insights.
