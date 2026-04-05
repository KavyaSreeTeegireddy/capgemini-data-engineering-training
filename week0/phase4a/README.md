
PHASE4a

## SparkSession Initialization             
Created a Spark environment using SparkSession to process customer and sales datasets. It was used to load CSV files into DataFrames and perform transformations and analytical operations.
## Problem Statement 
Calculated total customer spend and applied segmentation techniques like Gold, Silver, and Bronze.Compared rule-based, quantile-based, and ranking methods to identify the most effective segmentation approach.
## Approach & Methods Used
Loaded and joined datasets using join(), transformed data with withColumn() and cast(), and computed total spend using groupBy() with sum() and count().
Applied segmentation using when(), ranking with percent_rank(), and quantile-based analysis using approxQuantile().
## Key Learnings
Used aggregation methods like groupBy() with sum() and count() and combined datasets using join().Applied window functions like percent_rank(), conditional logic using when(), and quantile calculation using approxQuantile().
