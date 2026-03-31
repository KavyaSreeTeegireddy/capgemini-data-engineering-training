PHASE2

## SparkSession Initialization             
Created a Spark environment using SparkSession to process large-scale data. It is used to read CSV files, create DataFrames, and perform transformations and actions on the data.
## Problem Statement 
Analyzed customer and sales data to calculate total spending per customer, identify top customers, find customers with no purchases, compute city-wise revenue, calculate average spending, and identify customers with multiple orders.
## Approach & Methods Used
Loaded CSV data into DataFrames and handled missing values using **bold text** dropna(). Used  **bold text**show() to display results, applied transformations like **bold text** groupBy() with **bold text**sum(),**bold text** avg(), and **bold text** count(), sorted data using **bold text**orderBy(), filtered using **bold text**filter(), and performed **bold text**joins (inner and left) to combine customer and sales data.
## Key Learnings
Learned how to perform real-world data analysis using PySpark, including data cleaning, aggregation, filtering, sorting, and joining multiple datasets to generate meaningful business insights.
