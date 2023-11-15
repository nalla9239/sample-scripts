
# sum = 1
# for a in ls:
#     sum = a * sum
#     print(f"Ans = {sum}")
# if sum == 1000:
#     print("YES")
# else:
#     print("NO")


# ls = [9,5,7,3]
# ls.append(1)
# ls.insert(0,6)
# print(ls)

# sum = 1
# for a in ls:
#     sum = a * sum
#     print(f"Ans = {sum}")
# if sum == 1000:
#     print("YES")
# else:
#     print("NO")




# name = input("what is your name  ")
# colour = input("fav colour  ")
# print(name +   " likes "   + colour)


# birth_year = input("what is your birth year?  ")
# age = 2023 - int(birth_year)
# print(age)

# weight_pounds = input("What is your weight in pounds? ")
# weight = 0.45359237 * float(weight_pounds)
# print(weight)

# output = """hi john,
# how are you"""
# print(output)

# 


# x = 10
# # x = x + 3
# x += 3
# print(x)

# x = (2 + 3) * 10 - 3
# print(x)

# x = 2.9
# print(round(x))
# print(abs(-2.9))



# ****if, elif, else loop****
# credit_score = 900
# if credit_score <= 700:
#     print("put down 10%")
# else:
#     print("put down 20%")

# good_credit = True
# if good_credit:
#     print("put down 10%")
# else:
#     print("put down 20%")


# good_credit = True
# price = 1000000
# if good_credit:
#     down_payment = 0.1 * price
    
# else:
#     down_payment = 0.2 * price
# print(f"Down payment = ${down_payment}")

# good_credit = True
# good_salary = True

# if good_credit and not good_salary:
#     print("Eligible")
# else:
#     print("Not Eligible")

# temperature = 20
# if temperature > 30:
#     print("It's a hot day")
# elif temperature < 10:
#     print("It's a cold day")
# else:
#     print("It's hot nor cold")


# name = input("name: ")
# if len(name) < 3:
#     print("Name must be atleast 3 characters")
# elif len(name) > 50:
#     print("Name can be maximum of 50 characters")
# else:
#     print("Name looks good")


# weight = input("weight ")
# converter = input("(L)bs or (K)g: ")
# Lbs = float(weight) * 2.20
# Kg = float(weight) * 0.45
# if converter == "L":
#     print(Lbs)
# else:
#     print(Kg)


# weight = input("weight ")
# converter = input("Lbs or Kg: ")
# Lbs = float(weight) * 2.20
# Kg = float(weight) * 0.45
# if converter == "Lbs":
#     print(Lbs)
# else:
#     print(Kg)

# ****while loop****

# i  = 1
# while i <= 10:
#     print(i)
#     i = i + 1
# print("Done")



# i = 0
# while i <=4:
#     a = input("> ")
#     i = i + 1
#     if a == "help":
#         print("""Start - To start the car
#         Stop - To stop the car
#         Quit - To exit""")
#     elif a == "start":
#         print("Car started....Ready to go!")
#     elif a == "stop":
#         print("Car stopped")
#     elif a == "quit":
#         print("Exit")
#     else:
#         print("error")



# a = "" 
# while a != "quit":
#         a = input("> ")
#         if a == "help":
#             print("""Start - To start the car
#         Stop - To stop the car
#         Quit - To exit""")
#         elif a == "start":
#             print("Car started....Ready to go!")
#         elif a == "stop":
#             print("Car stopped")
#         elif a == "quit":
#             print("Exit")
#         else:
#             print("error")


# ****for and nested for loop example.py****

# for item in "Python":
#     print(item)
# for and nested for loop example.py

# ls = [10,20,30]
# sum = 0
# for item in ls:
#     sum = sum + item
# print(f"Total = {sum}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x} , {y})")




# for x in range(4):
#     for y in range(3):
#         for z in range(2):
#             print(f"({x} , {y} , {z})")



# ls1 = [5,2,5,2,2]
# ls2 = ["x"]
# for a in ls1:
#     for b in ls2:
#         c = a * b
#         print(c)


