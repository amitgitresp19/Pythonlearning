
#How can you use the map() function to apply a custom function to elements of multiple lists simultaneously in Python?

"""
li1=[1,2,3,4,5]
li2=[2,2,2,2,2]

print(list(map(lambda x,y:x+y,li1,li2)))

"""

#Create a Python program that uses map() to convert a list of temperatures from Celsius to Fahrenheit.
# c*9/5+32
""""
Celtemperature=[23,27,33.6,41.8,39.8]

print("Celsius to Frenheit:",list(map(lambda x:(x*9/5)+32,Celtemperature)))

"""

#Write a Python program that uses the map() function to round each element of a list of floating-point numbers to the nearest integer. Reduce :-

"""
from functools import reduce
floatnum=[23.789,27.849,33.62,41.1,53.39]

p=list(map(lambda x:round(x),floatnum))
print(p)

print(reduce(lambda x,y:x+y,p))

"""

#What is the reduce() function in Python, and what module should you import to use it? Provide an example of its basic usage.

#The reduce() function used to apply a function of two arguments of iterable items from left to right, 
#and reduce the iterable to a single value.
#functools module to import reduce.
#
"""

from functools import reduce as rd

li=[1,2,3,4,5]
#Multiple items to single item
print(rd(lambda x,y:x+y,li))

"""


#Write a Python program that uses the reduce() function to find the product of all elements in a list.

"""
from functools import reduce as rd

li=[1,2,3,4,5]
#Multiple items to single item
print(rd(lambda x,y:x*y,li))
"""