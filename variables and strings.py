# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t")
print "test".find("t", 1)

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string

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

# Add your own code and notes here	