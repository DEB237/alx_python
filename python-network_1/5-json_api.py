'''
This module contains a function
'''

import sys
import requests

if __name__ == "__main__":
    """
    Search User API Script
    
    This script sends a POST request to the Search API with a letter as a parameter. 
    It retrieves the JSON response and prints the ID and name if available, 
    or displays appropriate messages if the JSON is invalid or empty.
    """

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    
    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": letter}

    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
