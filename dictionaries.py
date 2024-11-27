# Lesson 4.4: Dictionaries

# Dictionaries are another crucial data structure to learn in Python in addition to lists.
# These data structures use string keywords to access data rather than an index number in lists.
# Using string keywords gives programmers more flexibility and ease of development to use a
# string keyword to access an element in this data structure.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4181088694/m-3919578552

# Strings vs List vs Dictionary Demo
s = "hello"
p = ["alpha",23]
d = {"hydrogen": 1, "helium": 2}

# Accessing items
print s[2]
print p[1]
print d["hydrogen"]

# Replacing values
#s[2] = "a" # Will produce error, comment this line to continue with rest of code execution
p[1] = 999
d["hydrogen"] = 49

# Add your own code and notes here

elements = {'hydrogen':1,'helium':2,'carbon':6}
print elements
print elements['helium']
print 'lithium' in elements #this will equate to false
elements['lithium'] = 3
elements['nitrogen'] = 8
print elements['nitrogen']
elements['nitrogen'] = 7
print elements['nitrogen']

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai':17.8,'Istanbul':13.3,'Karachi':13.0,'Mumbai':12.5}
print population
print population['Mumbai']

elements = {}
elements['H'] = {'name':"hydrogen",'number':1,'weight':1.00794}
elements['He'] = {'name':'Helium','number':2,'weight':4.00262,'noble gas':True}
print elements['H']
print elements['H']['name']
print elements['He']['name']
