
import media
import fresh_tomatoes

# the above uses the code in python files media and fresh_tomatoes

# toy_story is an instance of the class Movie
toy_story = media.Movie("Toy Story",
                        "A story of a boy",
                        "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# avatar is an instance of the class Movie
avatar = media.Movie("Avatar",
	                 "A story of a virtual forest",
	                 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	                 "https://www.youtube.com/watch?v=5PSNL1qE6VY")


despicable_me = media.Movie("Despicable Me",
	                        "A story about minions",
	                        "https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg",
	                        "https://www.youtube.com/watch?v=hknYz5IvOHs")

alexander = media.Movie("Alexander and the Terrible, Horrible, No Good, Very Bad Day",
	                    "A story of a boy and his family",
	                    "https://upload.wikimedia.org/wikipedia/en/5/5f/Alexander_and_the_Terrible%2C_Horrible%2C_No_Good%2C_Very_Bad_Day_poster.jpg",
	                    "https://www.youtube.com/watch?v=Z_dideF5qvk")

nemo = media.Movie("Finding Nemo",
	               "A story about a fish in the ocean",
	               "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
	               "https://www.youtube.com/watch?v=yDPRaVX2p8c")

big_hero = media.Movie("Big Hero",
                       "A story about a young robotics prodigy",
                       "https://upload.wikimedia.org/wikipedia/en/4/4b/Big_Hero_6_%28film%29_poster.jpg",
                       "https://www.youtube.com/watch?v=z3biFxZIJOQ")

# print (toy_story.storyline)
# toy_story.show_trailer()

# print (avatar.storyline)
# avatar.show_trailer()

# print (despicable_me.storyline)
# despicable_me.show_trailer()

# print (alexander.storyline)
# alexander.show_trailer()

# print (nemo.storyline)
# nemo.show_trailer()

# print (big_hero.storyline)
# big_hero.show_trailer()

# All of the instances of the class Movie are grouped together in a list
movies = [toy_story, avatar, despicable_me, alexander, nemo, big_hero]

# This function will generate a HTML page in the browser
# The input to this function is the class Movie and its instance variables
# The output of this function will display all of the instances of the class Movie on a HTML page
fresh_tomatoes.open_movies_page(movies)
 
