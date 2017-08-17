from media import Video
import fresh_tomatoes

# First Instance of Video Class
tarzan = Video("https://goo.gl/mG0EVP",
    "http://www.youtube.com/embed/2Lhoy5R4xp4?autoplay=1&html5=1",
    "638","6 August 2004","Tarzan Car","0.29s")

# Second Instance of Video Class
raees = Video("https://goo.gl/71xC9D",
    "http://www.youtube.com/embed/J7_1MU3gDk0?autoplay=1&html5=1",
    "437K","25 January 2017","Raees","2.46min")

# Third Instance of Video Class
hindi = Video("https://goo.gl/6eeoCy",
    "http://www.youtube.com/embed/GjkFr48jk68?autoplay=1&html5=1",
    "125K","19 May 2017","Hindi Medium","2.42min")

# Creating an list of the Video Class Instances
movies_list = [tarzan,raees,hindi]

# Passing the movie_list to open_movies_page function present in fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies_list)