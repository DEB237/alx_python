'''
This module contains a function
'''

import sys
import requests

if len(sys.argv) == 1:
    letter = ""
else:
    letter = sys.argv[1]

parameter = {'q':letter}
url = 'http://0.0.0.0:5000/search_user'
response = requests.post(url, data=parameter)

try:
    if response.json():
            print("[{}] {}".format(response.json()['id'], response.json()['name']))
    else:
        print("No result")
except:
    print("Not a valid JSON")
