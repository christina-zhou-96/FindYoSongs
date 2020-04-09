# Find all the playlists that contain this video on Youtube.

# Try it out at https://findyosongs.herokuapp.com/

# Notes:
# You're likely to only get a hit if these are relatively well known songs.
# This is because this only works if the playlists were indexed elsewhere on the web.
# That means, if someone posted it as in their own blog or Facebook.
# Sometimes, you'll click on the video and there is no playlist, I think
# the playlist went private in that case.

# TODO: I don't think this works with a video link already in a playlist, like
# v=42ijrf02oij$list=....
# Should change backend logic to only get the string between v= and &.

from flask import Flask,redirect,request

# Create app instance.
app = Flask(__name__)

# Create homepage with form.
@app.route("/")
def home():
    return"""
    <html><body>
        <h2>Find yo songs</h2>
        <form action="/link">
            YouTube video link <input type='text' name='link'>
            <input type='submit' value='Go'>
        </form>
    </body></html>
    """

# Backend logic to redirect user to the new Google page.
@app.route("/link")
def link():

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

# Run app.
if __name__ == "__main__":
    app.run()

# Resources:

# Local app
# 1. Make a Flask app
# https://runestone.academy/runestone/books/published/thinkcspy/WebApps/07-InputForAFlaskWebApplication.html

# 2. The idea
# This is a tip from user Ruben on stack overflow
# https://webapps.stackexchange.com/questions/44215/how-can-i-view-what-playlist-if-any-a-youtube-video-is-in

# Deployment
# 3. Overview to deploy with Heroku
# which sounds cuter and easier than Amazon or Google
# https://pythonhow.com/deploying-your-web-application-to-the-cloud/

# 4. Generating a requirements file
# https://stackoverflow.com/questions/40192651/django-pip-freeze-results-in-empty-file

# 5. The official Windows help
# Notice the special Windows procfile...
# https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

# 6. Make a Procfile with Waitress
# https://books.google.com/books?id=cVlPDwAAQBAJ&pg=PT282&lpg=PT282&dq=%22waitress%22+procfile&source=bl&ots=xNJYeoYq9_&sig=ACfU3U1aUYxH6Zjxy5pi-jXDJdf4CZF_2w&hl=en&sa=X&ved=2ahUKEwioxOPcitzoAhWCl3IEHSGsAwoQ6AEwBnoECAkQKQ#v=onepage&q=%22waitress%22%20procfile&f=false
# If you're on Windows, you can't use gunicorn, which is what the tutorial
# wants you to use. (The tutorial does have an example Windows procfile, but
# that's only applicable for local use.)

