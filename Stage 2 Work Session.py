# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here  hours_in_7_weeks = 24*7*7

hoursInADay = 24
hoursInAWeek = hoursInADay * 7
hoursIn7Weeks = hoursInAWeek * 7

print hoursIn7Weeks
#
#
s="udacity"
t="bobacious"
print s[0] + s[1] + s[2] + t[4:]

# Insert the proper slicing indices for the substring variable 
# so that the slice is a string that contains everything after "A NOUN". 
# For example, if we wanted to store everything after "went", the returned 
# string would be equal to sentence[11:].

sentence = "A NOUN went on a walk."
substring = sentence[:]
print sentence[6: ]

# Use string slicing to store everything before "NOUN" in substring1,
# everything after "NOUN" and before "VERB" in substring2, and everything after "VERB" 
# in substring3.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[ :2]
substring2 = sentence[6:29]
substring3 = sentence[34: ]
print substring1 + substring2 + substring3

# Set noun_replacement and verb_replacement to your own noun and verb strings. 
# Then, concatenate the variables substring1-3, noun_replacement, and 
# verb_replacement and assign the result to the variable new_sentence so that 
# it's in the same order as the variable sentence.

sentence = "A NOUN went on a walk. It can VERB really fast."
substring1 = sentence[0:2]
substring2 = sentence[6:30]
substring3 = sentence[34:]

noun_replacement = "NOUN" # your noun here
verb_replacement = "VERB" # your verb here

# your code here
new_sentence = substring1 + noun_replacement + substring2 + verb_replacement + substring3
# your code here
print new_sentence

# Mary is a world class spy with different aliases across the world.

# Mary is known as Randa in America. 
# But in Europe, her alias Randa has another alias known as Katie.
# In Asia, the alias Katie has another alias known as Salwa.
# In Australia, the alias Salwa is known as Kathleen.
# In South America, the alias Kathleen is known as the alias Gabriel.

# You're a spy yourself and you want to be able to print the real name associated with
# all of these alias names to keep track of Mary, but you only know that 
# gabriel = kathleen, and kathleen = salwa, etc..

# Your mission: knowing how each alias relates to each other, assign the variables 
# gabriel, kathleen, salwa, katie, and randa to each other so whenever we print any alias,
# the values for each alias will point to the string "Mary"

# NOTE: We can't simply assign all variables to "Mary".

mary = "Mary"
# Your code goes here
randa = mary
katie = randa
salwa = katie 
kathleen = salwa 
gabriel = kathleen 
print gabriel
print kathleen
print salwa
print katie
print randa

# Use the string.find method to locate "NOUN" and "VERB" in the string text
# and store those positions in the variables noun_position and verb_position respectively.
# Review Dave's video on string.find at https://goo.gl/Pde1nZ or visit
# http://www.tutorialspoint.com/python/string_find.htm for more information.

text = """Wow this is a fairly long body of text. Quite a few characters too.
I wonder if the string.find method could help find where NOUN is located.
That way, I could go out and VERB with my friends rather than counting characters
all day long!"""
print text.find("NOUN")
print text.find("VERB")

noun_position = text.find("NOUN")
verb_position = text.find("VERB")
print noun_position
print verb_position

# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# The Python code should be general enough
# to pass every possible case where 'zip' 
# can occur in a string

# Here are two example test cases:
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

print text.find("zip",text.find("zip")+1)

# Let's go over another string method: string.replace. Use this method
# to replace the instance of NOUN with "duck" and VERB with "waddle" in the string
# sentence. For more information, visit http://www.tutorialspoint.com/python/string_replace.htm.

sentence = "A NOUN went on a walk. They can VERB really well."
sentence1 = sentence.replace("NOUN","duck")
sentence2 = sentence1.replace("VERB", "waddle")
print sentence2

# Read through the code below. Even if you don't understand it, try to make 
# a guess about what it does. What do you think will happen when you press 
# "Test Run"? Once you have a prediction, press "Test Run" and compare what 
# happens to what you predicted.

def say_hello():
    return "Hello!"

print say_hello()

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing. 

# Continue to the next example to see a more interesting version of say_hello.

# Once again, say_hello is a function (AKA procedure). But this time, it DOESN'T
# do the same thing every time. 
#
# Read through the code and try to predict what the output will be when 
# you press "Test Run"

def say_hello(name):
    greeting = "Hello " + name + "!"
    return greeting

print say_hello("Miriam")
print say_hello("Andy")

def say_hello(name):
    greeting = "Hello " + name + '!'
    return greeting

# In the previous example, you saw code that looked like what you see above.
# Look at the first line. In that line, 'name' is a "parameter"
# of the function say_hello

# In the code below, the add_two_numbers function has two parameters.
# What do you think will happen when you press "Test Run"?
# Make a prediction and then press "Test Run"
def add_two_numbers(number_1, number_2):
    return number_1 + number_2

print add_two_numbers(4, 3)
print add_two_numbers(2, 6)
print add_two_numbers(0, 9)

# Once you've pressed Test Run, remove the comment characters from the 
# code below and then make ONE modification so that the function does 
# what the name says it should do.

def subtract_two_numbers(number_1, number_2):
   return number_1 - number_2

print subtract_two_numbers(4, 3)

#How do functions take input and produce output and what role do
#the keywords def and return have to do with this process?

# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

# Read through the code below. Even if you don't understand it, try to make 
# a guess about what it does. What do you think will happen when you press 
# "Test Run"? Once you have a prediction, press "Test Run" and compare what 
# happens to what you predicted.

def say_hello():
    return "Hello!"

print say_hello()

