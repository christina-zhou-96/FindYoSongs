# This stuff is basically copy pasted off the 2017 python snippet in the
# GitHub repo for python to Google.

# Replace CREDENTIALS_FILE with a text file with your
# own developer key, see Resources for more.

from googleapiclient.discovery import build

# Connect to Youtube API
CREDENTIALS_FILE = r'D:\youtube_api_key.txt'

file = open(CREDENTIALS_FILE,
            mode='r')

DEVELOPER_KEY = file.read()

file.close()

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

# Run a search for videos
# YouTube.Search.list('snippet['thumbnails']['url']', {q: '<query>'})

# Select the top video
# search[0]

# Select the top video's URL
# video.snippet.thumbnails.(key).url
# Return the URL