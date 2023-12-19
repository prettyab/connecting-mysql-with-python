# # 1.
# class MyString():
#     def __init__(self):
#         self.str1=""
#     def get_string(self):
#         self.str1=input("enter the string:")
#     def print_string(self):
#         print(self.str1.upper())
# str1=MyString()
# str1.get_string()
# str1.print_string()

# 2.

# class Car:
#     def __init__(self,wheels,doors):
#         self.wheels=wheels
#         self.doors=doors
# car1=Car(4,4)
# print(car1.wheels)
# print(car1.doors)
# car2=Car(2,2)
# print(car2.wheels)
# print(car2.doors)

# 3.
# class Circle():
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.radius**2*3.14
#     def perimeter(self):
#         return 2*self.radius*3.14
# Newcircle = Circle(8)
# print(Newcircle.area())
# print(Newcircle.perimeter())

# 4.
# class Bankaccount:
# 	def __init__(self):
# 		self.balance=0
# 		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

# 	def deposit(self):
# 		amount=float(input("Enter amount to be Deposited: "))
# 		self.balance += amount
# 		print(" Amount Deposited:",amount)

# 	def withdraw(self):
# 		amount = float(input("Enter amount to be Withdrawn: "))
# 		if self.balance>=amount:
# 			self.balance-=amount
# 			print(" You Withdrew:", amount)
# 		else:
# 			print(" Insufficient balance ")
# 	def display(self):
# 		print(" Net Available Balance=",self.balance)
# s = Bankaccount()
# s.deposit()
# s.withdraw()
# s.display()

# 5.
# class Shape:
#     def area(self):
#         return 0
# class Square(Shape):
#     def __init__(self, length=0):
#         self.length = length
#     def area(self):
#         return Shape.area(self)
# shape = Shape()
# print("Area of generic shape:", shape.area())
# square = Square(5)
# print("Area of square:", square.area())
# default_square = Square()
# print("Area of default square:", default_square.area())