# say_hello is a function. Or, as Dave would call it, a procedure.
# This procedure isn't particularly interesting because it only does
# one thing. 

# Continue to the next example to see a more interesting version of say_hello.

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here
def sum(a, b):
	a=a+b
	return a
	
print sum (1, 2)

# Define a procedure, square, that takes one number 
# as its input, and returns the square of that 
# number (result of multiplying
# the number by itself).
# To help you out, the code for sum(a,b) is below.

def square(a):
    c = a*a
    return c

print square(5)

x=25
y=square(x)

print y

print square(y)

print square(square(y))

#the abovbe is called procedure composition

# Define a procedure, sum3, that takes three
# inputs, and returns the sum of the three
# input numbers.
# To help you out, the code for sum(a,b) is below.

def sum3(a,b,c):
    return a + b + c

print sum3(1,2,3)

print sum3(93,53,70)

# Define a procedure, abbaize, that takes
# two strings as its inputs, and returns
# a string that is the first input,
# followed by two repetitions of the second input,
# followed by the first input.

def abbaize(a,b):
    return a+b+b+a

print abbaize('a','b')
print abbaize('dog','cat')
#>>> 'abba'

#print abbaize('dog','cat')
#>>> 'dogcatcatdog'

# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here

# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here

print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20: 
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"
    

    # Define a procedure, bigger, that takes in
# two numbers as inputs, and returns the
# greater of the two inputs.

def bigger(a,b):
    if a > b: 
       r=a
    else:
       r=b
    return r

print bigger (1,2)

# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'
def is_friend(name):
   if name[0]=='D':
      r=True 
   else:
      r=False
   return r 

print is_friend('Dave') 
print is_friend('Carl')
print is_friend('Mark')


#print is_friend('Diane')
#>>> True

#print is_friend('Fred')
#>>> False

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')


s="udacity"
print s[0]



def is_friend(name):
    return name[0]=='D' or name[0]=='N'
          
print True or False
print False or True
print True or True
print False or False

# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.

#print biggest(3, 6, 9)
#>>> 9
#print biggest(6, 9, 3)
#>>> 9
#print biggest(9, 3, 6)
#>>> 9
#print biggest(3, 3, 9)
#>>> 9
#print biggest(9, 3, 9)
#>>> 9

def biggest(a,b,c):
    big = c
    if (a > b and a > c):
        big = a
    elif b > c:
        big = b
    return big         

print biggest(3, 6, 9)
#>>> 9
print biggest(6, 9, 3)
#>>> 9
print biggest(9, 3, 6)
#>>> 9
print biggest(3, 3, 9)
#>>> 9
print biggest(9, 3, 9)
#>>> 9
    
def bigger(a,b):
    if a > b: 
       r=a
    else:
       r=b
    return r

print bigger (1,2)

# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# Add your own code and notes here

i=0
while i!=10:
    i=i+1
    print i

# This code demonstrates a while loop with a "counting variable"
i = 0
while i < 10:
    print i
    i = i+1

# This uses a while loop to remove all the spaces from a string of
# text. Can you figure out how it works?
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

# A procedure definition starts with def 
#must indent after the procedure is defined                
def print_numbers(n):
    i=1
    while i<=n:  
        print i 
        i=i+1    

print_numbers(3)
#A second way to do this is as below:
def print_numbers(n):
    i=0
    while i<n:  
        i=i+1  
        print i 

print_numbers(3)

#if print_numbers(0) then nothing will print because the while condition cannot be satisfied

# A small change will fix the crashing bug in printInches.

#cannot concatenate a string and integer in the same line
#search on google for unsupported operand type(s) for +:'int' and 'str'

def printExample(a, b):
    print a + b
    
def printInches(n):
    print str(n)+" inches"
 
# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)

# When I wrote boldwrap, I didn't copy the functionality of the
# bracket function carefully.  Review my code and catch the mistake.

def bracket(text):
    return '[' + text + ']'

def boldwrap(text):
   return '<b>' + text + '</b>'
#    print '\033[1m' + text + '\033[0m'

print bracket('This is an important message.')
print boldwrap('This is an important message.')

# Try adding print statements to look at the values of variables inside
# the remove function.  See if you can find out what's making it give
# silly answers such as remove('ding', 'do') -> 'dining'.

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location ==-1:
# this means that the string sub cannot be found
      return somestring
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

# 
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"

#Lesson 2.5 Debugging

#Debugging Strategy Recap
#We went over 5 debugging strategies in this lesson.
#Examine error messages when programs crash
#The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred.
#Work from example code
#If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.
#Make sure examples work
#Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.
#Check (print) intermediate results
#When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.
#Keep and compare old versions
#When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs.
#Commenting well to aid debugging
#You may have already seen comments in some of the code you've worked with throughout this program. Comments are lines of code that are ignored by the computer. They exist so that you can make notes (to other programmers or to yourself) about the code you write. Adding comments to your code can help you (and others) debug your code when things go wrong by comparing what the comment claims the code should do and what it actually does.

#In Python, you can make a comment by typing #. Everything written after the # on that line will be the comment. Other languages use different characters to denote comments, but every language has some way of making them.

#Programmers have many guidelines about how to write comments so that they are descriptive but unobtrusive. Throughout this Nanodegree program, and your entire programming career, you will be expected to follow that principle. Here are some tips to help you comment your code meaningfully:

#1) Don't comment "obvious code"
#The meaning of "obvious code" may change for you as you grow as a programmer, but generally if the code is self-explanatory it doesn't need a comment. The following is superfluous:

#print "Hello" # prints hello
#Simply writing print "Hello" is enough.

