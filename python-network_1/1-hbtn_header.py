'''
This module contains a function
'''

import requests
import sys

def get_request_id(url):
    """
    Sends a request to the given URL and displays the value of the 'X-Request-Id' header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')

    if request_id:
        print(f"The value of the 'X-Request-Id' header is: {request_id}")
    else:
        print("The 'X-Request-Id' header is not present in the response.")

# Check if a URL is provided as a command-line argument
if len(sys.argv) > 1:
    url = sys.argv[1]
    get_request_id(url)
else:
    print("Please provide a URL as a command-line argument.")
