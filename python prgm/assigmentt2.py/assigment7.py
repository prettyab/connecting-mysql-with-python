# 1.

# class Vehicle():
#     def __init__(self,model,year):
#         self.model=model
#         self.year=year
#     def display(self):
#         print(f"{self.model},{self.year}")
# class Car(Vehicle):
#     def __init__(self,model,wheel):
#         self.model=model
#         self.wheel=wheel
#     def display(self):
#         print(f"{self.model},{self.wheel}")    
# class Motorcycle(Vehicle):
#     def __init__(self,wheel,brand):
#         self.brand=brand
#         self.wheel=wheel
#     def display(self):
#         print(f"{self.brand},{self.wheel}")
# car1=Car("toyato",4)
# print(car1.model,car1.wheel)
# motocycle1=Motorcycle("tvs",2)
# print(motocycle1.brand,motocycle1.wheel)


# 2.
# class Animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def __init__(self,name,color):
#         super().__init__(name,species="Dog")
#         self.color=color
#     def make_sound(self):
#         return "boww! boww!"    
# class Cat(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name,species="Cat")
#         self.breed=breed
#     def make_sound(self):
#         return "meoww! meoww!"
    
# def animal_sound(animal):
#     print(f"{animal.name} the {animal.species} says:{animal.make_sound()}")
# dog1=Dog("nikky","white")
# cat1=Cat("millie","persian")
# animal_sound(dog1)
# animal_sound(cat1)

# 3.
# def cal_sum_and_product(numbers):
#     t_sum=0
#     t_product=1
#     for num in numbers:
#         t_sum+=num
#         t_product*=num
#     return t_sum,t_product
# def x():
#     input_numbers=int("enter a list of numbers separated by spaces:")
#     numbers=[float(i) for i in input_numbers.split()]
# sum_result,product_result=cal_sum_and_product(numbers)
# print(f"Sum:{sum_result}")
# print(f"product:{product_result}")

# 
# def main():
#     num_tuple=(1,2,3,4,5)
#     index_to_print=int(input("enter the index of the items to print:"))
#     items_to_print=num_tuple[index_to_print]
#     print(f"the item at index {index_to_print} is : (item_to_print)")
    

# 6.
# def main():
#     color_list=["Red","Green","White","Black"]
#     if color_list:
#         first_color=color_list[0]
#         last_color=color_list[-1]
#         print(f"first color :{first_color}")
#         print(f"last color: {last_color}")
#     else:
#         print("the color list is empty")
# main()

# 7.

# import datetime
# now=datetime.datetime.now()
# print(now)

# 8.
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def calculate_circle_area(self):
#         return math.pi*self.radius**2
#     def calculate_circle_perimeter(self):
#         return 2*math.pi*self.radius
# radius=float(input("enter the radius of the circle:"))
# Circle=Circle(radius)
# area=Circle.calculate_circle_area()
# perimeter=Circle.calculate_circle_perimeter()
# print(f"the area of the circle is :",area)
# print(f"the perimeter of the circle is :",perimeter)

# 9.

# def add_numbers(a,b):
#     if isinstance(a,int) and isinstance(b,int):
#         result=a+b
#         return result
#     else:
#         return "both objects should be integers"
#     return a+b
# print(add_numbers(10,20))
# print(add_numbers(10,20.45))
# print(add_numbers('5',20))
# print(add_numbers('5','6'))

# 10.
# class Bank:
#     def __init__(self):
#         self.accounts = {}
#     def create_account(self, account_number, initial_balance=0):
#         if account_number not in self.accounts:
#             self.accounts[account_number] = initial_balance
#             print(f"Account {account_number} created successfully.")
#         else:
#             print(f"Account {account_number} already exists. Please choose a different account number.")

#     def check_balance(self, account_number):
#         if account_number in self.accounts:
#             balance = self.accounts[account_number]
#             print(f"Balance for account {account_number}: {balance}")
#         else:
#             print(f"Account {account_number} does not exist.")

#     def deposit(self, account_number, amount):
#         if account_number in self.accounts:
#             self.accounts[account_number] += amount
#             print(f"Deposited {amount} into account {account_number}.")
#             self.check_balance(account_number)
#         else:
#             print(f"Account {account_number} does not exist.")

#     def withdraw(self, account_number, amount):
#         if account_number in self.accounts:
#             if amount <= self.accounts[account_number]:
#                 self.accounts[account_number] -= amount
#                 print(f"Withdrew {amount} from account {account_number}.")
#                 self.check_balance(account_number)
#             else:
#                 print(f"Insufficient funds in account {account_number}.")
#         else:
#             print(f"Account {account_number} does not exist.")
# def main():
#     bank = Bank()
#     bank.create_account("12345", 1000)
#     bank.create_account("67890")
#     bank.deposit("12345", 500)
#     bank.withdraw("67890")
#     bank.check_balance("12345")
#     bank.check_balance("67890")
#     bank.check_balance("00000")  
#     main()

# 6/12/23
# 1.
# data=[1,2,3]
# squared=map(lambda x:x**2,data)
# print(list(squared))

# 2.
# data=[1,2,3,4,5,7,8,6]
# data1=list(filter(lambda n:n%2==0,data))
# print("list of even numbers:",data1)

# 3.
# num=int(input("enter the value:"))
# print("even numbers from 1 to",num,"are:")
# for i in range(1,num+1):
#          if (i%2==0):
#                  print(i,end=" ")

# 4.
# rows=int(input("enter the total number of row:"))
# print("right angled triangle star pattern")
# for i in range(1,rows+1) :
#         for j in range(1,i+1):
#                 print('*',end=' ')
#         print()

# 5.
# f1=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/demofile.txt","w")
# f1.write("Hello ,World!")
# f1.close()

# 6.
# f2=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/world.txt","r")
# print(f2.read())
# f2=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/hai.txt","w")
# f2.write("hai iam pretty .now im in kochi.")
# f2=open("c:/Users/DELL/Desktop/python prgm/assigmentt2.py/hai.txt","a")
# f2.writelines("traine at spectrum\n")
# f2.close()
