

import math
import os
import random
import re
import sys

#Task
#Given an integer, , perform the following conditional actions:

#If num is odd, print Weird
#If num is even and in the inclusive range of 2 to 5, print Not Weird
#If num is even and in the inclusive range of 6 to 20, print Weird
#If num is even and greater than 20 , print Not Weird

import sys


num = input("Enter a number: ")
num = int(num)

if num % 2 != 0:
    print("Weird")
else:
    if num < 2 and num > 5:
        print("Not Weird")    
    if num < 6 and num > 20:
        print("Weird")
    if num > 20:
        print("Not Weird")

#Task
#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. 
#The first line should contain the result of integer division,  // . 
#The second line should contain the result of float division,  / .

#No rounding or formatting is necessary.

#Example
#a=3
#b=5
#The result of the integer division 3//5 = 0
#The result of the float division is 3/5 = 0.6

#a = input("Enter the first number: ")
#b = input("Enter the second number: ")

#def first(a, b):
#    c=a / b
#    return c
    

#def second(a, b):
#    d=a // b
#    return d

#print (c)
#print (d)

#def add_two_numbers(number_1, number_2):
#   return number_1 + number_2

#print (add_two_numbers(4, 3))
#print (add_two_numbers(2, 6))
#print (add_two_numbers(0, 9))

#Task Complete the function solveMeFirst to compute the sum of two integers.
#Task Example

#Return .
#Function Description
#Complete the solveMeFirst function in the editor below.
#solveMeFirst has the following parameters:
#
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#Returns
#int: the sum of a and b

def solveMeFirst(num1,num2):
    # Hint: Type return a+b below
    return num1+num2

res = solveMeFirst(num1,num2)
print(res)

#Task Complete the function solveMeFirst to compute the multiplication of two floating numbers.
#Task Example

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Returns
#float: the product of num1 and num2

def solveMeFirst(num1,num2):
    # Hint: Type return a+b below
    return num1*num2

res = solveMeFirst(num1,num2)
print(res)

#Task Complete the function solveMeFirst to compute the division of two floating numbers.
#Task Example

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Returns
#float: the division of num1 and num2

def solveMeFirst(num1,num2):
    # Hint: Type return a+b below
    return num1 / num2

res = solveMeFirst(num1,num2)
print(res)

#Task Complete the function solveMeFirst to compute the division of two floating numbers.
#Task Example

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Returns
#float: the division of num1 and num2

def solveMeFirst(num1,num2):
    # Hint: Type return a+b below
    return num1 // num2

res = solveMeFirst(num1,num2)
print(res)

#Task
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
#Example

#Print the following:
#8
#-2
#15
#Input Format
#The first line contains the first integer, .
#The second line contains the second integer, .
#Constraints - greater than one and less than 10e10

#Output Format
#Print the three lines as explained above.
#Sample Input 0
#3
#2
#Sample Output 0
#5
#1
#6
#Explanation 0

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


if (1 <= int(a) <= 10e+10 and 1 <= int(b) <= 10e+10):
    sum = a + b
    difference = a - b
    multiply = a * b
    print(sum)
    print(difference)
    print(multiply)
else:
    print("wrong input")

#Task The provided code stub reads two integers, a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  // . 
#The second line should contain the result of float division,  / .
#No rounding or formatting is necessary.
#Example
#The result of the integer division is 3//5 = 0.
#The result of the float division is 3/5 = 0.6 .
#Task Example

a = int(input("Enter the first number: ")) #all number inputs must be an integer
b = int(input("Enter the second number: "))

    
integers = a // b
floating = a / b

print(integers)
print(floating)

#Task
#The provided code stub reads an integer, n , from STDIN. For all non-negative integers i < n, print the square of i. 
#Print the square of each number on a separate line.
#The input is the integer n
#The constraint is that n must be larger than 1 and smaller than 20

n = int(input("Enter a number: "))

for i in range(0, n):
    if (1 <= int(n) <= 20):
        output = n*n
        print(output)
    else:
        print(0)

#The included code stub will read an integer,n , from STDIN.
#Without using any string methods, try to print the following:
#if n=3, print 123, without any spaces.
#The constraint is that n must be larger than 1 and smaller than 150

#Quiz 4 print the numbers on one line
#The included code stub will read an integer,n , from STDIN.
#Without using any string methods, try to print the following:
#if n=3, print 123, without any spaces.
#The constraint is that n must be larger than 1 and smaller than 150

n = int(input("Enter a number: "))
    
for i in range(n):
    if (1 <= int(n) <= 150):
        print(i+1, end='')
    else:
        print("out of range")

