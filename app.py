from flask import Flask,redirect

app = Flask(__name__)

@app.route("/")
def my_redirect():
    video_id = 'QuqCMHe4kxQ'
    return redirect(f"https://www.google.com/search?q=site%3Ayoutube.com+inurl%3A({video_id}+list)")

if __name__ == "__main__":
    app.run(debug=True)

# This is a tip from user Ruben on stack overflow
# https://webapps.stackexchange.com/questions/44215/how-can-i-view-what-playlist-if-any-a-youtube-video-is-in