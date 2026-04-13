PySpark Data Processing & Analysis – Car Sales Dataset
Dataset Overview

This project works with three datasets:

customers → (customer_id, name, city)
cars → (car_id, brand, model, price)
sales → (sale_id, customer_id, car_id, sale_date, quantity)

These datasets are joined to perform data cleaning, validation, transformation, and analysis.

Phase 1 – Data Understanding
Loaded CSV data using PySpark with schema inference.
Verified structure using printSchema().
Identified issues such as:
Null values
Negative prices
Duplicate records                                                                                                              
Phase 2 – Data Cleaning
Handled missing values using fillna().
Corrected invalid values:
Replaced negative prices with NULL.
Removed invalid records:
Filtered out rows with null keys (customer_id, car_id).                                                                                
Phase 3 – Data Validation
Used anti join to identify unmatched records (e.g., sales without valid customers).
Generated a validation report:
Total records
Valid customer and car references                                                                      
Phase 4 – Data Transformation
Created a new column:
Revenue = price × quantity
Aggregations performed:
Revenue per customer
Cars sold per brand
Revenue per city