#Quiz 5 An extra day is added to the calendar almost every four years as February 29, 
#and the day is called a leap day. It corrects the calendar for the fact that our planet 
#takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
#while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
#Task
#Given a year, determine whether it is a leap year. 
#If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN 
#and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

#year = int(input("Enter a year: "))

def is_leap(year):
    #logical path 1
    if (1900 <= int(year) <= 10e5) and (year % 4 == 0) and (year % 100 == 0) and (year % 400 == 0):
        leap = True
    #logical path 2
    elif (1900 <= int(year) <= 10e5) and (year % 4 == 0) and (year % 100 != 0):
        leap = True
    #logical paths 3 and 4
    elif (1900 <= int(year) <= 10e5) and (year % 4 !=0) or (year % 4 == 0 and year % 100 ==0 and year % 400 !=0):
        leap = False
    else:
        leap = False
    
    return leap #return must be outside the function

#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
#while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
#print(is_leap(year))
print(is_leap(1992))#error in the code here as it should return True and not False
print(is_leap(2000))#true
print(is_leap(2400))#true
print(is_leap(1800))#false
print(is_leap(2500))#false
print(is_leap(2300))#false

#Quiz #6 
#List
#What is the maximum difference between the integer pairs in an list
#[i, j, i,j,] starting at 0 position
#[i, j, i, j] starting at 1 position
#and so on

#x = [4,3,2,1]#nothing will update
x = [1,5,2,7]

def find_max_diff(x):
    best_j = 1
    best_i = 0
    max = x[1] - x[0]
    for j in range(len(x)):
        for i in range(j):
            if x[j] - x[i] > max:
                max = x[j]-x[i]
                best_j = j
                best_i = i

    return max, best_i, best_j

#test x =[4,3,2,1]
print(find_max_diff(x))#output is (6,0,3)

# Python3 code to demonstrate
# maximum difference pair
# using list comprehension + max() + combinations() + lambda
from itertools import combinations
 
# initializing list
test_list = [3, 4, 1, 7, 9, 1]
 
# printing original list
print("The original list : " + str(test_list))
 
# using list comprehension + max() + combinations() + lambda
# maximum difference pair
res = max(combinations(test_list, 2), key = lambda sub: abs(sub[0]-sub[1]))
 
# print result
print("The maximum difference pair is : " + str(res))
#this code does not use cascading sequence of i, j rotating through the list

#this code uses max difference between sequence of pairs in the list
def max_consecutive_diff(nums):
  max_diff = 0
  for i in range(len(nums) - 1):
    diff = abs(nums[i] - nums[i + 1])
    if diff > max_diff:
      max_diff = diff
  return max_diff

nums = [1,5,2,7]
print(max_consecutive_diff(nums))  # Output: 5

#Quiz  
#List
#What is the maximum difference between the integer pairs in an list

def max_difference(nums):
  """Finds the maximum difference between any two numbers in a list.

  Args:
    nums: The list of numbers.

  Returns:
    The maximum difference.
  """

  if len(nums) < 2:
    return 0

  max_diff = 0
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      diff = abs(nums[i] - nums[j])
      if diff > max_diff:
        max_diff = diff

  return max_diff

nums = [1, 2, 3, 8, 10]
print(max_difference(nums))#output = 6, this is correct.

#REFERENCE A CSV FILE IN CODE
## Read the csv file
#Get the corpus of text
#The combined dataset of reviews has been saved in a Google drive belonging to Udacity. You can download it from there.
#path = tf.keras.utils.get_file('reviews.csv',
#                              'https://drive.google.com/uc?id=13ySLC_ue6Umt9RJYSeM2t-V0kCv-4C-P')
#print (path)
#dataset = pd.read_csv(path)
#CHECK THIS TENSORFLOW COLAB
#https://colab.research.google.com/drive/1oB9-IBQTo8ac8nPZTwkdDK22Vzm1rN9X#scrollTo=kBpFip-X69Hf

#MACHINE LEARNING QUIZZES
#MACHINE LEARNING INTERVIEW CHECKLIST 
#SEVEN STEP PROCESS FOR SUCCESSFUL MACHINE LEARNING INTERVIEW
#CLARIFYING THE QUESTION, GENERATING INPUTS AND OUTPUTS, GENERATING TEST CASES,
# BRAINSTORMING, RUNTIME ANALYSIS, CODING, DEBUGGING
#https://docs.google.com/document/d/e/2PACX-1vSYBV2l-IUU8rFPa6ldB5CSCrrnz_czoVMGN5G2hRRjfUjlG82a-tif0sO4QUF_MBkgeOj6U44ACOqM/pub
#Quiz  
#Spam Classfication on email algorithm using Machine Learning

