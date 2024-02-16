#Create a Python program that uses reduce() to find the maximum element in a list of numbers.

"""from functools import reduce as rd

li=[10,1280,583,302,49,928]

print(rd(lambda x,y: x if x>y else y,li))"""




#How can you use the reduce() function to concatenate a list of strings into a single string?

"""from functools import reduce as rd

li=["My","Name","Is","Captain","Jacks","Sparrow"]

print(rd(lambda x,y: x+y,li))"""

#o/p = MyNameIsCaptainJacksSparrow


#Write a Python program that calculates the factorial of a number using the reduce() function.

"""from functools import reduce as rd

n=5

print(rd(lambda x,y:x*y, range(1,n+1),1))"""

#Create a Python program that uses reduce() to find the GCD (Greatest Common Divisor) of a list of numbers.

"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcdli(numbers):
    return reduce(gcd, numbers)


numbers = [24, 36, 48, 60]
print(gcdli(numbers))"""



#Write a Python program that uses the reduce() function to find the sum of the digits of a given number. Filter :-


"""from functools import reduce as rd

def sum(num):
    digits = filter(str.isdigit, str(num))
    return rd(lambda x, y: int(x) + int(y), digits, 0)


print(sum(115))"""