#Q2: example of map function to square the iterable.


def square(x):
    return x*x


li=[1,2,3,4,5]

print(list(map(square,li)))