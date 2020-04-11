Find all the playlists that contain this video on Youtube. <br>

Try it out at <b> https://findyosongs.herokuapp.com/ </b> <br>

<b>
Notes
</b>

<br>

You're likely to only get a hit if these are relatively well known songs. 
This is because this only works if the playlists were indexed elsewhere on the web.
That means, if someone posted it as in their own blog or Facebook.
Sometimes, you'll click on the video and there is no playlist, I think the playlist went private in that case.

<br>

<b>
Resources
</b>

<br>

Local app <br>
1. Make a Flask app <br>
https://runestone.academy/runestone/books/published/thinkcspy/WebApps/07-InputForAFlaskWebApplication.html <br>

2. The idea <br>
This is a tip from user Ruben on stack overflow <br>
https://webapps.stackexchange.com/questions/44215/how-can-i-view-what-playlist-if-any-a-youtube-video-is-in <br>

Deployment <br>
3. Overview to deploy with Heroku <br>
which sounds cuter and easier than Amazon or Google <br>
https://pythonhow.com/deploying-your-web-application-to-the-cloud/ <br>

4. Generating a requirements file <br>
https://stackoverflow.com/questions/40192651/django-pip-freeze-results-in-empty-file <br>

5. The official Windows help <br>
Notice the special Windows procfile... <br>
https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app <br>

6. Make a Procfile with Waitress <br>
https://books.google.com/books?id=cVlPDwAAQBAJ&pg=PT282&lpg=PT282&dq=%22waitress%22+procfile&source=bl&ots=xNJYeoYq9_&sig=ACfU3U1aUYxH6Zjxy5pi-jXDJdf4CZF_2w&hl=en&sa=X&ved=2ahUKEwioxOPcitzoAhWCl3IEHSGsAwoQ6AEwBnoECAkQKQ#v=onepage&q=%22waitress%22%20procfile&f=false
<br> If you're on Windows, you can't use gunicorn, which is what the tutorial
wants you to use. (The tutorial does have an example Windows procfile, but
that's only applicable for local use.) <br>

Connect to Youtube <br>
7. Overview of steps to use Youtube API <br>
https://developers.google.com/youtube/v3/getting-started <br>

8. python Youtube connection <br>
https://github.com/youtube/api-samples/tree/master/python <br>

9. The data structure of a video <br>
https://developers.google.com/youtube/v3/docs/videos#resource<br>

<b>Contributions</b> <br>

It would be great if we could nix the step of going to Youtube altogether.
For instance, looking for "Hit Me Baby One More Time", instead of
writing that into Youtube and then copying the link over, we should
just be able to search "Hit Me Baby One More Time" straight into this
site and get the results with one click (guessing that the user meant
the first video - more work but also could do a constantly refreshing
preview where all video images are previewed and user selects the one
they want).