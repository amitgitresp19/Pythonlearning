#Q3 Difference between list comprehension and map function
"""
The map() function and list comprehensions are works same to apply a transformation 
to each element of an iterable.

List comprehension:
x=7
y=8
list=[x if x>y else y]
arr=[1,2,3,4,5]
list1= [i*2 for i in arr]

Syntanx Difference:
>1map() takes a function and an iterable as arguments.
>1List comprehensions have a more compact syntax 
where the transformation logic and iteration are combined within square brackets.

Readability:
2>List comprehensions is more readable, simpler transformations, 
express the transformation and iteration in a single line.
2>map() requires defining a separate function, which might 
reduce readability in some cases, especially for short transformations.

Returning Object VS List:
>3map() returns a map object
List comprehensions directly produce a list.

>4.Map is Better When using built-in functions like len or str.upper

When to Use map():

You want to apply a function that already exists, especially built-in function.
You prefer map() in combination with other functional programming constructs like filter() or reduce().
For large datasets where the slight performance advantage matters.


When to Use list comprehensions :

The transformation logic is simple and can be expressed concisely.
Readability and simplicity are important.
You don't want to define separate functions for simple transformations.
You need the result directly as a list.



"""