#2) Start functions with a comment
#All functions should start with a comment describing the expected input(s) and output(s), and explaining what the function does. This helps others determine what the intended purpose of your function is. Here's an example:

#def isLeapYear(year):
    # takes a number as input and outputs True if the number
    # represents a leap year and False otherwise
#In Python (but not all languages), you can also comment your functions with a docstring. A docstring is a multi-line string that acts as a descriptive comment for a function, but it is retained by the computer as the code executes and can be accessed by users as your code runs.

#def isLeapYear(year):
#    '''takes a number as input and outputs True if the number
#    represents a leap year and False otherwise'''
#You can choose to use either comments or docstrings in IPND, but you should be consistent with your choice. Classes (which you'll learn about in Stage 3) should also follow this rule.

#3) Keep commments up-to-date
#Your code can become very confusing if you make a change without updating the comment(s) as well. Make sure that they stay aligned to avoid confusing others that may be reading your code (or yourself if you're returning to code after a long break). After all, a major purpose of comments is to help others evaluate what your code is supposed to do when things go wrong. That is much harder to do if your comments give incorrect information!

#4) Be concise

##>>> Comments should be short and explain only the most important details of your code. If you find yourself having to write very long comments to clarify confusing parts of your code, you may want to rethink your approach to the problem. Generally, well written code will have sparse comments. Poorly written code may depend on them!

def bar(n,ch='_'):
    #***A horizontal bar of length n***
    return ch * n

def separator(html=False):
    #***A horizontal line in plain text or HTML***
    if html:
        print "<hr />"
    else:
        print bar(40)

x = bar(5)
print "x is ", x

def box(txt):
    #***Put text inside a box***
    print "+-" + bar(len(txt)) + "-+"
    print "| " + text          + " |"
    print "+-" + bar(len(txt)) + "-+"

print box(hello)

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    if (day=='Saturday' or day=='Sunday'):
        return True
    else:
        return False
       
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')

# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
    i=n
    while i>0:
       print i
       i=i-1
       if i==0:
         return 'Blastoff!'
print countdown(3)     


def countdown(n):
    while n>0:
       print n
       n=n-1
    print'Blastoff!'
print countdown(3)   

#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    big = biggest(a,b,c)
    if big==a:
        return bigger(b,c)
    if big==b:
        return bigger(a,c)
    else:
        return bigger(a,b)

print median(3,4,2)        

def smaller(a,b):
    if a < b:
        return a
    else:
        return b

def smallest(a,b,c):
    return smaller(a,smaller(b,c))

#def median(a,b,c):
#   if a!=smallest or a!=biggest):
  #      return a
#    else:
#        if (b!=smallest or b!=biggest):
  #          return b
#        else:
 #           return c    

print bigger(1,2)
print biggest (1,2,3)
print smaller (1,2)
print smallest (1,2,3)

def median(a, b, c): 
    return sorted([a,b,c])[1]

print median (7,2,9)

def median(a,b,c):
    if a < b:
        if b < c:
            return c
        elif a < c:
            return c
        else:
            return a
    else:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c

print median(5,2,8)

#def smaller(a,b):


#def median(a,b,c):
#    if a > b:
#        bigger = b
#    elif c > bigger:
 #       bigger = c
#    elif a < b:
#        lesser = a
 #   elif c < lesser:
 #       lesser = c
 #  elif (a != bigger and a != lesser):
 #       med = a
 #  elif (b != bigger and b != lesser):
  #       med = b
 #    elif (c != bigger and c != lesser):
   #      med = c
  #   return med  
    
#print median(2,4,6)      
          
          # Write code for the function random_noun, which takes in no inputs but outputs 
# one of two nouns randomly. Use the randint function to generate a number 
# from 0-1 and return a noun depending on whether the number is equal to 0 or 1. 
# Feel free to experiment with different nouns, but for submission purposes return 
# the string "sofa" if the number is 0, else return "llama".

from random import randint

def random_noun():
    random_num = randint(0,1)
    if random_num==0:
        return "Sofa"
    else:
        return "Ilama"

# Write code for the function random_verb, which takes in no inputs but outputs 
# one of two verbs randomly. Use the randint function to generate a number from 0-1 
# and return a verb depending on whether the number is equal 0 or 1. Feel free to 
# experiment with different verbs, but for submission purposes return the string "run"
# if the number is 0, else return "kayak".

def random_verb():
    random_num = randint(0,1)
    if random_num==0:
       return "run"
    else:
       return "kayak"

# Write code for the function word_transformer, which takes in a string word as input. 
# If word is equal to "NOUN", return a random noun, if word is equal to "VERB", 
# return a random verb, else return the first character of word. 
# Use predefined functions -- this can be done in the code!

def word_transformer(word):
    if word[0:] == "NOUN":
# Can also use if word=="NOUN":
        return random_noun()
    elif word[0:] == "VERB":
# Can also use if word=="VERB":
        return random_verb()
    return word[0]

print word_transformer("BAILEY")

# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    sentence1 = mad_lib.replace("NOUN",random_noun())
    sentence2 = sentence1.replace("VERB",random_verb())
    return sentence2
    
print process_madlib("This is a good NOUN to use when you VERB your food")
print process_madlib("I'm going to VERB to the store and pick up a NOUN or two.")

        # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len

#Above does not use the word transformer

#Notes for this
#function is the string mad_lib that can contain instances of noun and verb
#gpa; os tp return a new string processed where all those instances  are replaced with the 
#random nouns and verbs
#So we'll be using this idea of a four character long box to solve this problem
#which we went over before writing code for a function word transformer
    #Since we need to keep track of our box's position becuase it's moving up the string
