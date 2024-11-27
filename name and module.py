#The attribute _name_ is present in every default python function
#This attribute _name_ gives the name of the class

def functionA():
    return "A"
def functionB(params):
    return params.__name__
 
print functionB(functionA) # prints functionA

#The attribute _module_ is the name of the module the function was defined in, or None if unavailable.

def functionA():
    return "A"
def functionB(params):
    return params.__module__
 
print functionB(functionA) # prints __main__

