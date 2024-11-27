# Stage 2 Project - Create a fill in the blanks quiz

# Create lists with the number of questions stored as strings
number_of_questions_in_easy = ["1", "2", "3", "4", "5"]
number_of_questions_in_medium = ["1", "2", "3", "4"]
number_of_questions_in_hard = ["1", "2", "3", "4"]

# Create lists with all of the answers
easy_answers = ['CATHERINE', 'SAIL', 'BOATS', 'ENGINEER', 'ATT']
medium_answers = ['BEAUTIFUL', 'BOATS', 'ENGINEER', 'SAIL']
hard_answers = ['BEAUTIFUL', 'ENGINEER', 'SAIL', 'OCEAN']

# Create the test strings to pass in to the rev_mad_lib function.
easy_string = "Hi my name is __1__ and I really like to __2__ __3__. I'm also an __4__ at __5__."
medium_string = "What am I going to do with all these __1__ __2__? Only a registered __3__ could __4__ them."""
hard_string = "What a __1__ day! I can take the day off from being an __2__ and go __3__ on the __4__."
# Create a blank list for all the blanks in the string
blank_list = ["__1__", "__2__", "__3__", "__4__", "__5__"]

# Create an input for the game difficulty
game_difficulty = raw_input('Please select a game difficulty by typing it in! Possible choices include easy, medium, and hard.')

print "You've chosen " + game_difficulty + "!"

# Create all of the user input options for each level of game difficulty
easy_list = ["easy", "Easy", "EASY", "EAsy", "EASy"]
medium_list = ["medium", "Medium", "MEDIUM", "MEdium", "MEDium", "MEDIum", "MEDIUm"]
hard_list = ["hard", "Hard", "HARD", "HArd", "HARd"]

# Create a function for the game difficulty with the acceptable user inputs as input and the output as the lowercase conversion of the acceptable user input for each difficulty level


def menu_function(game_difficulty):
    if game_difficulty in easy_list or game_difficulty in medium_list or game_difficulty in hard_list:
        return game_difficulty.lower()
    else:
        return 'Not valid'

if menu_function(game_difficulty) == "easy":
        string = easy_string
        number_of_questions = number_of_questions_in_easy
        answers = easy_answers
elif menu_function(game_difficulty) == "medium":
        string = medium_string
        number_of_questions = number_of_questions_in_medium
        answers = medium_answers
elif menu_function(game_difficulty) == "hard":
        string = hard_string
        number_of_questions = number_of_questions_in_hard
        answers = hard_answers

# Create a play game function with the inputs including the string, number of questions in each
# string, and the answers in each string. The game player will have no more than three tries at 
# guessing each answer


def play_game(string, number_of_questions, answers):
    i = 0
    n = 1
    print "The current paragraph reads as such: " + string
    while i < len(number_of_questions):
        print "What is the answer for question #", n
        current_answer = raw_input("My answer is: ")
        tries = 0
        while current_answer!=answers[i] and tries<3:
            current_answer=raw_input("Try again. Enter the correct answer: ") 
            tries = tries+1
            if tries == 3:
               print "The correct answer is " + answers[i]
        string=string.replace(blank_list[i], answers[i])
        print string
        n = n+1
        i = i+1     

print play_game(string, number_of_questions, answers)     

#UDACITY FEEDBACK

#PYTHON STYLE GUIDE
#https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements 

#Please note that "level selector" code piece should be implemented at the end of the file (main code block), or even better into a dedicated function.

#In order to get an easy to read and easy to understand code, it is recommended writing your code following a structured schema, e.g:
#1.- importing block section
#2.- constants definition / initialization
#3.- classes and functions definition
#4.- main code block

#The typical Python file would be something like this:

# This code file is for (whatever information you need to explain about the file)
#import some modules
#import other modules

#constant_1 = some_value
#constant_2 = [some, list, ...]

#def function_one(some, parameters):
#   """
#    docstring explaining the function...
#   """
  #  function code block
 #   return some, values

#def function_two(some, arguments):
#Here is the main code block, the code that is executed immediately after invoking 
#the program
#if __name__ == "__main__":
  #  print "Some starting message..."
#    function_one(some, params)
#

#(end of file)

#Please, note that some code lines are longer than maximum length specified in the Style Guide for Python Code (about 79 chars), this issue makes your code a bit difficult to read because readers need to scroll horizontally to reach the end of the line. Here you could find some useful information
#Developer to developer tip: Before submitting any project, it is a common practice to pass your codes (even those that were provided to you) to make sure your code adheres to PEP8, the Style Guide for Python Code (https://www.python.org/dev/peps/pep-0008/). You can pass your code through the online PEP8 checker at http://pep8online.com/ or look for available plug-ins for popular editor such as Sublime, Textmate or Vim.

#PS: Recommended video about PEP8:

#https://www.youtube.com/watch?v=wf-BqAjZb8M