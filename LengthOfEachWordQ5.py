#Q5. Write a Python program that uses the map() function to 
# calculate the length of each word in a list of strings.


li=["Stack","full","stackoverflow","indexmatch","honesty"]


x=list(map(lambda x:len(x),li))
print(x)

