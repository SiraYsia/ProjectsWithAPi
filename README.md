# YouTube API Popular Videos

This script makes a request to the YouTube Data API to retrieve the most popular videos. It then extracts the titles of those videos and prints them.

## Prerequisites

Before running the script, make sure you have the following:

- YouTube Data API key: You can obtain this key from the Google Developer Console.
- Required Python packages: requests, pandas, sqlalchemy.

## Setup

1. Clone the repository:

```
git clone <git@github.com:SiraYsia/Youtube-API.git>

 ```
2. Install the required Python packages:

```
 pip install requests pandas sqlalchemy

 ```

3. Set the environment variable for your YouTube Data API key:

- Open .bashrc file to set the variables every time the terminal restarts:

```
sudo nano ~/.bashrc

 ```

- Scroll to the bottom of the file and add the following line:
  ```
 export YOTUBE_API_KEY=[YOUR_API_KEY]
  ```

- Press Ctrl + X to exit, and when prompted to save, press Y and Enter/Return.

- Run the following command to set the environment variables for this terminal session:
  ```
 source ~/.bashrc
  ```

4. Run the script:
```
 python ytbe.py
  ```
  
## Database

The script uses an SQLite database to store the video titles. The database is created using SQLAlchemy. The table name is `table_name`, and the database file is `data_base_name.db`.


## Usage

The script fetches the most popular videos using the YouTube Data API and retrieves their titles. It then stores the titles in the database table and prints the result.

## Results

Here is an example of the retrieved video titles:

| video_title |
|-------------|
| Title 1     |
| Title 2     |
| Title 3     |
| ...         |
