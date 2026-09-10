# def sum(a,b):
#      return  a+ b
# print(sum(6,8))

# def cal_average(a, b , c):
#      sum= a + b+ c
#      avg= sum/3
#      print(avg)
# cal_average(5,6,7)

# num =["hello","no"," yes","there"]
# print([0] ,end="")
# print([1] , end="")

# def print_len(list):
#      for item in list:
#           print(item,end=" ")
# print()
# print_len(num)

# n = 10 
# fact = 1

# for i in range(1, 6):
#     fact *= i

# print(fact)

# def cal_fac(n)
#      fact= i
#      for i in range(1,+1):
#         fact*=1
# print(fact)
# cal_fac(5)


# def cal_fac(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact *= i

#     return fact

# print(cal_fac(5)) 

# def convert(usd_val):
#      inr_val=usd_val*83
#      print(usd_val,"USD=", inr_val,"INR")

# convert(100000)

# #  input a number add even output string function even 



# # def my_function(*args):
# #   print("The youngest child is " + args[1])
 
# # my_function("Emil", "Tobias", "Linus")

# def my_school(*args):
#     print("schol wherre place  "+args[2])

# my_school("nadaun","badarn","hamirpur")


# x= 300 
# def function():
#     global x
#     x=200

# function()

# print(x)


# 
# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)



# def my_fun1():
#      x="jan"
#      def my_fun2():
#           nonlocal x
#           x ="hello"
#      my_fun2()
#      return x
# print(my_fun1())





# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)

# number=[2,8,9,0,3,4,6,7,88]
# even=list(filter(lambda x :x % 2 ==0, number))
# print("Even number", even)

# city=["jaipu", "delhi","rajasthan","mandi","panjab"]
# def length(city):
#     return len(city)
# sort = sorted(city,key=length)
# print("sorted words by length",sort)



# city=["delhi","oman","paris","egypt","isral"]
# sort=sorted(city,key=lambda x :len(x),reverse=True)
# print("sorted word by length",sort)


# for i in range(10):
#     print(i)

x = 20

for i in range(9):
    if x > i:
        print(x - i)
 