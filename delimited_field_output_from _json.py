import requests
import re
from requests.exceptions import HTTPError
#from prettytable import PrettyTable
host = input('Enter the hostname of the URL: ' )
api = input('Enter API Key: ')

try:
    response = requests.get('https://' + host + '.appomni.com/api/v1/insights/discoveredinsight/', headers={'Authorization': 'Bearer ' + api})
    response.raise_for_status()
    # access JSOn content
    jsonResponse = response.json()
    #print("Entire JSON response")
    #print(jsonResponse["details"])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')
#myTable = PrettyTable(["Risk Level", "ServiceType", "Insight", "Description", "Category", "Potential Risk", "Risk Score"])
#myTable.hrules=='ALL'
#myTable._max_width = {"Risk Level" : 3, "ServiceType" :3, "Insight" : 50, "Description" : 80, "Category" : 30, "Potential Risk" : 60, "Risk Score" : 3}

for key in jsonResponse:
    risk = requests.get('https://' + host + '.appomni.com/api/v1/insights/discoveredinsight/details_for_insight/?internal_name=' + key['internal_name'], headers={'Authorization': 'Bearer ' + api})
    s= str(risk.json())
    try:
        match = re.search(r"Potential Risk:\s'\}\,\s\{'insert':\s['|\"](.*?)\\n['|\"]\}", s).group(1)
        #if match:
        insight = key['risk_level'],key['service_type'], key['label'], key['description'], key['insight_category'],match, key['risk_score']
        print(insight)
        with open(host + '_InsightsExport6.txt', 'a') as w:
            w.write(str(insight)+'\n')
        #myTable.add_row([key['risk_level'],key['service_type'], key['label'], key['description'], key['insight_category'],match, key['risk_score']])
    except AttributeError as err:
        
       
            match = "NA"   
