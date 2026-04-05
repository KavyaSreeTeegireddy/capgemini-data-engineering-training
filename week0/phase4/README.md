PHASE4

## SparkSession Initialization             
Created a Spark environment using SparkSession to efficiently process large-scale customer and sales datasets. It was used to load CSV files into DataFrames and perform transformations and actions.
## Problem Statement 
Cleaned and prepared customer and sales datasets, joined them to combine relevant information, calculated key metrics such as daily sales, total spending, and order count, applied aggregations for city-wise revenue and top customers, implemented business logic for customer segmentation, and generated the final reporting dataset.
## Approach & Methods Used
Loaded datasets into DataFrames and performed initial preparation. Converted data types using withColumn() and cast(). Combined datasets using join() (inner join). Applied transformations and filtering using filter(). Performed aggregations using groupBy() with sum(), avg(), and count(). Implemented business logic using when() for customer segmentation. Sorted and limited results using orderBy() and limit(). Referenced and renamed columns using col() and alias(). Displayed outputs using show() and generated the final reporting output.
## Key Learnings
Importance of cleaning and preparing data before analysis. Understanding how joins help in combining datasets for better insights. Applying aggregation functions to compute meaningful metrics. Using conditional logic for business rules like segmentation. Building a complete end-to-end PySpark data processing pipeline