#email = sender address, ip address, title, attachments, time and date sent, recipients, body, reply, forward
#sender address - is this in the address book or has the recipient received an email before
#known/unknown list, spammers list
#ip address by country, and prevalence of spam from the country
#Naive Bayes can handle checking both text and binary in an algorithm

#https://docs.google.com/document/d/e/2PACX-1vQa4quKMxBWnMe42emXY6P57p-2zJD3hcwCUKlQkZfEf5mI5MzRyxsjwMzOG7orNb55qYeKWRDI65zs/pub

#QUIZ - RAINY WEATHER PROBABILITY USING BAYES RULE
#OVER THE LAST MONTH, OVER 20 OF THE DAYS WERE CLOUDY
#OUT OF THOSE 20 DAYS, IN 5 DAYS IT ACTUALLY RAINED
#IF IT IS CLOUDY OUTSIDE, WHAT IS THE PROBABILITY THAT IT WILL RAIN
#P(A/B) = (P(B/A)*P(A))/P(B)
#MONTH HAS 30 DAYS
#CLOUDY WEATHER = 20 DAYS/30 DAYS
#RAINY WEATHER = 5 DAYS DURING CLOUDY DAYS
#C = CLOUDY
#R= RAINY
#P(R/C) = (P(C/R)*P(R))/P(C)
#P(R/C) = 5/20 = 1/4
#P(C)=20/30 = 2/3
#P(R) = 5/30 = 1/6
#P(C/R)*P(R)/P(C) = 


#QUIZ - IDENTIFY FISH
#QUIZ - PLAIGARISM DETECTION
#QUIZ - Reduce Data Dimensionality

# 6 - FIND NUMBER OF ISLANDS IN A MATRIX

from collections import

M =([1,0,1],[0,1,0])

def islandcounter(M):
    if (M == 0 or M == [[]]):
        return 0
    islands = 0
    c = len(M[0])
    r = len(M)
    for i in range(0,r):
        for j in range(0,c):
            if (M[i][j]==1):
                islands += 1
#                findpartsofisland(M,i,j,r,c)
    return islands  

print(islandcounter(M))#output is 3

