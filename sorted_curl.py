from MovieLens import MovieLens
from surprise import SVD
import csv
import requests
import json
import shlex
import pycurl
import subprocess


api_key = 'Bearer keyHbd3ja5QEm4pVa'
url = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande"

headers = {'Authorization': api_key, 'accept': 'application/json'}
url_for_search = f"{url}?filterByFormula=User_ID"


def fetch_airtable(query):
    offset = ''
    url_for_search = f"{url}?filterByFormula=User_ID"
    if (query > 0):
        url_for_search = url_for_search + '=' + str(query)

    # query = 'Sundsvall'
    limit = 3     # 100 is max number of hits that can be returned.
    # If there are more (which you find with 'limit' : 0 ) you have to use offset and multiple requests to get all ads
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search, headers=headers, params=search_params)
    # print(response.content)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']
    total_recs = len(hits)
    with open('../../dev/Jobmaking/Data/najj.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'User_ID', 'Namn', 'Yrke','Beskrivning'])
        for hit in hits:
            # print( hit['id'], hit['fields']['User_ID'], hit['fields']['Namn'], hit['fields']['Yrke'], hit['fields']['Beskrivning'] )
            employee_writer.writerow([hit['id'], hit['fields']['User_ID'], hit['fields']['Namn'], hit['fields']['Yrke'], hit['fields']['Beskrivning'] ])

    if 'offset' in json_response:
        offset = json_response['offset']
    else:
        offset = ''


    while (offset != ''):
        search_params = {'limit': limit, 'offset': offset} #'': query, 
        response = requests.get(url_for_search, headers=headers, params=search_params)
        response.raise_for_status()  # check for http errors
        json_response = json.loads(response.content.decode('utf8'))
        
        hits = json_response['records']
        total_recs = total_recs + len(hits)

        with open('../../dev/Jobmaking/Data/najj.csv', mode='a+') as jobPath:
            employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for hit in hits:
                # print( hit['id'], hit['fields']['User_ID'], hit['fields']['Namn'], hit['fields']['Yrke'], hit['fields']['Beskrivning'] )
                employee_writer.writerow([hit['id'], hit['fields']['User_ID'], hit['fields']['Namn'], hit['fields']['Yrke'], hit['fields']['Beskrivning'] ])

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''


    print(total_recs)


query = 0
fetch_airtable(query)


# #curl https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -d '{"sort": [ { "User_ID": "desc" } ] } '
# cmd = 'curl https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande?filterByFormula=User_ID=26 -H "Authorization: Bearer keyHbd3ja5QEm4pVa" '
# process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
