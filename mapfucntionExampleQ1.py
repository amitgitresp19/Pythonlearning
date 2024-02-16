#The map() function is used to apply a specified function to every item in an iterable
# (like a list, tuple, or dictionary) and returns a new iterable results. 


def sumitself(x):
    return x+x 


li=[1,2,3,4,5]

print(list(map(sumitself,li)))