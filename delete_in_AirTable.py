from MovieLens import MovieLens
from surprise import SVD
import csv
import requests
import json
import shlex
import pycurl
import subprocess


api_key = 'Bearer keyHbd3ja5QEm4pVa'
url0 = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb"
url2 = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning"

headers = {'Authorization': api_key, 'accept': 'application/json'}
url_for_search0 = f"{url0}"
url_for_search2 = f"{url2}"


def delete_in_airtableJOBS(query):
    offset = ''
    limit = 100     # 100 is max number of hits that can be returned.
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search0, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']
    for hit in hits:
        del_id = hit['id']
        cmd = 'curl -v -X DELETE https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -G --data-urlencode \'records[]=' + del_id + '\''
        # print (cmd)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()

    if 'offset' in json_response:
        offset = json_response['offset']
    else:
        offset = ''

    while (offset != ''):
        search_params = {'limit': limit, 'offset': offset} #'': query, 
        response = requests.get(url_for_search0, headers=headers, params=search_params)
        response.raise_for_status()  # check for http errors
        json_response = json.loads(response.content.decode('utf8'))
        
        hits = json_response['records']
        for hit in hits:
            del_id = hit['id']
            cmd = 'curl -v -X DELETE https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -G --data-urlencode \'records[]=' + del_id + '\''
            # print (cmd)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''


def delete_in_airtableMATCHES(query):
    offset = ''
    limit = 100     # 100 is max number of hits that can be returned.
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search2, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']
    for hit in hits:
        del_id = hit['id']
        cmd = 'curl -v -X DELETE https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -G --data-urlencode \'records[]=' + del_id + '\''
        # print (cmd)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.communicate()

    if 'offset' in json_response:
        offset = json_response['offset']
    else:
        offset = ''

    while (offset != ''):
        search_params = {'limit': limit, 'offset': offset} #'': query, 
        response = requests.get(url_for_search2, headers=headers, params=search_params)
        response.raise_for_status()  # check for http errors
        json_response = json.loads(response.content.decode('utf8'))
        
        hits = json_response['records']
        for hit in hits:
            del_id = hit['id']
            cmd = 'curl -v -X DELETE https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -G --data-urlencode \'records[]=' + del_id + '\''
            # print (cmd)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''


query = 0

# delete_in_airtableJOBS(query)
delete_in_airtableMATCHES(query)