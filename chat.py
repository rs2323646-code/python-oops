# is_park=True
# is_sir=False
# print(is_park)
# print(is_sir)
# print(type(is_park))
# print(type(is_sir))

# age=2
# if age <10:
#     print("younger")
# else:
#     print("older")
# marks =87
# if marks<=87:
#     print("a")
# elif marks>=33:
#    print("b")
# else:
# #     print("f")

# age =20
# if age <18 and age>=33:
#     print("eligable")




# i = 1

# while i <= 5:
#     print(i)
#     i += 1


# student = {
#     "name":"Rohit",
#     "age" : 18,
#     "course" : "bca"
# }
# print(student.keys())
# print(student.values())


# # student = {
#     "name": "Rohit",
#     "age": 18,
#     "course": "bca"
# }
# print(student.items())
# print(student.keys())
# print(student.values())

# nums = [2, 7, 11, 15]
# target = 9

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print([i, j])


# num1 = float(input("Enter first number: "))
# operator = input("Enter operator (+, -, *, /): ")
# num2 = float(input("Enter second number: "))

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#     elif operator == "%":
#         if num2 !=0:
# #             result =num1 % num2
# #         else:
# #             result = "Cannot divide by zero!"
# #     else:
# #      result = "Invalid operator!"

# # print("Result:", result)



# create a function greet() that prints[hello world]

# def greet():
#     print("hello world")
# greet()

# Create a function welcome() that prints "Welcome to Python"

# def welcome():
#     print("Welcome to python ")
# welcome()

# Create a function square(n) that prints the square of n

# def square(n):
#     print(n * n)

# square(12)

# Create a function cube(n) that returns the cube of n

# def cube(n):
#     print(n * n * n)

# cube(5)

# Create a function add(a, b) that returns the sum

# def add(a,b):
#     print(a+b)

# add(2,7)

# Create a function subtract(a, b) that returns the difference.

# def sub(a, b):
    # print(a - b)

# sub(7, 4)

# Create a function is_even(n) that returns True if the number is even.

# def is_even(n):
    # return n % 2 == 0

# print(is_even(8))

# Create a function maximum(a, b) that returns the larger number.
 
# def maximum(a,b):
#     if a > b:
#         return a
#     else:
#         return b
# print(maximum (10, 20))

# create greet(name) that prints Hello, <name>.
# def greet(name):
#       print("hello",name)
 
# greet("Rohit")

# Create multiply(a, b) that returns multiplication.
# def multiply(a,b):
#     return a*b
# print(multiply(2,2))

# Create student(name, age) that prints both values.
# def student(name,age):
#     print("Name",name)
#     print("age",age)
# student("Rohit",20)

# Create area(length, width) that returns the area of a rectangle.
# def area(length,width):
#     return(length*width)
# print(area(10,76)) 

# Create check_age(age) that prints whether a person is eligible to vote.
# def check_age(age):
#    if age >= 18:
#        print("eligibale to vote ")
#    else:
#        print("not eligible to vote ")
# check_age(20)

# Create calculate_average(a, b, c) that returns the average.
# def calculate_average(a,b,c):
#     return (a + b + c)/3
# print(calculate_average(10,30,20))

# Create greet(name="Guest") that prints a greeting.
# def greet(name="Guest"):
#     print("Henerry", name)

# greet()

# # Create power(num, exponent=2) that returns num raised to exponent.
# def power(num, exponent=2):
#     return num ** exponent

# print(power(5))

# Create bill(amount, tax=18) that calculates the amount including tax.
# def bill(amount,tax=18):
    
    



# Create student(name, course="Python") that prints the student's name and course.
# def student(name,course="python"):
#     print("Name", name)
#     print("Course", course)
# student("Rohit")

# Create login(username, role="user") that prints username and role.
# def login(username, role="user"):
#     print("Username",username)
#     print("Role",role)
# login("Rohit")

# #Create discount(price, discount=10) that returns the final price after discount.  





# x = 66
# y = 44
# total = 0

# for i in [x, y]:
#     total += i

# print(total) 

# x= lambda a,b,c: a+b+c;
# print(x(1,2,3))

def func(n):
    return lambda a:a*n
my_doubler=func(2)
print(my_doubler(12))


