import unittest
import pandas as pd
from ytbe import extract_video_titles, save_video_titles_tod_database, retrieve_from_database
from ytbe import (
    extract_video_titles,
    save_video_titles_to_database,
    retrieve_from_database
)


class TestYouTubeAPI(unittest.TestCase):
    def test_extract_video_titles(self):
        # Mock data for testing
        data = {'items': [
            {'snippet': {'title': 'Video 1'}},
            {'snippet': {'title': 'Video 2'}},
            {'snippet': {'title': 'Video 3'}}
        ]}

        # Test the extracting of video titles 
        # Test the extracting of video titles
        video_titles = extract_video_titles(data)
        expected_titles = ['Video 1', 'Video 2', 'Video 3']
        self.assertEqual(video_titles, expected_titles)

    def test_retrieve_from_database(self):
    # Prepare the test data in the database
      db_name = 'test_db.db'
      table_name = 'test_table'
      video_titles = ['Title 1', 'Title 2', 'Title 3']
      save_video_titles_tod_database(video_titles, db_name)
    
    # Test retrieving data from the database
      retrieved_data = retrieve_from_database(db_name)
      expected_data = pd.DataFrame({'video_title': video_titles})
      self.assertTrue(retrieved_data.equals(expected_data))
        # Prepare the test data in the database
        db_name = 'test_db'
        table_name = 'test_table'
        video_titles = ['Title 1', 'Title 2', 'Title 3']
        save_video_titles_to_database(video_titles, db_name)

        # Test retrieving data from the database
        retrieved_data = retrieve_from_database(db_name)
        expected_data = pd.DataFrame({'video_title': video_titles})
        self.assertTrue(retrieved_data.equals(expected_data))


if __name__ == '__main__':
    unittest.main()
