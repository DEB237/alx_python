import requests

def fetch_status(url):
    """
    Fetches the status from the given URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.content)}")
    print(f"\t- content: {response.content.decode()}")