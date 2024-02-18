#Explain the concept of recursion in Python. How does it differ from iteration?

"""Recursion is function calls itself in order to solve a problem.
It's a powerful tool that allows a function to break down a 
problem into smaller, more manageable subproblems.

Each recursive call typically operates on a smaller subset of the original problem 
until a base case is reached, at which point the function stops calling itself and 
starts returning values back up the call stack.

Both recursion and iteration involve repetitive execution of a set of instructions. 
However, recursion is more about solving a problem in terms of smaller 
instances of the same problem, while iteration is about executing a set of instructions 
repeatedly until a certain condition is met."""

#Write a Python program to calculate the factorial of a number using recursion.

"""def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))"""

#Create a recursive Python function to find the nth Fibonacci number.

#fibonacci
# 0 1 1 2 3 5 8 ...

"""def fib(x):
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fib(x-2)+ fib(x-1)


print(fib(7))"""
    

#Write a recursive Python function to calculate the sum of all elements in a list.

"""def sum(x):
    if len(x)==0:
        return 0
    else:
        return x[0] + sum(x[1:])

li=[1,2,3,4,5]

print(sum(li))"""

#How can you prevent a recursive function from running indefinitely, causing a stack overflow error?

"""To prevent a recursive function from running indefinitely is by implementing a termination condition. 
This condition should be based on some criteria that, when met, 
stops the recursion from continuing further.
"""
#Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

"""def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, 18)) """

#Write a recursive Python function to reverse a string.

"""def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))"""

#Create a recursive Python function to calculate the power of a number (x^n).

"""def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 3))"""

#Write a recursive Python function to find all permutations of a given string.

"""def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i, char in enumerate(s):
            remaining_chars = s[:i] + s[i+1:]
            subperms = permutations(remaining_chars)
            for perm in subperms:
                perms.append(char + perm)
        return perms

# Example usage:
print(permutations("abc")) """

#Write a recursive Python function to check if a string is a palindrome.

"""def is_palindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

# Example usage:
print(is_palindrome("radar"))"""

#Create a recursive Python function to generate all possible combinations of a list of elements. 

"""def combinations(elements):
    if len(elements) == 0:
        return [[]]  # Return a list containing an empty list as the base case
    else:
        head = elements[0]  # First element of the list
        tail = elements[1:]  # Rest of the elements
        combinations_without_head = combinations(tail)  # Recursive call without the head
        combinations_with_head = []
        for combo in combinations_without_head:
            combinations_with_head.append(combo)  # Add combinations without the head
            combinations_with_head.append([head] + combo)  # Add combinations with the head
        return combinations_with_head

# Example usage:
print(combinations([1, 2, 3]))"""

# 1. Write a program to reverse a string.

"""strr="Stack"

for i in range(len(strr)-1,-1,-1):
    print(strr[i],end="")"""



#Check if a string is a palindrome.

"""strr="stacats"
l=len(strr)-1
count=0
for i in range(0,len(strr)//2,1):
    if strr[i]==strr[l]:
        l=l-1
        count=count+1
    
if count>0:
    print("String is palindrome")
else:
    print("Not palindrome")"""


#Convert a string to uppercase.

"""strr="stack"
print(strr.upper())"""

#Convert a string to lowercase.

"""strr="stack"
print(strr.lower())"""


#Count the number of vowels in a string.

"""strr="abcdefgijklmn"
vowels="aeiou"
count=0
for i in range(len(strr)):
    if strr[i] in vowels:
        count=count+1

print("No. of Vowels:", count)"""


#Count the number of consonants in a string.

"""strr="abcdefgijklmn"
conso="aeiou"
count=0
for i in range(len(strr)):
    if strr[i] not in conso:
        count=count+1

print("No. of Consonants:", count)"""


#Remove all whitespaces from a string.

"""strr="ab cdefgi jklmn "
spaces=" "
count=0
for i in range(len(strr)):
    if strr[i] in spaces:
        count=count+1

print("No. of Whitespaces:", count)"""


#Find the length of a string without using the len() function.

"""strr="stack"
c=0
for i in strr:
    if i == strr[-1]:
        break
    else:
        c=c+1

print(c+1)"""

#Check if a string contains a specific word.

"""strr="Brillica provides analyst course"
find="data"
c=0
if find in strr:
    c=c+1

if c>0:
    print("Yes Specefic String is present")
else:
    print("No present")"""

#Method 2 = str.find()===============
# find() function mei -1 ka mtlb word not word not there
# find() gives any other word means it found.

"""strr="Brillica provides data analyst course"
findd="data"

if strr.find(findd)!=-1:
    print("Yes Specefic String is present")
else:
    print("No present")"""



#Replace a word in a string with another word.

"""strr="Brillica provides dataa analyst course"
findd="dataa"
replacee="Data"

print(strr.replace(findd,replacee))"""

#Count the occurrences of a word in a string.

"""strr="Brillica provides data analyst course"
spa=0
for i in range(len(strr)):
    if strr[i]==" ":
        spa=spa+1


print("No of words",spa+1)"""


#Find the first occurrence of a word in a string.

