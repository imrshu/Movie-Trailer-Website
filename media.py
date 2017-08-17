class Movie():
    ''' This Class Represents My Favourite Movies '''

    def __init__(self,movie_poster,movie_trailer_url):
        self.movie_poster = movie_poster
        self.movie_trailer_url = movie_trailer_url

class MovieExtras():
    ''' This Class Represents Some Extra Info About My Favourite Movies '''

    def __init__(self,movie_likes,movie_release_date):
        self.movie_likes = movie_likes
        self.movie_release_date = movie_release_date

class Video(Movie,MovieExtras):
    ''' This Class Represents Movie Title & Movie Trailer Duration & Also Inherits Properties
    from Movie and MovieExtras Classes'''

    def __init__(self,movie_poster,movie_trailer_url,movie_likes,movie_release_date,movie_title,movie_trailer_time):
        Movie.__init__(self,movie_poster,movie_trailer_url)
        MovieExtras.__init__(self,movie_likes,movie_release_date)
        self.movie_title = movie_title
        self.movie_trailer_time = movie_trailer_time

