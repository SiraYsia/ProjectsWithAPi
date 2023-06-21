import requests

response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json')
item_ids = response.json()

item_id = item_ids[0] 
response = requests. get(f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json')
story = response.json()

title = story['title']
author = story['by']
link = story['url']

print('Title:', title)
print('Author:', author)
print('Link:', link)


