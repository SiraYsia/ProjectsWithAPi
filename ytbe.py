import requests
import json

url = 'https://www.googleapis.com/youtube/v3/videos'
params = {
    'part': 'snippet',
    'chart': 'mostPopular',
    'key': 'AIzaSyDbkW3MTT4vkSL2XOGfezAwR_WJLVhV0O8'  # Replace with your YouTube API key
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

