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

region = 'Västernorrland Jämtland'


def test_search_loop_through_hits(query):
    # From the jobs get the genre
    with open('Data/usersPath.csv', newline='') as csvfile:
        ratingReader = csv.reader(csvfile)
        next(ratingReader)

        with open('Data/userJOBPath.csv', mode='w') as jobPath:
            employee_writer = csv.writer(jobPath, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(['userId', 'Namn', 'Yrke'])

            for row in ratingReader:
                grName = row[2] + ' ' + region
                print(grName, query)
                if (grName == query):
                    employee_writer.writerow([ row[0],row[1],row[2] ])
        
        with open('Data/userJOBRatings.csv', mode='w') as jobRatings:
            employee_writer = csv.writer(jobRatings, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            employee_writer.writerow(['jobId', 'userId', 'rating', 'genre'])

            for row in ratingReader:
                grName = int(row[2])
                if (grName == query):
                    employee_writer.writerow([0, row[0], 5, query])


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
testSubject = 24435258

yrke = []
userName = []
with open('./Data/AllJobsPath.csv', newline='') as csvfile:
    jobsReader = csv.reader(csvfile)
    next(jobsReader)
    for row in jobsReader:
        # jobID = int(row[0])
        # if (testSubject == jobID):
        testSubject = int(row[0])
        jobTetle = row[1]
        yrke = row[2]

        # query = 'Personlig assistent Västernorrland'
        query = yrke
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
        for ratings in loved:
            if ( ml.getMovieName(ratings[0]) != '' ):
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
                print (cmd)
                # process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                # stdout, stderr = process.communicate()

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