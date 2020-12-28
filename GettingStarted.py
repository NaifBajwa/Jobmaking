from MovieLens import MovieLens
from surprise import SVD
import csv
import requests
import json
import shlex
import pycurl
import subprocess

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
    # print("Total number of jobs found is ", total['value'])

    counter = 1
    with open('../../dev/Jobmaking/Data/jobPath.csv', mode='w') as jobPath:
        employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['jobId', 'title', 'genre', 'Arbetsgivare', 'application_deadline'])

        for hit in hits:
            # print(hit['headline'] ,hit['application_deadline'], hit['employer']['name'], 
            # hit['description']['requirements'], hit['description']['conditions']   )
            # hit['description']['text_formatted'], hit['description']['needs'], 
            employee_writer.writerow([counter,hit['headline'] , query, hit['employer']['name'],hit['application_deadline'] ])
            counter = counter + 1
        
    counter = 1
    with open('../../dev/Jobmaking/Data/jobRatings.csv', mode='w') as jobRatings:
        employee_writer = csv.writer(jobRatings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['userId', 'jobId', 'rating', 'genre'])
        for hit in hits:
            employee_writer.writerow([0, counter, 5, query])
            counter = counter + 1


def BuildAntiTestSetForUser(testSubject, trainset):
    fill = trainset.global_mean

    anti_testset = []
    
    u = trainset.to_inner_uid(str(testSubject))
    
    user_items = set([j for (j, _) in trainset.ur[u]])
    anti_testset += [(trainset.to_raw_uid(u), trainset.to_raw_iid(i), fill) for
                             i in trainset.all_items() if
                             i not in user_items]
    return anti_testset


# Pick an arbitrary test subject
# 34 = snickare, 50 = Utvecklare, 22 = Personlig assistent
# 30 = Sjuksköterska, 4 = Läkare, 17 = Lastbil förare
testSubject = 41

region = 'Västernorrland Jämtland'
yrke = []
userName = []
with open('./Data/usersPath.csv', newline='') as csvfile:
    usersReader = csv.reader(csvfile)
    next(usersReader)
    for row in usersReader:
        # userID = int(row[0])
        # if (testSubject == userID):
        testSubject = int(row[0])
        userName = row[1]
        yrke = row[2]

        # query = 'Personlig assistent Västernorrland'
        query = yrke + ' ' + region
        # print(query)
        test_search_loop_through_hits(query)

        ml = MovieLens()

        # print("Loading job ratings...")
        data = ml.loadMovieLensLatestSmall(testSubject)
        userRatings = ml.getUserRatings(0)
        loved = []
        hated = []
        for ratings in userRatings:
            if (float(ratings[1]) > 4.0):
                loved.append(ratings)
            if (float(ratings[1]) < 3.0):
                hated.append(ratings)

        ll = 0
        for ratings in loved:
            if ( ml.getMovieName(ratings[0]) != '' ):
                ll = ll + 1

        if (ll == 0):
            continue

        titel = ''
        Arbetsgivare = ''
        lastDate = ''
        print("\nWe recommend ", ll, " jobs for ", userName, ":\n")
        counter = 0
        for ratings in loved:
            if ( ml.getMovieName(ratings[0]) != '' and counter < 2):
                counter = counter +1
                titel = ml.getMovieName(ratings[0])
                Arbetsgivare = ml.getArbetsgivare(ratings[0])
                lastDate = ml.getLastDate(ratings[0])
                # print(ml.getMovieName(ratings[0]))

                cmd = 'curl -v -X POST https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -H "Content-Type: application/json" --data \'{"records": [{"fields": {'
                cmd = cmd + '"Name": "' + userName +'"'
                cmd = cmd + ',"Yrke": "' + yrke + '"'
                cmd = cmd + ',"Annonstitel": "' + titel +'"'
                cmd = cmd + ',"Arbetsgivare": "' + Arbetsgivare +'"'
                cmd = cmd + ',"Sista ansökningsdatum": "' + lastDate + '"}}]}\''
                # print (cmd)
                process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

        if (len(hated) > 0):
            print("\n...and didn't like these movies:")
            for ratings in hated:
                print(ml.getMovieName(ratings[0]))

        # print("\nBuilding recommendation model...")
        trainSet = data.build_full_trainset()

        algo = SVD()
        algo.fit(trainSet)

        # print("Computing recommendations...")
        testSet = BuildAntiTestSetForUser(0, trainSet)
        predictions = algo.test(testSet)

        recommendations = []

        if (len(predictions) > 0):
            print ("\nWe recommend:")
            for userID, movieID, actualRating, estimatedRating, _ in predictions:
                intMovieID = int(movieID)
                recommendations.append((intMovieID, estimatedRating))

            recommendations.sort(key=lambda x: x[0], reverse=False)

            for ratings in recommendations:
                print(ml.getMovieName(ratings[0]))


# cmd = 'curl -v -X POST https://api.airtable.com/v0/appaW3k9mZn7c7hhb/Individuell%20matchning -H "Authorization: Bearer keyHbd3ja5QEm4pVa" -H "Content-Type: application/json" --data \'{"records": [{"fields": {'
# cmd = cmd + '"Name": "' + userName +'"'
# cmd = cmd + ',"Yrke": "' + yrke + '"'
# cmd = cmd + ',"Annonstitel": "' + titel +'"'
# cmd = cmd + ',"Arbetsgivare": "' + Arbetsgivare +'"'
# cmd = cmd + ',"Sista ansökningsdatum": "' + lastDate + '"}}]}\''
# print (cmd)