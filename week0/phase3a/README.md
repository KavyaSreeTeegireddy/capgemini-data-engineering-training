
PHASE3a

## SparkSession Initialization             
Created a Spark environment using SparkSession to process large-scale customer and sales data efficiently. It was used to load CSV files into DataFrames and perform transformations and actions for analysis.
## Problem Statement 
Identify data issues (nulls, duplicates, invalid values). Clean data (handle missing values, remove duplicates, filter invalid age). Validate data after cleaning (row count checks). Apply transformations (filtering, column handling). Perform aggregation (customer count per city). Generate final cleaned output for analysis
## Approach & Methods Used
Created a DataFrame from raw input data and performed data cleaning by handling missing values using fillna(), removing duplicates with dropDuplicates(), and filtering invalid records using filter(). Validated the cleaned dataset through row count checks to ensure correctness. Data Cleaning: fillna(), dropDuplicates()
Filtering: filter()
Aggregation: groupBy() with count()
Data cleaning - fillna(), dropDuplicates() 
## Key Learnings
Importance of cleaning data (nulls, duplicates, invalid values) Validating data after cleaning Using aggregation to summarize data Building a simple data processing workflow
