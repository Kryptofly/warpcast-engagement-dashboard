import requests
from config import WARPCAST_API_TOKEN, WARPCAST_API_ENDPOINT

def fetch_user_interactions(username):
    url = f"{WARPCAST_API_ENDPOINT}/users/{username}/interactions"
    headers = {
        'Authorization': f'Bearer {WARPCAST_API_TOKEN}'
    }
    response = requests.get(url, headers=headers)
    return response.json().get('data', [])
