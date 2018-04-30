import csv
import json
import requests

url = "https://svcgtwynew.dev.cox.com/CLIFF/tls/clientids"
headers = {'Content-type': 'application/json'}
reader_dict = csv.DictReader(open("C:\\Users\\clifsmit\\Desktop\\test.csv"))

for row in reader_dict:

               #Params Dict
               data = {'clientid':row['clientid'],'clientsecret':row['clientsecret'],'scope':row['scope']}
               
               #Print params
               print(data)
               
               #Send Request
               request = requests.post(url, data, headers = headers)
              
               #Response Content
response = request.text
print(response)