"""strr="Stack is full of solutions"
for i in range(len(strr)):
    if strr[i]==" ":
        break
    print(strr[i],end="")"""

#Find the last occurrence of a word in a string.
    
"""strr="Stack is full of solutions"
for i in range(len(strr)-1,-1,-1):
    if strr[i]==" ":
        break
    print(strr[i],end="")"""

#Split a string into a list of words.

"""strr="Stack is full of solutions"

li=strr.split()

for i in range(0,len(li),1):
    print(li[i])"""


#Join a list of words into a string 

"""strr=["Stack", "is","sequence", "or", "order"]
print(strr)
li=""
for i in range(len(strr)):
    li=li+" "+(strr[i])

print(li)"""


#List Based Practice Problem :

#Create a list with integers from 1 to 10.

"""li=[1,2,3,4,5,6,7,8,9,10]"""

#Find the length of a list without using the len() function.
"""
li=[1,2,3,4,5,6,7,8,9,10]
c=0
for i in range(li[-1]):
    c=c+1

print(c)"""

#Append an element to the end of a list.

"""li=[1,2,3,4,5,6,7,8,9,10]

li.append(11)
print(li)"""

#Insert an element at a specific index in a list.

"""li[2]=120
print(li)"""

#Remove an element from a list by its value.

"""li.remove(120)
print(li)"""

#Remove an element from a list by its index.

"""li=[1,2,3,4,5,6,7,8,9,10]
del li[2]
print(li)"""

#Check if an element exists in a list.

"""li=[1,2,3,4,6,7,8,9,10]
if 5 in li:
    print("Present")
else:
    print("not present")"""

#Find the index of the first occurrence of an element in a list.
"""
li=[1,4,5,8,9,5,4,3,10,15,5,10]
element=5

for i in range(len(li)):
    if li[i]==element:
        print(i)
        break"""

#Count the occurrences of an element in a list.
"""c=0
for i in range(len(li)):
    if li[i]==element:
        c=c+1

print(c)"""


#Reverse the order of elements in a list.

"""for i in range(len(li)-1,-1,-1):
    print(li[i],end=" ")"""


# 11. Sort a list in ascending order.
    
"""for i in range(len(li)):
    for j in range(len(li)):
        if li[i]<li[j]:
                 li[i],li[j] =li[j],li[i]

print(li)"""

#Sort a list in descending order.

"""for i in range(len(li)):
    for j in range(len(li)):
        if li[i]>li[j]:
                 li[i],li[j] =li[j],li[i]

print(li)"""

#Create a list of even numbers from 1 to 20.
"""p=[]
for i in range(1,20,1):
    if i%2==0:
        p.append(i)

print(p)"""


#Create a list of odd numbers from 1 to 20.

"""p=[]
for i in range(1,20,1):
    if i%2!=0:
        p.append(i)

print(p)"""

#Find the sum of all elements in a list.

"""li=[1,2,3,4,5]
c=0
for i in li:
    c=i+c
print(c)"""


#Find the maximum value in a list.
"""li=[17,29,49,20,123,193,583,12,29,11,5,215]
print(max(li))

for i in range(len(li)):
    for j in range(len(li)):
        if li[i]>li[j]:
            li[j],li[i]=li[i],li[j]
    
print(li[0])"""


#Find the minimum value in a list.

"""for i in range(len(li)):
    for j in range(len(li)):
        if li[i]<li[j]:
            li[j],li[i]=li[i],li[j]
    
print(li[0])"""

#Create a list of squares of numbers from 1 to 10.

"""li=[1,2,3,4,5]
ji=[]
for i in li:
    ji.append(i*i)
print(ji)"""

#Create a list of random numbers.

"""import random

x=[random.randint(1,20) for x in range(10)]
print(x)"""

#Remove duplicates from a list.
"""method 1:
li=[12,46,75,5,23,84,94,21,5,4,10,50,10]
p=[]
for i in li:
   if i not in p:
      p.append(i)

print(p)"""

"""
method 2:

li=set(li)
print(list(li))"""

#Find the common elements between two lists.

"""li1=[1,2,5,7,8,9]
li2=[1,2,7,8,3,11]
li3=[]

for i in li1:
    for j in li2:
        if i not in li3:
            li3.append(i)
        elif j not in li3:
            li3.append(j)

print(li3)"""

      


#Find the difference between two lists.

"""li1=[1,2,5,7,8,9]
li2=[1,2,7,8,3,11]
li3=[]



for i in range(len(li1)):
    li3.append(li1[i]-li2[i])


print(li3)"""

#Merge two lists.

"""li1=[1,2,5,7,8,9]
li2=[1,2,7,8,3,11]
li3=[]

for i in range(len(li1)):
    li3.append(li1[i])
    li3.append(li2[i])

print(li3)"""

#Multiply all elements in a list by 2.

"""li=[1,2,5,7,8,9]"""

"""for i in range(len(li)):
    li[i]=li[i]*2
print(li)
"""

"""x=[x*2 for x in li]
print(x)"""


"""print(list(map(lambda x:x*2,li)))"""

