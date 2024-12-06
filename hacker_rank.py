

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

#Quiz  
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

#Quiz  
#Spam Classfication on email algorithm using Machine Learning

#email = sender address, ip address, title, attachments, time and date sent, recipients, body, reply, forward
#sender address - is this in the address book or has the recipient received an email before
#known/unknown list, spammers list
#ip address by country, and prevalence of spam from the country
#Naive Bayes can handle checking both text and binary in an algorithm

#https://docs.google.com/document/d/e/2PACX-1vQa4quKMxBWnMe42emXY6P57p-2zJD3hcwCUKlQkZfEf5mI5MzRyxsjwMzOG7orNb55qYeKWRDI65zs/pub