#by increments of one or four, we'll need to introduce a new variable for that purpose
#we'll set the variable index to 0 and we chose 0 because our box will start at the beginning of
#the string passed in. Since the length of hte string passed in can vary and because we want to
#repeat the same steps of checking everything in the box, and adding to process based on
#what's inside over and over again, we'll want to use this while loop
#But now we'll need to figure out what our condition is since we're going through the string
#madlib character by character until we've reached the end of the string, the condition use for
#a while loop will be while index is less than the length of madlib
#Cool now that we have our while loop set up, let's start writing the internals of the loop
#Since all our decisions on whether to add single character or a random verb or noun is 
#based on this idea of this four charaxter long box we need to set that up first
#In code this box will be this four character long substring starting from index, or at the
#beginnng of the box to index+4
#Now the only thing i dont like about this string slice is this number 4 here
#Although we know it represents the length of the box, this quote unquote magic number
#can cause confusion later on. If you come back to this program after a while or someone looks
#at your code for the first time they might have trouble figuring out what this numnber
#means or what its purpose is which is something we dont want.
#to fix this I set this variable box length to 4 and use that in our string slide
#Now it's clear what the number 4 represents
#Now that we have our first four character box set up property let's refresh ourselves
#on what we need to do based on the contents of this box
#So if the box over the variable frame is equal to noun or verb we add the respective
#noun or verb to processed and move our box over by four characters
#If the box isnt equal to noun or verb we add the first character of frame to processed
#and move our box over by one. This variable to_add has the proper random word or single
#character we need to add to our string processed since it uses the function word_transformer
#which we wrote before. To_add will be equal to a random verb if frame is equal to the string verb
#and a random noun of frame is equal to the string noun else it would be equal to the first character
#of frame. Let's add this now to our processed string. Now that our processed string has the
#right value added to it the only thing left to do is move our box over by one or four 
#characters so we can repeat this process. How can we do this? Why don't we check the length
#of to_add or the word returned and make our decision based on that
#If the length of to_add is one character long then we obviously havent been returned
#with a random verb or noun so we'll just inch our box over by one index.
#If that wasnt the case you'll be sure to be returned with a random verb or noun so we'll add
#4 to index instead. The last thing we need to do is return the processed string.
#So lets add that to the end of our function outside of the. loop. There
#we have it a fully functioning madlibs generator that can repleace instances of
#nouns and verbs with the random nouns and random verbs

def process_madlib(mad_lib):
    processed = ""
    index = 0
    box_length=4
    while index < len(mad_lib):
        frame=mad_lib[index:index+box_length]
        to_add=word_transformer(frame)
        processed+=to_add
        if len(to_add)==1:
            index+=1
        else:
            index+=4
    return processed
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)

# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# Add your own code and notes here

# Here's a chance to play around with lists for a bit before you continue
# Take a look at what the following code does and try to guess how it works.

print "EXAMPLE 1: Lists can contain strings"
string_list = ['HTML', 'CSS', 'Python']
print string_list
#output = ['HTML', 'CSS', 'Python']

print "EXAMPLE 2: Lists can contain numbers"
number_list = [3.14159, 2.71828, 1.61803]
print number_list
#output = [3.14159, 2.71828, 1.61803]

print "EXAMPLE 3: Lists can be 'accessed' and 'sliced' like how we accessed and sliced strings in the previous lessons"
pi = number_list[0]
not_pi = number_list[1:]
print pi
print not_pi
#output = pi=3.14159, not pi = [2.71828, 1.61803]

print "EXAMPLE 4: Lists can contain strings AND numbers"
mixed_list = ['Hello!', 42, "Goodbye!"]
print mixed_list
#output = ['Hello!', 42, "Goodbye!"]

print "Example 5: Lists can even contain other lists"
list_with_lists = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']
print list_with_lists
#output = [3, 'colors:', ['red', 'green', 'blue'], 'your favorite?']

stooges = ['Moe','Curly','Happy']
print stooges

# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    a = month_number
    how_many_days = days_in_month[a]
    return days_in_month[a]

print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

def how_many_days(month):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    return days_in_month[month - 1]

print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30

beatles = [['John', 1940],['Ringo', 1941], ['Paul', 1942],['George', 1945]]
print beatles
print beatles[3][1]

# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list
print countries[1][1]

# Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Calculate this by accessing the list and
# dividing the population of China (1350)
# by the population of Romania (21).
# Please print your result.
china = countries[0][2]
romania = countries[2][2]
multiple = china / romania
print multiple

print countries [0][2] / countries [2][2]

p = ['H','e','l','l','o']
print p
p[0]='Y'
print p
p[4]='!'
print p

# We defined:

stooges = ['Moe','Larry','Curly']

# but in some Stooges films, Curly was
# replaced by Shemp.

# Write one line of code that changes
# the value of stooges to be:

# but does not create a new List
# object.
stooges[2]='Shemp'
print stooges

spy=[0,0,7]
agent=spy
print spy, agent
spy[2]=agent[2]+1
print spy[2]
print agent[2]

# Define a procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.

#spy = [0,0,7]

# In the test below, the first line calls your 
# procedure which will change spy, and the 
# second checks you have changed it.
# Uncomment the top two lines below.
def replace_spy(p):
    spy = [0,0,7]
    p[2]=p[2]+1
print spy
#>>> [0,0,8]

#List Operations1
#<list>.append(<element>)
stooges=['Moe','Larry','Curly'] 
stooges.append('Shemp')
print stooges

p=[1,2]
p.append(3)
p=p+[4,5]#this is an assignment p
print p
print len(p)

p=[1,2]
q=[3,4]
p.append(q)
print p
print len(p)

# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
  for e in p:
       print e

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here
#the above will print out this -- 1, 2, [3,4]

# Read through these examples and try to figure out what's going on.
# Press "Test Run" to see what they do.

print "EXAMPLE 1: We can use for loops to go through a list of strings"
example_list_1 = ['a', 'b', 'c', 'd']
for thing in example_list_1:
    print thing 

print "EXAMPLE 2: We can use for loops on nested lists too!"
example_list_2 = [['China', 'Beijing'],
                  ['USA'  , 'Washington D.C.'],
                  ['India', 'Delhi']]
for country_with_capital in example_list_2:
    country = country_with_capital[0]
    capital = country_with_capital[1]
    print capital + ' is the capital of ' + country

def sum_list(list): #the parameter is list
    sum = 0
    for i in list:
        sum = sum + i
    return sum    

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134
def sum_list(p): #the parameter is p
    result = 0
    for e in p:
        result = result + e
    return result    

print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134

# Define a procedure, measure_udacity,
# that takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(p): #as defined by me
    result = 0
    for e in p:
        if e[0]=="U":
           result = result + 1
        else: 
           result = 0
    return result
        
print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])

def measure_udacity(U): #as defined by Udacity
    result = 0
    for e in U:
        if e[0]=='U':
           result = result + 1
    return result
        
print measure_udacity(['Dave','Sebastian','Katy'])
#>>> 0

print measure_udacity(['Umika','Umberto'])
#>>> 2

print measure_udacity(['Udacity','umberto','USA', 'under'])
#>>>2

# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.
def find_element(p):
    return p.index(2)
print find_element([1,2,3])  
#output = 1  

def find_element(list,string):
       if string in list:
         return list.index(string)
       else:
         return -1
print find_element([1,2,3],3)
#output = 2
print find_element(['alpha','beta'],'gamma')
#output=-1

def find_element(p,t):
    i=0
    while i<len(p):
        if p[i]==t:
            return i
        i=i+1
    return i       

aList = [123, 'xyz', 'zara', 'abc'];

print "Index for xyz : ", aList.index( 'xyz' ) 
print "Index for zara : ", aList.index( 'zara' ) 

p=[0,1,2]
print p.index(2)
p=[0,1,2,2]
print p.index(2)#p is the first place in the list where it occurs
#p=[0,1,3]
# print p.index(2)
#for this will get an error that 2 doesnt exist in the list 

# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(list,string):
       if string in list:
         return list.index(string)
       else:
         return -1
print find_element([1,2,3],3)
#output = 2
print find_element(['alpha','beta'],'gamma')
#output=-1

def find_element(list,string):
    if string not in list:
        return -1
    else:
        return list.index(string)

print find_element([1,2,3],3)
#output = 2
print find_element(['alpha','beta'],'gamma')
#output=-1   

# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.
#def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    #return days   

#print daysBetweenDates(1963, 1, 2, 2015, 11, 28)

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_Year(byear, eyear):
    result = 0
    i=byear
    while i <= eyear:
        if i % 4 == 0 and i %100 != 0 or i % 400 == 0: 
           result = result + 1
        i=i+1
    return result    

print leap_Year(1963, 2015)

# % modulus - Divides left hand operand by right hand operand and returns remainder 
def totaldaysinayear(daysOfMonths,y1,y2): #the parameter is daysOfMonths
    sum = 0
    for i in daysOfMonths:
        sum = sum + i
    years = y2-y1-1
    totaldays = years*sum
    return totaldays
print totaldaysinayear(daysOfMonths,1963,2015)

def totaldaysinfirstmonth(bmonth,bday):
    daysinfirstmonth=daysOfMonths[bmonth-1]-bday
    return daysinfirstmonth
print totaldaysinfirstmonth(1,2)

def totaldaysincurrentmonth(cmonth,cday):
    daysincurrentmonth=cday
    return daysincurrentmonth
print totaldaysincurrentmonth(12,5)

#def totaldaysinrestoffirstyear(daysOfMonths,bmonth):
#    a = bmonth
#   totaldays = 0
#    for a in daysOfMonths:
#        totaldays = totaldays+=daysOfMonths
#       a=a+1
#   return totaldays
#print totaldaysinrestoffirstyear(daysOfMonths,1)
#ABOVE CODE IS NOT CORRECT -- THERE IS AN ERROR 

#BREAKDOWN OF PROBLEMS
#PROBLEM #1 = NUMBER OF DAYS IN FIRST MONTH OF BIRTH YEAR
#PROBLEM #2 = NUMBER OF DAYS IN THE LAST MONTH OF CURRENT YEAR
#PROBLEM #3 = NUMBER OF DAYS IN BETWEEN THE BIRTH AND CURRENT YEAR
#PROBLEM #4 = NUMBER OF LEAP YEARS
#TOTAL NUMBER OF DAYS = OUTPUTS OF #1+#2+#3+#4

# Lesson 2.7: How to Solve Problems - Days Between Dates

# In this lesson, you'll be working on solving a much
# bigger problem than those you've seen so far. If you
# want, you can use this starter code to write your
# quiz responses and then copy and paste into the
# Udacity quiz nodes.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4184188665/m-108325398

# Simple Mechanical Algorithm
# days = 0
# while date1 is before date2:
#     date1 = advance to next day
#     days += 1

# Fill in the functions below to solve the problem.

def isLeapYear(year):
    return True

def daysInMonth(year, month):
    return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        days += 1
    return days

###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    if day!= 30:
        day=day+1
    elif month!=12:
        month=month + 1
        day = 1
    else:
        year=year + 1
        month = 1
        day = 1
    return year, month, day

