import sys
import requests

if __name__ == "__main__":
    """
    GitHub API - Retrieve User ID
    
    This script uses the GitHub API to retrieve the user ID for a given GitHub account. It takes in the username and personal access token as arguments and makes a GET request to the GitHub API endpoint.

    Args:
        username (str): GitHub username.
        password (str): Personal access token as the password.

    Returns:
        None: If the request is unsuccessful or the user ID is not found.
        int: The user ID if the request is successful.

    Requires:
        - The requests library.
    """

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        data = response.json()
        print(data["id"])
    else:
        print("None")