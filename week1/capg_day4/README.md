**Databricks Submission Analysis Project**                  
**Overview**

This project focuses on analyzing student assignment submissions using Databricks (PySpark + SQL). The goal is to clean and unify messy data, track submissions accurately, detect duplicates, and classify students based on their submission status.
**Datasets Used**                    
Master Table
Contains the official list of students (56 records)
Includes student ID and both college & personal email IDs
Task1_Responses
Contains actual student submissions (51 records)
Based on email IDs
Task1_File2
Contains extra data (60 records)
Includes duplicates, invalid entries, and noise
**Phase 1: Data Preparation**                                                                                
**Email Normalization**                                          
Emails were standardized by converting them to lowercase and removing unnecessary spaces. This ensures consistency and avoids mismatches during joins.
**Unified Email Mapping**                                                      
Since students can submit using either their college or personal email, both were combined into a single mapping. This allows linking multiple emails to one unique student ID, enabling accurate tracking.
**Phase 2: Core Analysis**                                              
**Students Who Did Not Submit**                                                                      
A comparison was made between the master list and submissions to identify students who did not submit any response.
**Valid Submissions**                                                                                        
Submissions that matched with the master dataset were identified as valid.
**Invalid Submissions**
Any email found in the submission data but not present in the master list was treated as invalid.
**Phase 3: Duplicate Detection**                                                                
**Identifying Duplicates**                                                                            
A window function was used to assign an order to submissions for each student. The earliest submission was treated as the valid one, while later ones were marked as duplicates.
**GROUP BY vs Window Functions**                                                    
GROUP BY helps count how many submissions exist per student.
Window functions go deeper by identifying exactly which records are duplicates and which one is original.
**Phase 4: Advanced Insights**                                                                    
**Submission Count per Student**                                                          
Calculated how many times each student submitted the assignment.
**Students Using Both Emails**                                                            
Identified students who used both their college and personal emails for submissions, which can indicate inconsistencies.
**Final Classification**                                                        
Each student was categorized into one of the following:
Submitted → Exactly one valid submission
Duplicate → Multiple submissions
Not Submitted → No submission found
Invalid → Submission email not found in master data                                                                            
**Challenges Faced**                                                                              
Inconsistent column names with spaces and formatting issues
CSV parsing problems due to messy input data
Duplicate and invalid records affecting accuracy
Email mismatches due to case sensitivity and extra spaces                                              
**Key Learnings**                                                                            
Data cleaning is a crucial first step in any analysis
Standardizing keys (like email) is essential for accurate joins
Window functions are powerful for real-world deduplication tasks
Understanding join types is critical for correct data insights                                                
**Final Outcome**                                                                                
A complete pipeline was built to:
Clean and standardize data
Map identities across multiple email sources
Detect duplicates and invalid entries
Accurately classify student submission status                                                    
**Conclusion**                                                                    
This project demonstrates a real-world data analytics workflow using Databricks. It highlights how raw, messy data can be transformed into meaningful insights through structured processing, making it highly relevant for practical data engineering and analytics scenarios.
