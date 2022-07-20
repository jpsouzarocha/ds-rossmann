import json
import requests
import pandas as pd

# loading test dataset
d10 = pd.read_csv('/home/joao94/repos/DS-em-produção/test.csv')

# merge test + store datasets
df_test = pd.merge(d10, df_store_raw, how='left', on='Store')

# choose store for prediction
df_test = df_test[df_test['Store'] == 22]

# remove closed stores
df_test = df_test[df_test['Open'] != 0]
df_test = df_test[~df_test['Open'].isnull()]
df_test = df_test.drop('Id', axis=1)

# convert dataframe to json
data = json.dumps(df_test.to_dict(orient='records'))

# API Call
url = 'http://0.0.0.0:5000/rossmann/predict'
header = {'Content-type': 'application/json'}
data = data

r = requests.post(url, data=data, headers=header)
print(f'Status Code {r.status_code}')