# ****Lists****
# ****find the largest number in list****
# ls = [2,4,6,8,10]
# max = ls[0]
# for a in ls:
#     if a > max:
#       max = a
# print(a)


# ****2D lists or tow-dimensional lists****

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# print(matrix[0] [2])
# for rows in matrix:
#     for items in rows:
#          print(items)


# list = [2,3,5,2,8]
# print(list.count(8))
# # print(list.clear())
# print(list.index(5))
# list.reverse()
# print(list)

# **** removes duplicates in list****
# list = [3,9,6,3,1,9,1,2]
# list1 = []
# for num in list:
#     if num not in list1:
#         list1.append(num)
# print(list1)
      
# ****To find greater or lesser numbers in list****
# list = [2,4,3,9]
# list1 =[]
# for num in list:
#     if num < 6:
#         list1.append(num)
# print(list1)     

# ****To find even number****
# list = [2,4,6,5,1,9]
# list1 = []
# for nums in list:
#     if nums % 2 == 0:
#         list1.append(nums)
# print(list1)  

# ****To find odd number****
# list = [1,3,5,2,6]
# list1 = []
# for nums in list:
#     if nums % 2 != 0:
#         list1.append(nums)
# print(list1)   


# ls = [1,1,1,1,1,2,3]
# count = ls.count(1)
# print(count)
        

# ls = [1,2,3]
# x,y,z = ls
# print(x)

# ****Dictionaries****

# customers = {"name":"Akarsh",
#              "email": "akarsh@gmail.com",
#              "age": 30}
# print(customers["name"])
# print(customers.get("age"))
# print(customers.get("phone"))


# phone = input("Phone: ")

# words = {
#          "1" : "one",
#          "2" : "Two",
#          "3" : "Three",
#          "4" : "Four"   
#          }

# output = ""                                 
# for nums in phone:
#    output += words.get(nums) + " "
# print(output)


# input = input("details: ")

# data = {
#             "1" : "akarsh@gmail.com",
#             "2" : "30",
#             "3" : "Male"
# }
# output = ""
# for ques in input:
#     output += data.get(ques)
# print(output)

# **** functions ****
# def phone_number():
#     print(9500110969)
#     print(4704187357)


# print("What is your phone number")
# phone_number()
# print("Thank You")


# **** Parameters ****                                      
# def details(name):
#     print(f"Hi {name}")
#     print("Welcome aboard")
# details("Akarsh")

   


# def names(first_name,last_name ):
#     print(f"Hello {first_name} {last_name}")
# names("Akarsh", "Nalla")


# def addition(n1,n2):
#     sum = n1+n2
#     return sum
# total = addition(1,2)
# print(total)

# **** keyword Arguments ****
# def names(first_name,last_name):
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome")
# names("Akarsh",last_name="Nalla")

#  **** return function ****
# def addition(n1,n2):
#    return n1 + n2
# total = addition(2,4)
# print(total)
# #     or    
# print(addition(1,3))


# **** Exception ****
# try:
#     age = int(input("age: "))
#     print(age)
# except ValueError:
#     print("Invalid input")

# def addition(n1,n2):
#     sum = n1+n2
#     print(sum)
#     # return sum
# addition(1,2)


# **** Class ****

# class Point:
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
# point1 = Point()
# point1.draw()
# point1.x = 1
# point1.y = 2
# print(point1.x)

# point2 = Point()
# point2.move()
# point2.x = 3
# point2.y = 4
# print(point2.y)

# class Akarsh:
#     def add(self):
#         print("hello")

# name = Akarsh()
# name.add()


# **** Constructors ****
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")


# point = Point(10,20)
# point.draw()
# point.move()
# print(point.x)


# class Person:
#     def talk(self):
#         print("Telugu")
# name = Person()
# name.talk()
# name.a = "Akarsh"
# print(name.a)



# class Person:
#     def __init__(self, name, talk):
#         self.name = name
#         self.talk = talk

# details = Person("Akarsh", "Telugu")
# print(details.name)
# print(details.talk)


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi iam {self.name}")

akarsh = Person("Akarsh Reddy")
akarsh.talk()
    
   




   
   

   
    



    







   

