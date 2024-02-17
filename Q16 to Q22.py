#Explain the purpose of the filter() function in Python and provide an example of how it can be used to filter elements from an iterable.

"""filter() function is used to filter elements from an iterable based on a given function. 

It takes two arguments - function that defines the filtering condition and the iterable to be filtered.

filter(function, iterable)


def is_even(n):
    return n % 2 == 0

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(is_even, n)))

"""

#Write a Python program that uses the filter() function to select even numbers from a list of integers.

"""li=[1,2,5,7,9,10,12,15,20,17,19,18,22,23,24,25]

print(list(filter(lambda x:x%2==0,li)))"""


#Create a Python program that uses the filter() function to select names that start with a specific letter from a list of strings.

"""li=["Ajay","Vijay","Sanjay","Naveen","Deep","Singh","Anil","Anajana"]

def letter(x):
    if x[0]=="A":
        return x
    else:
        return 0


print(list(filter(letter,li)))"""

#Write a Python program that uses the filter() function to select prime numbers from a list of integers.


"""def is_prime(n):
    if n <= 1:
        return 0
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return 0
    return 1

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print(list(filter(lambda x: is_prime(x), numbers)))"""




#How can you use the filter() function to remove None values from a list in Python?

"""li=[1,2,5,6,9,None,10,22,None,28,None]

print(list(filter(lambda x:x!=None,li)))"""





#Create a Python program that uses filter() to select words longer than a certain length from a list of strings.

"""li=["Ajay","Vijay","Sanjay","Naveen","Deep","Singh","Anil","Anajana"]

def is_len(x):
    if len(x)>4:
        return 1
    else:
        return 0

print(list(filter(lambda x: is_len(x), li)))"""


#Write a Python program that uses the filter() function to select elements greater than a specified threshold from a list of values. Recursion:-

"""li=[20,30,10,9,39,182,7,21,129]

def is_thres(x):
    if x>15:
        return 1
    else:
        return 0

print(list(filter(lambda x: is_thres(x) ,li)))"""

