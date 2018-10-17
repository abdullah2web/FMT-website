# import fresh_tomatoes file to run the list of movies in html page
# import media file to use the classes init to run the arguments in Movie
import fresh_tomatoes
import media

""" each movie put in variables
then use the Movie class in media file to send the arguments.
we wrote 6 favorite movies and put it in variables below: """

toy_story = media.Movie(
    "Toy Story",
    "A Story of a boy and his toys that comes to live",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie(
    "School of Rock",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie(
 "Midnight in Paris",
 "Storyline",
 "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
 "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie(
    "Hunger Games",
    "Storyline",
    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")

# put the variable movies in array to run with function named open_movies_page

movies = [
        toy_story,
        avatar,
        school_of_rock,
        ratatouille,
        midnight_in_paris,
        hunger_games]

fresh_tomatoes.open_movies_page(movies)