def findpartsofisland(m,i,j,r,c):

    q = queue
    q.append([i.j])
    while(len(q)!=0):
        i=q.pop()
        x=i[0]
        y=i[1]
        if (M([x][y]==1):
            M[x][y]==2

defappendif(q,r,c,x,y):
#    if (x>0) and 
#CANNOT READ ON THE SCREEN THE REST OF THE CODE

#PHONE INTERVIEW QUESTIONS FOR A SDEE POSITION 
#https://sites.google.com/site/steveyegge2/five-essential-phone-screen-questions


#TIC TAC TOE GAME

#QUIZ 7

#list comprehensions! 
#You are given three integers X,Y,Z,N  and representing the dimensions of a cuboid along with an integer N . 
#Print a list of all possible coordinates given by I,J,K on a 3D grid where the sum of  is not equal to I+J+K IS NOT EQUAL TO N . 
#Here, 0<=I<=X, 0<=J<=Y. 0<=K<=Z. 
#Please use list comprehensions rather than multiple loops, as a learning exercise.
#Example X=1, Y=1, Z=2, N=3
##[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]

#Print an array of the elements that do not sum to n=3.

#[[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,2]]#not sure about the last one. 


#Input Format

x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
z = int(input("Enter value of z: "))
n = int(input("Enter value of n: "))

three_d_list = [[0,0,0], [0,0,1], [0,0,2], [0,1,0], [0,1,1], [0,1,2], [1,0,0], [1,0,1], [1,0,2], [1,1,0], [1,1,1], [1,1,2]]

print (three_d_list[0])#output is [0, 0, 0] 
print (len(three_d_list))#counts the number of elements in the list
print(sum(len(v) for v in three_d_list))#counts the total number of items in the list

#THIS FUNCTION DOES NOT EXECUTE
def sum_and_check(three_d_list, n):
#    """
#    Sums elements in a 3D list and prints elements where the sum is not equal to n.
#
#   Args:
#        lst: A 3D list of numbers.
#        n: The number to compare the sum against.
#   """

    for i in range(len(three_d_list)):
        for j in range(len(three_d_list[i])):
            for k in range(len(three_d_list[i][j])):
                current_element = three_d_list[i][j][k]
                # Calculate sum of the current element's "coordinates"
                element_sum = i + j + k
                if element_sum != n:
                    print(f"Element at index [{i}][{j}][{k}] = {current_element}, sum of indices = {element_sum} (not equal to {n})")
                    print(current_element)

    return(current_element)

#b = [sum(x) for x in matrix]
#if b!= n:
#    print(matrix[x])#output is [0,0,1]

# Initialize a result list with zeros
#result_list = [0] * len(matrix[0])

# Add elements from each list
#for l in matrix:
#    for i in range(len(l)):
#       result_list[i] += l[i]
#       if result_list[i] != n:

#            print(matrix[i])



#for i in range(len(matrix)):
#   for j in range(len(matrix[i])):
#        for k in range(len(matrix[i][j])):
#            sum=i+j+k
#            if sum != n:
#                print(matrix[i][j][k])

#for i in range(len(matrix[0])) and j in range(len(matrix[1])) and k in range(len(matrix[2])):
#   sum=i+j+k
#  if sum != n:
#         print(matrix)   

#b = [sum(x) for x in matrix]
#print(b)#output is [0, 1, 2, 1, 2, 3, 1, 2, 3, 2, 3, 4]



#THIS CODE WORKS!
#x = [i for i in range(x+1)]
#y = [i for i in range(y+1)]
#z = [i for i in range(z+1)]
# for each combination of i,j,k will form a sublist in the final_list, and sum of i,j,k will not equal to n
#final_list = [[i,j,k]for i in x for j in y for k in z if (i+j+k)!=n]
#print(final_list)#inputs = 1,1,1,2 output is [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


#list comprehension for 3D matrix with sum of i j and k values python


#QUIZ #8
#Given the participants' score sheet for your University Sports Day, 
#you are required to find the runner-up score. 
#You are given  scores. Store them in a list and find the score of the runner-up.

#Input Format
#The first line contains N. 
#The second line contains an array[]  of N integers each separated by a space.

#OUTPUT FORMAT
#Print the runner-up score.

#Given list is [2,3,6, 6,5]. The maximum score is 6, second maximum is 6. 
#Hence, we print 5 as the runner-up score.

n = int(input())
arr = map(int, input().split())

#n = int(input("Enter the first number: "))
arr = [2,3,6,6,5]

#n = int(input())
#arr = map(int, input().split())

largest=max(arr)
print(largest)

array = [2,3,6,6,5]

#THIS CODE WORKS
# Initialize largest (max1)
# and second largest (max2) to negative infinity
max1 = max2 = -100 #float('-inf')use negative 100

# Loop through each number in list
for n in array:
  
    # If the current number is greater 
    # than largest found so far
    if n > max1:
        #when n=0, for this array, the value 2 is greater than max1
        # Update second largest to the previous largest
        max2 = max1  
        #max2 = negative 100
        # Update largest to the current number
        max1 = n     
        #max1 becomes the array value 2
    # If current number is less than largest
    # but greater than second largest
    elif n > max2 and n != max1:
    #when n=0, for this array,the array value 2is greater than -100, but the array value is equal to max1 which is 2
     # Update second largest to current number
     #this does not get updated when the array value is 2.
        max2 = n  

print(max2)

#QUIZ 9
#SECOND LOWEST GRADE

#Given the names and grades for each student in a class of N students, 
#store them in a nested list and print the name(s) of any student(s) 
#having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, 
#order their names alphabetically and print each name on a new line.
#Example
#Records = [[“chi”, 20.0], [“beta”, 50.0], [“alpha”, 50.0]]

#The ordered list of scores is [20.0, 50.0] , so the second lowest score is 50.0. 
#There are two students with that score: [“beta”, “alpha”]. 
#Ordered alphabetically, the names are printed as:
#alpha
#beta

#Input Format
#The first line contains an integer, N the number of students. 
#The  subsequent lines describe each student over  lines. 
#- The first line contains a student's name. 
#- The second line contains their grade. 
#Constraints
#There will always be one or more students having the second lowest grade. 
#Output Format
#Print the name(s) of any student(s) having the second lowest grade in.
#If there are multiple students, order their names alphabetically and print each one on a new line.

#Sample Input 

#5
#Harry
#37.21
#Berry
#37.21
#Tina
#37.2
#Akriti
#41
#Harsh
#39

#Explanation 
#There are 5 students in this class whose names and grades are assembled to build the following list:

#python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

#The lowest grade of 37.2 belongs to Tina. 

#The second lowest grade of 37.21 belongs to both Harry and Berry, 
#so we order their names alphabetically and print each name on a new line.

#Berry
#Harry




