import math 

#Function for addition
def add(x,y):
    result = x + y
    return result

#Function for substraction
def sub(x,y):
    result = x - y
    return result

#Function for multiplication
def mul(x,y):
    result = x*y
    return result

#Function for devision 
def dev(x,y):
    result = x/y
    return result

#Function for getting the power
def pow(x,y):
    result = x**y
    return result

#Function for getting the sqare root
def root(x):
    if x < 0:
        print("There's no square root for negetive numbers!")
    else:
        result = math.sqrt(x)
    return result

#Function for getting the sine value
def sine(x):
    result = math.sin(math.radians(x))
    return result

#Function for getting the cosine value 
def cos(x):
    result = math.cos(math.radians(x))
    return result

#Function for getting the tangent value
def tan(x):
    result = math.tan(math.radians(x))
    return result
