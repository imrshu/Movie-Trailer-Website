import webbrowser
import os

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 120px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 2;
            background-color: white;
        }
        .scale-media h2 {
            background-color: #00d4ca;
            margin:0;
            font-size: 20px;
        }
    </style>
    <script>
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });

        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            // Fetching the value of trailer-youtube-link data attribute
            var trailerYouTubelink = $(this).attr('trailer-youtube-link');

            // Fetching the value of movie_likes data attribute
            var movie_likes = $(this).attr('movie_likes');

            // Appending an IFrame tag with its content filled in
            $("#trailer-video-container").append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': trailerYouTubelink,
              'frameborder': 0
            }));

            // Prepending movie_likes before IFrame tag
            $('#trailer-video-container').prepend('<h2>Trailer Likes- '+movie_likes+'</h2>');
        });

        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailer Site</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" trailer-youtube-link="{trailer_youtube_id}" movie_likes="{movie_likes}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <h3>{movie_release_date}</h3>
    <h4>{movie_trailer_time}</h4>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''

    for movie in movies:
        # Append the template for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.movie_title,
            poster_image_url=movie.movie_poster,
            trailer_youtube_id=movie.movie_trailer_url,
            movie_likes= movie.movie_likes,
            movie_release_date= movie.movie_release_date,
            movie_trailer_time= movie.movie_trailer_time
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (Also in a new tab)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
