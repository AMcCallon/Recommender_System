# Recommender_System
Unstructured Data Final Exam Recommender System


## Files needed to fully run 

Three files are needed to run depending on the need:
  - Online Retail.xlsx
  - Convert_xlsx_to_csv.py
  - Shopping_Cart_Annotator.py
  - run_query.py
  
Not all of the above file will be needed to run the full recommender system depening on what already exists on the users system

### Online Retail.xlsx

This excel file contains the data that we are going to be loading into Kibana.  Before this happens however, it will need to be converted into a csv file.  This can either be done with Convert_xlsx_to_csv.py or by manually saving the file as "Online_Retail.csv".

### Convert_xlsx_to_csv.py

This file is used to convert Online Retail.xlsx to a csv file titled "Online_Retail.csv". This csv file is needed in order to run either Shopping_Cart_Annotator.py or run_query.py

If you already have "Online_Retail.csv" then this script should not be ran.

### Shopping_Cart_Annotator.py

This file is used to creat an index, delete an index, and send messages to an index in Kibana.  

#### NOTE: THIS SCRIPT DOES TAKE A FEW MINUTES TO FULLY RUN 
The file run_query.py can be ran before Shopping_Cart_Annotator.py is completely finished running.  It will need to be reran once Shopping_Cart_Annotator.py has finished to recieve consistent answers.

### run_query.py

The file run_query.py takes a user input for a StockCode, and will run a query in Kibana to return recommendations based on 






The output of run_query.py should look approximately like this. (StockCode 22297 was used for this example)

```
{'took': 427, 'timed_out': False, '_shards': {'total': 5, 'successful': 5, 'skipped': 0, 'failed': 0}, 'hits': {'total': 50, 'max_score': 0.0, 'hits': []}, 'aggregations': {'bestMatch': {'doc_count_error_upper_bound': 10, 'sum_other_doc_count': 1724, 'buckets': []}, 'correlated_words': {'doc_count': 50, 'bg_count': 2941, 'buckets': []}}}

```