print nextDay(2015, 12, 30)
print nextDay(1999, 12, 30) #=> (2000, 1, 1)
print nextDay(2013, 1, 30) #=> (2013, 2, 1)
print nextDay(2012, 12, 30) #=> (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
           return year, month+1, 1 
        else:
           return year+1, 1, 1 
    
print nextDay(2015, 12, 30)
print nextDay(1999, 12, 30) #=> (2000, 1, 1)
print nextDay(2013, 1, 30) #=> (2013, 2, 1)
print nextDay(2012, 12, 30) #=> (2013, 1, 1)  (even though December really has 31 days)

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
       
#def daysBetweenDates(year1, month1, day1, year2, month2, day2):
#Returns the number of days between year1/month1/day1 and year2/month2/day2. Assumes inputs are valid dates in Gregorian calendar, and the first date is not after
#the second.
#PSEUDOCODE

def dateIsBefore(year1, month1, day1, year2, month2, day2):
#Returns True if year1 + month1 + day1 is before year2 + month2 + day2. Otherwise returns False
    if year1 < year2:  
        return True
    else:
        if year1==year2 and month1==month2 and day1==day2:
            return False
        else:
            return True

def leap_Year(year1, year2):
    result = 0
    i=year1
    while i <= year2:
        if i % 4 == 0 and i %100 != 0 or i % 400 == 0: 
           result = result + 1
        i=i+1
    return result    

#print leap_Year(1963, 2015)       

def daysBetweenDates(year1,month1,day1,year2,month2,day2):

#    assert not dateIsBefore(year2, month2, day2, year1, month1, day1) - activating this will result in a Python error called Assertion Error
    days=leap_Year(year1,year2)
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
         year1,month1,day1=nextDay(year1,month1,day1)
         days=days+1
    return days 

print daysBetweenDates(1963,1,2,2015,12,6) 
print daysBetweenDates(2013,1,24,2013,6,29) 
print daysBetweenDates(1912,12,12,2012,12,12) 

# THIS IS HOW I SOLVED THE PROBLEM
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def daysInMonth(year,month):
    return daysOfMonths[month-1]

def nextDay(year, month, day):
    if day!= daysInMonth(year,month):
        day=day+1
    elif month!=12:
        month=month + 1
        day = 1
    else:
        year=year + 1
        month = 1
        day = 1
    return year, month, day
   
def dateIsBefore(year1, month1, day1, year2, month2, day2):
#Returns True if year1 + month1 + day1 is before year2 + month2 + day2. Otherwise returns False
    if year1 < year2:  
        return True
    else:
        if year1==year2 and month1==month2 and day1==day2:
            return False
        else:
            return True

def leap_Year(year1, year2):
    result = 0
    i=year1
    while i <= year2:
        if i % 4 == 0 and i %100 != 0 or i % 400 == 0: 
           result = result + 1
        i=i+1
    return result    

def daysBetweenDates(year1,month1,day1,year2,month2,day2):

    days=leap_Year(year1,year2)
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
         year1,month1,day1=nextDay(year1,month1,day1)
         days=days+1
    return days 

print daysBetweenDates(1963,1,2,2015,12,6) 
print daysBetweenDates(2013,1,24,2013,6,29) 
print daysBetweenDates(1912,12,12,2012,12,12) 

# THIS IS HOW UDACITY SOLVED THE PROBLEM
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False        

def daysInMonth(year,month):
    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        return 31
    else:
        if month==2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30        

    return daysOfMonths[month-1]

def nextDay(year, month, day):
    if day < daysInMonth(year,month):
        return year, month, day+1
    else: 
        if month < 12: 
            return year, month+1,1 
        else:
            return year+1, 1,1
           
def dateIsBefore(year1, month1, day1, year2, month2, day2):
#Returns True if year1 + month1 + day1 is before year2 + month2 + day2. Otherwise returns False
    if year1 < year2:  
        return True
    if year1==year2:
        if month1<month2:
           return True
        if month1==month2:
           return day1<day2
    return False         
        
def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    days=0
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
         year1,month1,day1=nextDay(year1,month1,day1)
         days=days+1
    return days 

def mytest():
    assert daysBetweenDates(2013,1,1,2013,1,1)==0
    assert daysBetweenDates(2013,1,1,2013,1,2)==1
    assert nextDay(2013,1,1)==(2013,1,2)
    assert nextDay(2013,4,30)==(2013,5,1)
    assert nextDay(2012,12,31)==(2013,1,1)
    assert nextDay(2013,2,28)==(2013,3,1)
    assert nextDay(2013,9.30)==(2013,10,1)
    assert nextDay(2012,2,28)==(2012,2,29)
    assert DaysBetweenDates(2012,1,1,2013,1,1)==366
    assert DaysBetweenDates(2013,1,1,2014,1,1)==365
    assert DaysBetweenDates(2013,1,23,2013,6,29)==156
    print "Tests Finished!"

print daysBetweenDates(1963,1,2,2015,12,6) 
print daysBetweenDates(2013,1,24,2013,6,29) 
print daysBetweenDates(1912,12,12,2012,12,12) 

# Below is a testing script that will check if your code is doing
# what it is supposed to. Don't change it! The test will run
# when you execute the file.
# Bonus: Can you figure out how the test works?

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

# Investigating adding and appending to lists
# If you run the following four lines of codes, what are list1 and list2?

list1 = [1,2,3,4]
list2 = [1,2,3,4]

list1 = list1 + [5, 6]
list2.append([5, 6])

# to check, you can print them out using the print statements below.

print "showing list1 and list2:"
print list1
print list2

