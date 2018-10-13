#import webbrowser file for use it when click on movie poster to run the trailer 
import webbrowser

#create class in this module to use the arguments in entertainment center file 
class Movie():

#first function use init is mean this override to use the arguments
#self mean it use for varibles
    def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#show trailer function creat it with webbrowser for run the movie url link in screen page      
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
