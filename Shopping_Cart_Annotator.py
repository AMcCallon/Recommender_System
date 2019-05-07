#Import Packages
import pandas as pd
import requests
import ujson
from confluent_kafka import Consumer, KafkaError

#Create the index if one does not exist using function
def create_index(index, index_config):
    r = requests.put('http://elasticsearch:9200/{}'.format(index), json = index_config)
    if r.status_code != 400:
        print('Error creating index')
        print(r.status_code)
    else:
        print('created')


#Delete Index if it exists function
def delete_es_index(index):
    r =  requests.delete('http://elasticsearch:9200/{}'.format(index))
    if r.status_code !=200:
        print('Error Deleting Index')
    else:
        print('index deleted')

#Read in CSV
df = pd.read_csv('Online_Retail.csv')

#Group the CSV by Invoice Number
invoice_groups = df.groupby('InvoiceNo')



#Create Index
index_config = {
    "mappings": {
        'basket':  {
            'properties':{
                'StockCodes':{'type':'string',"fields":{"keyword":{"type":"keyword"}}, "fielddata":True},
                'Descriptions':{'type':"string", "fielddata":True},
                'Quantities':{'type':'integer'},
                'Unitprices':{'type':'scaled_float'}
            }
        }
    }
}


#Assign Index Name
index_name = 'shopping_cart'
#Delete any existing indexes
delete_es_index(index_name)

#Create a new index
create_index(index_name, index_config)


# iterate over each group (each invoice)
for invoice_name, invoice in invoice_groups:
    basket = {}
    stockcodes = []
    descriptions = []
    quantities = []
    unitprices = []
    # iterate over rows in this invoice dataframe
    for row_index, row in invoice.iterrows():
        # these fields are the same for each row, so doesn't matter if we keep overwriting
        basket['InvoiceNo'] = row['InvoiceNo']
        basket['CustomerID'] = row['CustomerID']
        basket['InvoiceDate'] = row['InvoiceDate']
        basket['Country'] = row['Country']
        # these fields are different for each row, so we append to lists
        stockcodes.append(row['StockCode'])
        descriptions.append(row['Description'])
        quantities.append(row['Quantity'])
        unitprices.append(row['UnitPrice'])
    basket['StockCodes'] = stockcodes
    basket['Descriptions'] = descriptions
    basket['Quantities'] = quantities
    basket['UnitPrices'] = unitprices

    #Send to elasticsearch
    r = requests.post('http://elasticsearch:9200/shopping_cart/basket', json =basket)
    if r.status_code !=201:
        print('Error: Could Not Send Message to ElasticSearch')
        print('r.status_code')
    else:
        print('Message was sent')
