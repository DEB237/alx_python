"""
 Python script that takes in a URL and an email address
"""
import sys
import requests

url = sys.argv[1]
email = sys.argv[2]
parameter = {'email':email}

response = requests.post(url, params=parameter)
print("Email:",parameter['email'])
