#Makes a request to the YouTube Data API to 
#retrieve the most popular videos. It then 
#extracts the titles of those videos and prints them.
import requests
import pandas as pd
import sqlalchemy as db
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
video_titles = [item['snippet']['title'] for item in data['items']]


data_frame = pd.DataFrame({'video_title': video_titles})
engine = db.create_engine('sqlite:///data_base_name.db')
data_frame.to_sql('table_name', con=engine, if_exists='replace', index=False)


with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM table_name;")).fetchall()
    print(pd.DataFrame(query_result))