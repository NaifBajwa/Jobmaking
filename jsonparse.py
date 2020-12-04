# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:55:41 2020

@author: Naif Bajwa
"""

import json 

  
# Opening JSON file 
f = open('2006.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in range(0, 10) : 
    print(data[i]['application_details']) 
    print(data[i]['description']['text'])
    print(data[i]['driving_license_required'])
    print(data[i]['duration']['label'])
    print(data[i]['employer']['name'])
    print(data[i]['headline'])
    print(data[i]['experience_required'])
    print(data[i]['must_have']['languages'])
    print(data[i]['must_have']['skills'])
    print(data[i]['must_have']['work_experiences'])
    print('\n')
    
  
# Closing file 
f.close() 