#syntax

# always defined using def 


# def function_name(parameter1,parameter_n)
    # function body 

# function_name(4,3)


# Types of function 
# userdefined function(user create)
# inbuilt function (print(),max(),min())


# without return type 
# def abhi():
#     x = int(input())
#     y = int(input())
#     z = x % y
#     print(z)
# # calling function 
# abhi()


# Return type 
# def abhi():
#     x = int(input())
#     y = int(input())
#     z = x % y
#     print(z)
#     return z
# print(abhi())

# ******************Arguments***********************
# default argument 
# def sub(a=5,b=6):
#     return a+b
# print(sub())
# print(sub(10,5))


# Positional argument 
# def  add(a,b):
#     return a+b

# x = add(5,5)
# print(x)

# # keyword argument 
# def add(a,b):
#     return a+b

# x = add(b=6, a=5)
# print(x)

# giving a sequence in the argument 
# first we need to unpack it 

# def print_name(a,b,c,d,e):
#     print(a,b,c,d,e)
# list_1 = [1,2,3,4,5]
# print_name(*list_1)



# def diction(name="name",age="age"):
#     print(name,age)
# dick={"name":"kk","age":22}
# # unpacking dictionary 
# diction(**dick)


# ********************************QUESTION*********************************
# write a program to receive three integers from keyboard and get their sum and product calculated through user defined function.

# def sum_product():
#     x= int(input())
#     y = int(input())
#     z = int(input())
#     w = f"The sum is: {x+y+z} the product is:  {x*y*z}"
#     return w
# print(sum_product())



# *****************using Positional argument 

# def sum_product(x,y,z):
#     return x+y+z, x*y*z
# x=int(input())
# y = int(input())
# z=int(input())
# print(sum_product(x,y,z))


# ******************keyword argument 
# def sum_product(x,y,z):
#     return x+y+z, x*y*z
# w=int(input())
# u = int(input())
# v=int(input())
# print(sum_product(x=w,y=u,z=v))


                 
