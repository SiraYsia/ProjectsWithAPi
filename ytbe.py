import requests
import pandas as pd
import sqlalchemy as db
import os


def makee_youtube_api_requests():
    url = 'https://www.googleapis.com/youtube/v3/videos'
    api_key = os.environ.get('YOTUBE_API_KEY')

    params = {
        'part': 'snippet',
        'chart': 'mostPopular',
        'key': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data


def extract_video_titles(data):
    video_titles = [item['snippet']['title'] for item in data['items']]
    return video_titles


def save_video_titles_to_database(video_titles, data_base_name):
    data_frame = pd.DataFrame({'video_title': video_titles})
    engine = db.create_engine('sqlite:///data_base_name.db')
    data_frame.to_sql(
        'table_name',
        con=engine,
        if_exists='replace',
        index=False
    )


def retrieve_from_database(data_base_name):
    engine = db.create_engine('sqlite:///data_base_name.db')
    with engine.connect() as connection:
        query = "SELECT * FROM table_name;"
        query_result = connection.execute(db.text(query)).fetchall()
        return pd.DataFrame(query_result)


data = makee_youtube_api_requests()
video_titles = extract_video_titles(data)
save_video_titles_to_database(video_titles, 'data_base_name.db')


retrieve_titles = retrieve_from_database('data_base_name.db')
print(retrieve_titles)
