# This stuff is basically copy pasted off the 2017 python snippet in the
# GitHub repo for python to Google.

# Replace CREDENTIALS_FILE with a text file with your
# own developer key, see Resources for more.

from googleapiclient.discovery import build

# Data structures
CREDENTIALS_FILE = r'D:\youtube_api_key.txt'

DEVELOPER_KEY = None
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Connect to Youtube API
def _build_youtube_instance():

    file = open(CREDENTIALS_FILE,
                mode='r')
    DEVELOPER_KEY = file.read()
    file.close()

    youtube = build(YOUTUBE_API_SERVICE_NAME,
                    YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    return youtube

# Run a search for videos
def _search_videos(youtube):
    search_response = youtube.search().list(
        part='snippet',
        maxResults=1
    ).execute()

    return search_response

# Select the top video's ID
def _top_id(search_response):

    # Select the top video
    video = search_response.get('items', [])[0]

    # Select the top video's ID
    id = video['id']['videoId']

    # Return the ID
    return id

# Outer function
def youtube_connector():

    youtube = _build_youtube_instance()

    search_response = _search_videos(youtube)

    return _top_id(search_response)