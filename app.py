from flask import Flask,redirect,request
from youtube import find_video

# Create app instance.
app = Flask(__name__)

# Create homepage with form.
@app.route("/")
def home():
    return"""
    <html><body>
        <h2>Find yo songs</h2>
        <form action="/query">
            Your song and artist <input type='text' name='query'>
            <input type='submit' value='Go'>
        </form>
        
        <br>
        
        <form action="/about">
            <input type='submit' value='About'>
        </form>
    </body></html>
    """

# Create about page.
@app.route("/about")
def about():
    return"""
    <html><body>
        <b>Have you ever really liked a song</b>, but not because of its genre, just because it's good?
        <br>
        <br>        
        I have trouble finding similar songs; algorithms don't do the trick.
        <br>
        <br>
        I'd rather find what other people like me enjoyed!
        <br>
        <br>
        This search seeks out public playlists on Youtube that contain your desired song.
        <br>
        <br>
        You can get a lot of interesting finds this way...
        <br>
        <br>
        Try it out!
        <br>
        <br>
        <br>
        <b>Stuck?</b>
        <br>
        <br>
        Try one of these searches:
        <br>
        <br>
        when youre gone
        <br>
        <br>
        316 all about you
        <br>
        <br>
        forever young alphaville
        <br>
        <br>
        the kill 30 seconds to mars
        <br>
        <br>
        <br>
        <b>
        <a href="https://github.com/christina-zhou-96/FindYoSongs">Code</a>
        </b>
    </body></html>
    """

# Backend logic to redirect user to the new Google page.
@app.route("/query")
def link():

    # Get the query from user.

    query = request.args['query']

    # Find the video ID.
    # Uses Youtube API.
    video_id = find_video(query)

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
    app.run(debug=True)

