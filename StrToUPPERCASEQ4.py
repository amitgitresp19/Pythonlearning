#Q4.Create a Python program that uses the map() function to convert a list of names to uppercase.

# convert to uppercase:
def upper(x):
    return x.upper()


li=["Stack","full","stackoverflow","indexmatch","honesty"]

print(list(map(upper,li)))

#method 2:

#print(list(map(lambda x:x.upper(),li)))