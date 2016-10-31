# importing webbrowser module
import webbrowser


# Class Movie initialzes 5 Movie object variables - title, storyline,
# poster_image_url, trailer_youtube_url and release_date
class Movie():

    def __init__(self, title, storyline, poster, trailer, release_date):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.release_date = release_date

# Function to open youtube URL in webbowser
    def show_trailer(self):
        webbrowser.open(self.trailer)
