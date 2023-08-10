'''
This module contains a function
'''

import requests
import sys

def post_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter
    and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter in the request.

    Returns:
        None
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(f"Your email is: {email}")
    print("Response body:")
    print(response.text)

# Check if a URL and email address are provided as command-line arguments
if len(sys.argv) > 2:
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
else:
    print("Please provide a URL and an email address as command-line arguments.")
