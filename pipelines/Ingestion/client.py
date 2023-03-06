import pandas as pd
import requests

data = pd.read_csv('data.csv', sep=',')
api_endpoint = 'https://amhxxkxau1.execute-api.eu-west-3.amazonaws.com/beta/test'

# Simulate streaming by sending every transaction (row) to API gateway
for i in data.index:
    transaction = data.loc[i].to_json()
    response = requests.post(api_endpoint, data=transaction)
    print(response)
