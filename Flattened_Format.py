#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:08:01 2022

@author: b hovd
"""

import json
import requests

host = input('Enter the hostname of the URL: ' )
api = input('Enter API Key: ')
wf = input('Enter Work Flow Name: ')

# Making a request for workflow IDs
response = requests.get('https://' + host + '.appomni.com/api/v1/integrations/workflowinstance', headers={'Authorization': 'Bearer ' + api})
policies = json.loads(response.text)
#print(policies)
for policy in policies:
    if policy['name'] == wf:
        wfid =str(policy['id'])
    

# Making a PATCH request
status = requests.patch('https://' + host + '.appomni.com/api/v1/integrations/workflowinstance/' + wfid + '/', headers={'Authorization': 'Bearer ' + api}, data={"data_format":"policy.issues.mapped"})
#status code
#print(status)
# print content of request
#print(status.content)
stat = str(status)
if stat == '<Response [200]>':
        print('Success! AppOmni Work Flow \"' + wf + '\" is now in a flattened format.')
else:
    print('!!!!!Check your hostname, API key & workflow name!!!!!')  
