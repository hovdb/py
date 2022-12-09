#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:08:01 2022

@author: b hovd
"""


import requests
import json
from requests.exceptions import HTTPError
from prettytable import PrettyTable
host = input('Enter the hostname of the URL: ' )
api = input('Enter API Key: ')

try:
    response = requests.get('https://' + host + '.appomni.com/api/v1/detection/detectionalert/', headers={'Authorization': 'Bearer ' + api})
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    #print("Entire JSON response")
    #print(jsonResponse)
    
    

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
    
myTable = PrettyTable(["Time","Rule","User","Message","ID"])
myTable.hrules=='ALL'
myTable._max_width = {"Time" : 19,"Rule" : 20, "User" : 20, "Message" :70, "ID" :20}

for key in jsonResponse["results"]:
    #print(key['id'])
    
    
 #  try:
       #print(key["event"]["message"])  
       myTable.add_row([key["created"],key["event"]["rule"]["name"],key["event"]["related"]["user"],key["event"]["message"],key["id"]])

print(myTable)
