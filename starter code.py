# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

print 3
print 1 + 1

# Add your own code and notes here
print 7 * 7 *24 *60
print 299792458 * 100 * 1.0/1000000000

# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here
cycles_per_second = 2700000000 # processor speed_of_light
cycle_distance = speed_of_light / cycles_per_second
print cycle_distance
my_age = 52
number_of_days_in_a_year = 365
days_alive = my_age * number_of_days_in_a_year
print days_alive

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
name = "My name is Catherine"
print name
print name * 4

# This code shows some basic variable assignment and string printing. 
name = "Andy"
print "Hello " + name
print name * 4

# This code shows the difference between the string "4" and the number 4.
# Remove the four comment characters (#) on the lines below to see what happens.
print 4
print "4"
print 4 + 4
print "4" + "4"

# This code shows some of the different mistakes that are easy to make while 
# working with strings. Remove one comment at a time and press Test Run to 
# see what happens. Be sure to re-comment before moving on or the program
# will keep showing you an error.
print "hello"
print 'hello'
print "hello"

# This code will give you a peek at what you are about to learn! Uncomment 
# all of the lines below to get a glimpse of "string indexing"
name = "Andy"
print name[0]
print name[1]
print name[2]
print name[3]
s = "udacity"
print s[0:]
print "U" + s[1:]
print s[1:1