# What is the difference between these two pieces of code?
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def proc(mylist):
    mylist += [6, 7]
    return mylist

def proc2(mylist):
    mylist.append(6)
    mylist.append(7)
    return mylist

# Can you explain the results given by the print statements below?

print
print "demonstrating proc"
print list1
print proc(list1)
print list1
print
print "demonstrating proc2"
print list2
print proc2(list2)
print list2

# Python has a special assignment syntax: +=.  Here is an example:

list3 = [1,2,3,4,5]
list3 += [6, 7]

def proc3(mylist):
    return mylist
# Does this behave like list1 = list1 + [6,7] or list2.append([6,7])? Write a
# procedure, proc3 similar to proc and proc2, but for +=. 

print
print "demonstrating proc3"
print list3
print proc3(list3)
print list3

# Let's learn a little bit of Data Analysis and how we can use
# loops and lists to create, aggregate, and summarize data
# For the part 1, we'll learn a basic way of creating data using
# Python's random number generator.
# To create a random integer from 0 to 10, we first import the 
# "random" module
# We then print a random integer using the random.randint(start, end) function
# Remember that if we want to concatenate a string and a number, we need to convert the 
# integer into a string using the str() function
# We now want to create a list filled with random numbers. The list should be 
# of length 20
# Write code here and use a while loop to populate this list of random integers. A crucial
# function that will help you is to use the append() method to add elements to a list.
import random

random_list = []
list_length = 20

#One piece of code suggested by UDACITY
#while len(random_list) < list_length:
#   random_list.append(random.randint(0,10))
#   return random_list

#Here's alternative code that simplifies the logic a bit if the above code is complicated to understand. import random
count = 0
while count < list_length:
   random_list.append(random.randint(0,10))
   count += 1
   
# When we print this list, we should get a list of random integers such as:
# [7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
print random_list
print "Random number generated: " + str(random.randint(0,10))

#Breaking Down the Problem
#We first need to understand what are the inputs and what are the outputs (or results) that we want to obtain.
#The inputs are:
#An empty list
#A variable that has the value 20, telling us that we want to create a list of length 20
#The output is:
#A list of random integers between 0 and 10 that could look like:
#[7, 5, 1, 6, 4, 1, 0, 6, 6, 8, 1, 1, 2, 7, 5, 10, 7, 8, 1, 3]
#What To Do

#Therefore we want to generate a list of random integers given an empty list. One way is to use the append() method for lists and add in a random integer, 20 times.

#That's how a person would do it manually on pen and paper anyway. Let's see if we can write an outline of what to do if we were to do this manually on pen and paper:

#Generate a random integer between 0 and 10
#Add this random integer to our list
#Do we have a list of length 20 yet?
#If not, we loop back up and go through steps 1 to 3 again **while** length of the list is less than 20
#If we translate these steps into real code, we can use a while loop that checks whether the length of the list is less than 20.

# Know we want to ask our self the question:
# How many occurrences of the number 9 appear in our randomly made list?
# For example if we have a list: [2,8,9,9,4,5,9], we want to figure out
# how to go loop through the list and count how many occurrences of the
# number 9. In this example, the number 9 occurs 3 times in the example
# list

import random

# 1. Create random list of integers using while loop
random_list = []
list_length = 20

i = 0
count = 0
while i < list_length:
   random_list.append(random.randint(0,10))
   if random_list[i] == 9:
      count=count+1
   else:
      count=count+0
   i=i+1     

# Write code here to loop through the list and count all occurrences
# of the number 9. If statements and While loops will help you solve
# this problem.
# Test if our While loop we wrote works, we should manually count
# how many times the number 9 is present in the list.
print random_list
print count

#Breaking Down the Problem
#We first need to understand what are the inputs and what are the outputs (or results) that we want to obtain.
#The inputs are:
#A list of 20 randomly generated integers
#The output is:
#A number representing the count of the number of times the number 9 is in the list
#What To Do
#Therefore we want to loop through the list and count how many times the number 9 appears. If the current element is the number 9, we can increase the count by 1 and move on to the next element in the list.
#Let's see if we can write an outline of what to do if we were to do this manually on pen and paper:
#Loop through each element in the list
#If the element is 9, we increase our count by 1
#Are we at the end of the list yet?
#If not, we loop back up and go through steps 1 to 3 again while we are still going through the list
#Translation
#Let's step through these steps and translate these steps into computer code.
#1. Loop through each element in the list
#It seems like we first need to set up the loop structure to loop through each element in the list. In order to do this, we should setup some variables to hold the current index of the list and the current count:
index = 0
count = 0
#We can now set up our loop structure:

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1

random_list = []
list_length = 20

while len(random_list) < list_length:
   random_list.append(random.randint(0,10))

index = 0
count = 0

while index < len(random_list):
  if random_list[index] == 9:
    count = count + 1
  index = index + 1

# Great! We now want to create a new list that contains the counts
# of all occurrances of every number seen in the randomly generated 
# list. That means we want counts of all occurrences of all numbers
# from 0 through 10 in our randomly generated list.
# Let's store our counts in a list of length 11 
# with zeros filled in.
# We can multiply a list construct to create a list with the same
# elements n number of times.
#count_list = [0] * 11
# We use this list to store our count of numbers 0 to 10 - take note 
# that total numbers 0 to 10 is 11. We can use the index number of
# each element to refer to the count of our target
# number. Our target number is actually the index of the list.
# Therefore, for our output, we want a count_list that looks like:
# [1,2,3,2,2,1,1,2,3,1,2]
# Here's our code that we coded before
# Initialize count_list for every integer between 0 and 10. 
# A number will correspond to an index of this count_list
# Therefore if we see that there are 3 occurrences of the number 4, 
# we assign count_list[4] = 3, if there are 5 occurrences of the 
# number 6, we assign count_list[6] = 5
# Check the list we created
#print count_list
# If we coded everything correctly, the sum of all of the numbers 
# in count_list should be 20
#print sum(count_list)
# Let's print out the occurrences for the numbers 0, 4, 5, and 6

