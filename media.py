# importing webbrowser module
import webbrowser


class Movie():
    """ Class Movie initialzes 5 Movie object variables - title, storyline,
        poster_image_url, trailer_youtube_url and release_date """

    def __init__(self, title, storyline, poster, trailer, release_date):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        self.release_date = release_date

    def show_trailer(self):
        """ Function to open youtube URL in webbowser """
        webbrowser.open(self.trailer)
