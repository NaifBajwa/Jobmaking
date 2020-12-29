from MovieLens import MovieLens
from surprise import SVD
import csv
import requests
import json
import shlex
import pycurl
import subprocess
import time

# offset = 0
#  + '/collab%20DB?offset=' + offset

api_key = 'YidceGMwXHgwNFx4N2Y5XHhjYzpceGMxXHhjYlx4MGVceGI3QyE0XHhkMFx4YzIyXHhkY1x4YmZ2XHgwOCc'
url = "https://jobsearch.api.jobtechdev.se"

headers = {'api-key': api_key, 'accept': 'application/json'}
url_for_search = f"{url}/search"


def test_search_loop_through_hits(query):
    # query = 'Sundsvall'
    limit = 100     # 100 is max number of hits that can be returned.
    # If there are more (which you find with 'limit' : 0 ) you have to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit}
    response = requests.get(url_for_search, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    total = json_response['total']
    hits = json_response['hits']
    print("Total number of jobs found is ", total['value'])

    with open('../../dev/Jobmaking/Data/AllJobsPath.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Job_ID', 'Title', 'genre', 'Arbetsgivare', 'Yrke','Beskrivning','Ort'])

        for hit in hits:
            # print(hit['id'],hit['headline'] , query, hit['employer']['name'],hit['occupation']['label'],hit['headline'], hit['employer']['workplace'])
            employee_writer.writerow([hit['id'],hit['headline'] , query, hit['employer']['name'],hit['occupation']['label'],hit['headline'], hit['employer']['workplace'] ])
   

# cmd = ''
# with open('./Data/AllJobsPath.csv', newline='') as csvfile:
#     allJobsReader = csv.reader(csvfile)
#     next(allJobsReader)
#     for job in allJobsReader:
#         cmd = 'curl -v -X POST https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -H "Content-Type: application/json" --data \'{"records": [{"fields": {'
#         cmd = cmd + '"Job_ID": "' + job[0] +'"'
#         cmd = cmd + ',"Titel": "' + job[1] + '"'
#         cmd = cmd + ',"Yrke": "' + job[4] +'"'
#         cmd = cmd + ',"Beskrivning": "' + job[5] +'"'
#         cmd = cmd + ',"Ort": "' + job[6] +'"'
#         cmd = cmd + ',"Arbetsgivare": "' + job[3] + '"}}]}\''

#         process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate()
#         # time.sleep (2)

# print (cmd)

def postCSVJobsTo_aws_dynamodb():
    cmd = ''
    with open('./Data/AllJobsPathNew.csv', newline='') as csvfile:
        allJobsReader = csv.reader(csvfile)
        next(allJobsReader)
        for job in allJobsReader:
            cmd = 'aws dynamodb put-item --table-name Avail_Jobs --item \'{'
            cmd = cmd + '"ID": {"N": "' + job[0] +'"}'
            cmd = cmd + ',"Titel": {"S": "' + job[1] + '"}'
            cmd = cmd + ',"Yrke": {"S": "' + job[4] +'"}'
            cmd = cmd + ',"Beskrivning": {"S": "' + job[5] +'"}'
            cmd = cmd + ',"Ort": {"S": "' + job[6] +'"}'
            cmd = cmd + ',"Arbetsgivare": {"S": "' + job[3] + '"}}\''

            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate()

    # print (cmd)


def search_for_AF_Jobs(query):
    limit = 100     # 100 is max number of hits that can be returned.
    # If there are more (which you find with 'limit' : 0 ) you have to use offset and multiple requests to get all ads
    search_params = {'q': query, 'limit': limit}
    response = requests.get(url_for_search, headers=headers, params=search_params)
    response.raise_for_status()  # check for http errors
    json_response = json.loads(response.content.decode('utf8'))
    total = json_response['total']
    hits = json_response['hits']
    print("Total number of jobs found is ", total['value'])

    with open('../../dev/Jobmaking/Data/AllJobsPathNew.csv', mode='a+') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['Job_ID', 'Title', 'genre', 'Arbetsgivare', 'Yrke','Beskrivning','Ort'])

        for hit in hits:
            employee_writer.writerow([hit['id'],hit['headline'] , query, hit['employer']['name'],hit['occupation']['label'],hit['headline'], hit['employer']['workplace'] ])

            cmd = 'curl -v -X POST https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Lediga%20jobb -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -H "Content-Type: application/json" --data \'{"records": [{"fields": {'
            cmd = cmd + '"Job_ID": "' + hit['id'] +'"'
            cmd = cmd + ',"Titel": "' + hit['headline'] + '"'
            cmd = cmd + ',"Yrke": "' + hit['occupation']['label'] +'"'
            cmd = cmd + ',"Beskrivning": "' + hit['description']['text_formatted'] +'"'
            cmd = cmd + ',"Ort": "' + hit['employer']['workplace'] +'"'
            cmd = cmd + ',"Arbetsgivare": "' + hit['employer']['name'] + '"}}]}\''

            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

    print("Done!")
    print( " ")


# region0 = 'Utvecklare Västernorrland Jämtland'
# test_search_loop_through_hits(region0)

# region = 'Västernorrland Jämtland'
# Yrke = {'Snickare','Kundtjänstmedarbetare','Butiksbiträde','Kock','Operatör', 'Köksbiträde','Utvecklare', 'Lärare', 'Läkare', 'Personlig assistent', 'Sjuksköterska', 'Lastbilsförare','Mäklare', 'Undersköterska' ,'Städare' }

# for yrk in Yrke:
#     query = yrk  + ' ' + region
#     print("Processing ...", query)
#     search_for_AF_Jobs(query)

postCSVJobsTo_aws_dynamodb()
