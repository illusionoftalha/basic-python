# Use the CMD version of Python to execute this
#open() function

# f = open("Days.txt", "r")

#readline() function

# f = open("Days.txt", "r")
# data = f.readline()
# print(data)

#readlines() function

# f = open("Days.txt", "r")
# data = f.readlines()
# print(data)

#write() funtion

# f = open("Days.txt", "r+")
# f.write("These are Weekdays\n")
# data = f.readlines()
# print(data)

#close() function

# f = open("Days.txt", "r+")
# f.write("These are Weekdays\n")
# data = f.readlines()
# print(data)
# f.close()

#working with the modules

# import random # here the module is "random"
# print('Random Number 1 =>', random.random())
# print('Random Number 2 =>', random.random())

#random.randit() method

# print(random.randint(3,9))

#random.randrange() method

# print(random.randrange(3,9))

# shuffle() method

# list = [10,6,4,11,1]
# random.shuffle(list)
# print(list)

# choices() method

# numList = [151, 251, 351, 451, 551]
# print(random.choices(
#     numList, weights=(10,20,30,40,50), k=5
# ))

# This all was about (import random)

# Now we are going towards (import statistics)

# Some Basic Information On Basic OPerations in Python
# Median: The middle number or midpoint of the data, when the numbers are listed in ascending order.
# To find the median, place the number in value order and find middle number.

# Mode: The mode is the value that occurs most often.
# if no number in the list is repeated, then there is no mode for the list.

# import statistics # statistics is module here

# mean(), median(), mode() method

# scores = [1,2,9,2,9,10,9,7]
# a = statistics.mean(scores)
# b = statistics.median(scores)
# c = statistics.mode(scores)
# print("Mean:", a,"Median:", b, "Mode:",c,)

# median_low() method

# list1 = [20,40,60,80,100]
# list2 = [30,70,90]
# a = statistics.median_low(list1)
# b = statistics.median_low(list2)
# print("Low Median:", a, "Low Median:",b)

# median_high() method

# list1 = [20,40,80,100]
# list2 = [30,90]
# a = statistics.median_high(list1)
# b = statistics.median_high(list2)
# print("High Median:", a, "High Median:",b)

# Let me tell you something about Variance:
# Variance in statistics refers to the average of the squared dufferences from the mean.
# In other words, how varied is the data? Does it vary a lot, in that say we have one grade of say 20, another
# that's 99, and another that's like 50? Are the grades very varied? or are they fairly close together?
# Before even running the code we can conclude that our grades are fairly similar.
# let's go towards the

# variance() method

# grades = [70,90,50,85,65,83,94]
# gradesmean = statistics.mean(grades)
# print(statistics.variance(grades,gradesmean))

# Somethings you should know about Standard Deviation:
# Standard deviation is used to show how much variation from the mean exists.
# You can think of it as a typical deviation from the mean.
# A low standard deviation indicates that the values tend to be close to the mean of the set,
# while a high standard deviation indicates that the values are spread out over a wider range.
# Fun fact for the math geeks. The standard deviation is actually the square root of the variance.

# stdev() method

# grades = [89, 91, 95, 92, 93, 94, 98, 90]
# stdevgrades = statistics.stdev(grades)
# print("The Standard deviation of the list is: ", stdevgrades)

# import time # Here time is module

# time() method

# currtime = time.time()
# print(currtime)

# ctime() method

# epochtime = 1673199458.3812485
# localtime = time.ctime(epochtime)
# print(localtime)

# Topic change, here are some types of exceptoions in Python
# ZeroDivisionError: It is traced when you try to divide a number with 0.
# ImportError: It is raised when you try to import the library that is not installed or you have provided a wrong
# name.
# IndexError: Raised when an index is not found in a sequence. For example, if the length of the list is 10
# and you are trying to access the 11th index from that list, you'll get this error.
# IndentationError: Raised when indentation is not specified properly
# ValueError: Raised when the built-in function for a data type has the valid type of arguments,
# but the arguments have invalid values specified
# Exception: Base class for all exceptions. If you are not sure about,
# which exception may occur, you can use the base class. It will handle all of them
# Type Error - Happens when an incorrect type of function or operation is applied to an object.

# Exception is not an EXAMPLE!
# You may be wondering why would we want to hndle these exceptions? How is this helpful?
# By handling exceptions, an alternative flow of execution to avoid crashing your program unexpectedly.
# For example: print(Language) this ine will give us the NameError: name Language is not defined.
# We will handle it like this:

# exceptions method

# try:
#     print(language)
# except NameError as e:
#     print("Some error has occured")

# using finally in exception method

# try:
#     print(language)
# except NameError as e:
#     print("Some error has occured")
# finally:
#     print("That was Good, man")

# thala = [80]
# try:
#     print(thala)
# except Exception:
#     print("thala is not defined")
# finally:
#     print("Hell, yeah")

# Whether the output is Executed or it has an error the (finally) will always be executed.

# raising exceptions in Python

# def fiveletter(data):
#     if len(data) != 5:
#         raise ValueError("You got that wrong!!")
#     for item in data:
#         print(item)
# fiveletter([1])

# Writing Regular Expression in python
# first take R from Regular and E from Expression, then write,
# import re

# findall method

import re # Here re is module
# def findall():
#     string = "Hello World"
#     print(re.findall("Hello", string))
# findall()

# identifier

# def findall():
#     string = "Hello World x10"
#     print(re.findall("\d", string))
# findall()

# Using modifier

# def findall():
#     string = "I love you 3000"
#     print(re.findall("\d+", string))
# findall()

# search() method

# def search():
#     if re.search("awesome", "isn't this an awesome view?"):
#         print("You Are Awesome!")
#         return
# search()

# split() method

# def split():
#     result = re.split("s","Awesome")
#     print(result)
# split()

# Starting MySQL:
# Introduction to SQL:
# Almost anything you can think of could benefit from some type of database, from bare bones to elaborate.
# Cataloging literally anything: rock collection, stamp collection, comic collection and etc.
# Tracking progress on literally anything: Weight loss, running speed, weight lifting and etc.
# Various other things: documenting who you've loaned things to, organizing bills nd etc.

# MySQL is an open-source relational database management system. MySQL stoes data in tables.

# Optional MySQL notes only; not required by the guided course:
# import mysql.connector
# it takes 3 required parameters 'host', 'user' and 'passwd'
# note that you'll have to download the MySQL app in your pc and have to set up the all process
# def sqlconn():
#     db = mysql.connector.connect(
#         host = "localhost",
#         user = "YOUR_DATABASE_USER",
#         passwd = "YOUR_DATABASE_PASSWORD"
#     )
#     print(db)
# sqlconn()

# I won't be continuing this so this is the Goodbye Mates!!
