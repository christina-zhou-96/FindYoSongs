# Find all the playlists that contain this video on Youtube.

# Notes:
# This only works if the playlists were indexed elsewhere on the web.
# That means, if someone posted it as in their own blog or Facebook.
# Sometimes, you'll click on the video and there is no playlist, I think
# the playlist went private in that case.

# Instructions:

# 1. Go to localhost:5000
# 2. Add /?link= to start a link parameter
# 3. Copy your youtube link after that.

from flask import Flask,redirect,request

app = Flask(__name__)

@app.route("/")
def my_redirect():

    # Get the link from user.

    link = request.args['link']

    # Find the video ID.
    # Current business rule: video ID is between v= and &

    video_id = link.partition("v=")[2]

    # Relink to the Google search.
    # Current business rule: looks like site:youtube.com inurl(2jopgOD + list)

    google_search_base_url = "https://www.google.com/"
    google_search_param = "search?q="

    def youtube_search_builder(video_id):
        return f'site%3Ayoutube.com+inurl%3A({video_id}+list)'

    final_link = google_search_base_url + \
                 google_search_param + \
                 youtube_search_builder(video_id)

    return redirect(final_link)

if __name__ == "__main__":
    app.run()

# This is a tip from user Ruben on stack overflow
# https://webapps.stackexchange.com/questions/44215/how-can-i-view-what-playlist-if-any-a-youtube-video-is-in