PySpark End-to-End Data Pipeline – Car Sales & Dealer Analytics
Dataset Overview

This project processes and analyzes sales data using multiple related datasets:

customers → (customer_id, name, city)                                                                                                                      
cars → (car_id, brand, model, price)                                                                                                                              
sales → (sale_id, customer_id, car_id, sale_date, quantity)                                                                                                  
dealers → (dealer_id, name, city)                                                                                          
sales_dealer → (sale_id, dealer_id)                                                                                                                        

These datasets are integrated to build a complete analytics pipeline.

Phase 1 – Data Understanding
Loaded all datasets using PySpark with schema inference.
Verified structure using schema checks and record counts.
Identified potential issues:
Missing values (nulls)
Duplicate records
Invalid values (e.g., negative prices)                                                                
Phase 2 – Data Cleaning
Handled null values using appropriate default replacements.
Corrected invalid data:
Negative car prices were replaced with nulls.
Standardized text fields:
Trimmed leading/trailing spaces in string columns.
Ensured data integrity:
Removed records with invalid foreign keys (customer_id, car_id, dealer_id).                                                                                                    
Phase 3 – Data Validation                                                                                                          
Used left anti joins to detect:
Sales without valid customers
Sales without valid cars
Dealer mappings without valid references
Generated a validation report including:
Total records
Valid vs invalid key counts
Data quality summary                                                                                                                                    
Phase 4 – Data Transformation                                                                                                                  
Created derived metric:
Revenue = price × quantity
Aggregations performed:
Customer revenue → total spend per customer
Brand-wise sales → total cars sold per brand
City-wise revenue → revenue contribution by city                                                                                                                        
Phase 5 – Dealer Analytics                                                                                                              
Integrated dealer data via sales_dealer mapping.
Performed key analyses:
Revenue per dealer
Top dealers by revenue
Dealer-city contribution → revenue distribution across cities per dealer
Phase 6 – SQL Analysis (PySpark)                                                                                                                    
Top 3 customers per city
Implemented using window functions (row_number)
Monthly trends
Extracted year and month from sale_date
Aggregated revenue over time
Repeat customers
Identified customers with multiple purchases                                                                                                                    
Phase 7 – Output                                                                                                                                      
Saved processed and aggregated results to storage (CSV/Parquet).
Prepared structured outputs for:
Customer insights
Dealer performance
