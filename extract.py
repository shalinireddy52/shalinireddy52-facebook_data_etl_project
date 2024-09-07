# scripts/extract.py
import requests
from config import ACCESS_TOKEN, BASE_URL

def get_facebook_page_data(page_id):
    url = f"{BASE_URL}/{page_id}/posts?access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
