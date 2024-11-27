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

def biggest(a,b,c):
   if a > b:
        if a > c:
          return a 
        else:
            return c
   else:
       if b>c:
          return b
       else:
          return c

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
def biggest(a,b,c):
     return max(a,b,c)
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