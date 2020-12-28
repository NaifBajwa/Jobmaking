from MovieLens import MovieLens
from surprise import SVD
import csv
import requests
import json
import shlex
import pycurl
import subprocess

api_key1 = 'YidceGMwXHgwNFx4N2Y5XHhjYzpceGMxXHhjYlx4MGVceGI3QyE0XHhkMFx4YzIyXHhkY1x4YmZ2XHgwOCc'
url1 = "https://jobsearch.api.jobtechdev.se"

headers1 = {'api-key': api_key1, 'accept': 'application/json'}
url_for_search1 = f"{url1}/search"

def fetch_100_jobs(query):
    offset = ''
    # query = 'Sundsvall'
    limit = 100     # 100 is max number of hits that can be returned.
    # If there are more (which you find with 'limit' : 0 ) you have to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit} #, 'offset': offset
    response = requests.get(url_for_search1, headers=headers1, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    hits = json_response['hits']
    counter = 0
    data = []

    for hit in hits:
        counter = counter + 1
        # data[counter] = [counter,hit['headline'] , query, hit['employer']['name'],hit['application_deadline'] ]
        data.append( {'jobID':counter, 'Titel':hit['headline'] , 'Yrke':query, 'Arbetsgivare':hit['employer']['name'], 'Beskrivning': hit['description']['text_formatted'],'application_deadline':hit['application_deadline'] })

    if 'offset' in json_response:
        offset = json_response['offset']
    else:
        offset = ''

    while (offset != ''):
        search_params = {'q': query, 'limit': limit, 'offset': offset} #'': query, 
        response = requests.get(url_for_search1, headers=headers1, params=search_params)
        response.raise_for_status()  # check for http errors
        json_response = json.loads(response.content.decode('utf8'))
        
        hits = json_response['hits']
        for hit in hits:
            counter = counter + 1
            data.append({'jobID':counter, 'Titel':hit['headline'] , 'Yrke':query, 'Arbetsgivare':hit['employer']['name'], 'application_deadline':hit['application_deadline'] })

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''

    with open('Data/'+query+'.json', 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


api_key = 'Bearer keyHbd3ja5QEm4pVa'
url = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande"
url0 = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb"
url2 = "https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning"

headers = {'Authorization': api_key, 'accept': 'application/json'}
url_for_search = f"{url}?filterByFormula=User_ID"
url_for_search0 = f"{url0}"
url_for_search2 = f"{url2}"


def converCSV2JSON(csvFile, jsonFile):
    data = []
    with open(csvFile, newline='') as csvFile:
        csvFileReader = csv.DictReader(csvFile)
        next(csvFileReader)
        for rows in csvFileReader:
            # print (rows)
            data.append(rows)

    with open(jsonFile, 'w') as jsonFile:
        jsonFile.write(json.dumps(data, indent=4))


def fetch_airtable(query):
    offset = ''
    url_for_search = f"{url}?filterByFormula=User_ID"
    if (query > 0):
        url_for_search = url_for_search + '=' + str(query)

    limit = 30     # 100 is max number of hits that can be returned.
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']

    with open('../../dev/Jobmaking/Data/JobSeekers.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'User_ID', 'Namn', 'Yrke','Beskrivning'])
        for hit in hits:
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

        with open('../../dev/Jobmaking/Data/JobSeekers.csv', mode='a+') as jobPath:
            employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for hit in hits:
                employee_writer.writerow([hit['id'], hit['fields']['User_ID'], hit['fields']['Namn'], hit['fields']['Yrke'], hit['fields']['Beskrivning'] ])

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''

    converCSV2JSON('../../dev/Jobmaking/Data/JobSeekers.csv', '../../dev/Jobmaking/Data/JobSeekers.json')


def fetch_airtableJOBS(query):
    offset = ''
    limit = 30     # 100 is max number of hits that can be returned.
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search0, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']
    with open('../../dev/Jobmaking/Data/Lediga_jobb.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'Job_ID', 'Titel', 'Yrke','Beskrivning', 'Ort', 'Arbetsgivare'])
        for hit in hits:
            employee_writer.writerow([hit['id'], hit['fields']['Job_ID'], hit['fields']['Titel'], hit['fields']['Yrke'], hit['fields']['Beskrivning'], hit['fields']['Ort'], hit['fields']['Arbetsgivare'] ])

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

        with open('../../dev/Jobmaking/Data/Lediga_jobb.csv', mode='a+') as jobPath:
            employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for hit in hits:
                employee_writer.writerow([hit['id'], hit['fields']['Job_ID'], hit['fields']['Titel'], hit['fields']['Yrke'], hit['fields']['Beskrivning'], hit['fields']['Ort'], hit['fields']['Arbetsgivare'] ])

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''

    converCSV2JSON('../../dev/Jobmaking/Data/Lediga_jobb.csv', '../../dev/Jobmaking/Data/Lediga_jobb.json')


def fetch_airtableMATCHES(query):
    offset = ''
    limit = 30     # 100 is max number of hits that can be returned.
    search_params = {'limit': limit, 'offset': offset} #'': query, 

    response = requests.get(url_for_search2, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    
    hits = json_response['records']
    with open('../../dev/Jobmaking/Data/Matchning.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['ID', 'Name', 'Yrke', 'Annonstitel','Arbetsgivare', 'Sista ansökningsdatum'])
        for hit in hits:
            employee_writer.writerow([hit['id'], hit['fields']['Name'], hit['fields']['Yrke'], hit['fields']['Annonstitel'], hit['fields']['Arbetsgivare'], hit['fields']['Sista ansökningsdatum'] ])

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

        with open('../../dev/Jobmaking/Data/Matchning.csv', mode='a+') as jobPath:
            employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for hit in hits:
                employee_writer.writerow([hit['id'], hit['fields']['Name'], hit['fields']['Yrke'], hit['fields']['Annonstitel'], hit['fields']['Arbetsgivare'], hit['fields']['Sista ansökningsdatum'] ])

        if 'offset' in json_response:
            offset = json_response['offset']
        else:
            offset = ''

    converCSV2JSON('../../dev/Jobmaking/Data/Matchning.csv', '../../dev/Jobmaking/Data/Matchning.json')


query = 0
# fetch_airtable(query)
# fetch_airtableJOBS(query)
# fetch_airtableMATCHES(query)

query1 = 'Västernorrland Jämtland'
fetch_100_jobs(query1)

# converCSV2JSON('Data/najj.csv', 'Data/najj.json')

# converCSV2JSON('Data/Matchning.csv', 'Data/Matchning.json')
# converCSV2JSON('Data/JobSeekers.csv', 'Data/JobSeekers.json')
# converCSV2JSON('Data/Lediga_jobb.csv', 'Data/Lediga_jobb.json')

# curl https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb -H "Authorization: Bearer keyHbd3ja5QEm4pVa"
# curl https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande -H "Authorization: Bearer keyHbd3ja5QEm4pVa" 
# cmd = 'curl https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Arbetss%C3%B6kande?filterByFormula=User_ID=26 -H "Authorization: Bearer keyHbd3ja5QEm4pVa" '
# process = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