import random

count_list = [0]*11
count = 0
index = 0
random_list = []
list_length = 20
i=0
while i < list_length:
  random_list.append(random.randint(0,10))
  i=i+1

index = 0
sum=0
while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  sum = sum + number
  index = index + 1
  
print random_list
print sum
print count_list[0]
print count_list[4]
print count_list[5]
print count_list[6]

# We now would like to summarize this data and make it more visually appealing
# We want to go through count_list and print a table that shows the number and its 
# corresponding count.

# The output should look like this neatly formatted table:
"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""
# Here is our code we have written so far:

import random

count_list = [0]*11
count = 0
random_list = []
list_length = 20
i=0
while i < list_length:
  random_list.append(random.randint(0,10))
  i=i+1

index = 0
sum=0
while index < len(random_list):
  number = random_list[index]
  count_list[number] = count_list[number] + 1
  sum = sum + number
  index = index + 1

print random_list
print " "" "
print "number | occurrence"
num_len = len("number")

index = 0
while index <= 10:
   num_spaces = num_len - len(str(index))
   print " " * num_spaces + str(index) + " | " + str(count_list[index])
   index = index + 1
  
print random_list
print sum
print count_list[4]
print count_list[5]
print count_list[6]
   
# Write code here to summarize count_list and print a neatly formatted table that looks
# like this:

"""
number | occurrence
     0 | 1
     1 | 2
     2 | 3
     3 | 2
     4 | 2
     5 | 1
     6 | 1
     7 | 2
     8 | 3
     9 | 1
    10 | 2
"""

# Hint: To print 10 blank spaces in a row, we can multiply a string by a number "n"
# to print this string n number of times:
print "Udacity! "*10 

# Define a procedure, product_list,
# that takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(list):
    i=0
    sum=1
    while i < len(list):
        sum = sum * list[i]
        i=i+1
    return sum

print product_list([9])
#>>> 9

print product_list([1,2,3,4])
#>>> 24

print product_list([])
#>>> 1

# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list_of_numbers):
    i=0
    if len(list_of_numbers) == 0:
        big = 0
    elif list_of_numbers[i+1] > list_of_numbers[i]:
        big = list_of_numbers[i+1]
    else:
        big = list_of_numbers[i]
    i=i+1
    return big    

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

def greatest(list_of_numbers):
    big = 0
    for i in list_of_numbers:
        if i > big:
            big = i
    return big

print greatest([4,23,1])
#>>> 23
print greatest([])
#>>> 0

# Let's play around with one more string method: string.split(), which
# splits a string into a list of substrings, and returns it as a new list. 
# Assign list_of_words1 to the split string1 and list_of_words2 to the split string2.

string1 = "Yesterday, PERSON and I went to the PLACE. On our way, we saw a ADJECTIVE NOUN on a bike."
string2 = "PLACE is located on the ADVERB side of Dublin, near the mainly ADJECTIVE areas of PLACE."
list_of_words1 = string1.split()
list_of_words2 = string2.split()

print list_of_words1
print list_of_words2

# Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.

#THIS CODE DOES NOT WORK -- NEED TO FIGURE OUT WHY NOT!
def word_in_pos(word, parts_of_speech):
    count = 0
    while count < len(parts_of_speech):
      if word in parts_of_speech[count]:
            return word
      return "None"
    count=count+1 

test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)
  
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
      if pos in word:
            return pos
    return "None"
    
test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)  

# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that 
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input. 

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN With Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
def play_game(ml_string, parts_of_speech):    
    replaced=[] 
    ml_string=ml_string.split()
    for word in ml_string:
        replacement=word_in_pos(word,parts_of_speech)
        if replacement!= None:
           word=word.replace(replacement,"Corgi")
           replaced.append(word)
        else:
           replaced.append(word)
    replaced=" ".join(replaced)  
    return replaced      
            
print play_game(test_string, parts_of_speech)

#Same as above but with user input for the word

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """Straight outta PLACE, crazy NOUN named PERSON, 
from the gang called PLURALNOUN With Attitude"""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):    
    replaced=[] 
    ml_string=ml_string.split()
    for word in ml_string:
        replacement=word_in_pos(word,parts_of_speech)
        if replacement!= None:
#           user_input=raw_input('-->')
# This will work if the raw input module is installed on Sublime Text2
           word=word.replace(replacement,"Bailey")
           replaced.append(word)
        else:
           replaced.append(word)
    replaced=" ".join(replaced)  
    return replaced      
            
print play_game(test_string, parts_of_speech)

#cd: Stands for "change directory." When you first open Terminal, you will be in your computer's Home 
#directory (usually this directory has the same name as your user account).
#From there you can cd into any directory accessible from the Home. 
#In the video, Sean uses Terminal to cd into the Desktop by typing 
#cd Desktop/ Note: "directory" and "folder" are synonymous

#ls: Stands for "list." The ls command lists all files and folders in the current directory.

#python: This command will start a Python interpreter so you can run code. 
#If you write just python a Python shell starts and you can write Python code
# directly in Terminal (this is not recommended for big projects). 
#You can also include the name of a Python file in the current directory to run pre-written code. 
#So, for example, python madlibs_generator.py runs the file 
#madlibs_generator.py within the current directory.