#Import Packages
import requests
import pandas as pd

def execute_es_query(index, query):
    r = requests.get("http://elasticsearch:9200/{}/_search".format(index), json =query)
    #if r.status_code !=200:
     #  print("Error executing query")
    #else:
    return r.json()


#Read in CSV
df = pd.read_csv('Online_Retail.csv', usecols = ["StockCode"])
unique_stock_code = df.StockCode.unique()
unique_stock_code = list(unique_stock_code)
del df

#Take User Input
user_stock_code = input("Enter an Valid Stockcode (i.e. 22297, 85123A, 10002): ")

#Check to see if the given input is a valid StockCode
try:
    b=unique_stock_code.index(user_stock_code)
except ValueError:
    print("Error: Input provided was not a Valid StockCode.  \n The Script will now exit,please try again")
    raise SystemExit() #If given code is not valid, exit the script
else:
    print('Valid StockCode was provided') #Let user know the code is valid and continue


#Create Query
query = {
  "size":0,
  "query": {
    "bool": {
      "filter": [
        {
          "term": {
            "StockCodes": 22297
          }
        }
      ]
    }
  },
  "aggs": {
    "bestMatch": {
      "terms": {
        "field": "StockCodes.keyword",
        "exclude": "22297",
        "min_doc_count": 50
      }
    },
    "correlated_words": {
      "significant_terms": {
        "field": "StockCodes.keyword",
        "exclude": "22297",
        "min_doc_count": 50
      }
    }
  }
}

#Run the execute query function
res = execute_es_query("shopping_cart" , query)
#Print results
print(res)
