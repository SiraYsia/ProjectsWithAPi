import requests
import json
import config

url = 'https://www.googleapis.com/youtube/v3/videos'
api_key = config.API_KEY

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
