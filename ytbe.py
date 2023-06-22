#Makes a request to the YouTube Data API to 
#retrieve the most popular videos. It then 
#extracts the titles of those videos and prints them.

import requests
import json
import os

url = 'https://www.googleapis.com/youtube/v3/videos'
api_key = os.environ.get('YOTUBE_API_KEY')

params = {
    'part': 'snippet',
    'chart': 'mostPopular',
    'key': api_key
}

response = requests.get(url, params=params)
data = response.json()

if 'error' in data:
    print(f"Error: {data['error']['message']}")
else:
    items = data.get('items', [])
    for item in items:
        snippet = item.get('snippet', {})
        title = snippet.get('title')
        print(title)