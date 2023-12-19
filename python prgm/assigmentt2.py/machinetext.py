#1.
# num=int(input("enter the number:"))
# if num>1:
#     for i in range(2,int(num**.5)+1):
#         if num %i==0:
#             print(f"num is  not prime number:")
#             break
#         else:
#             (f" num is prime number:")

# 2.


# class BankAcc:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive value.")
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
#         elif amount <= 0:
#             print("Invalid withdrawal amount. Please enter a positive value.")
#         else:
#             print("Insufficient funds for withdrawal.")
#     def get_balance(self):
#         print(f"Account balance for {self.account_holder}: ${self.balance}")
#         return self.balance
# account_holder_name = "John Doe"
# initial_balance = 1000
# account = BankAcc(account_holder_name, initial_balance)

# account.get_balance()
# account.deposit(500)
# account.withdraw(200)
# account.get_balance()

# 3.
# from tkinter import *
# from PIL import Image,ImageTk
# root=Tk()
# root.configure(bg="#181c31")
# root.geometry("500x450")
# def click_me_for_courier():
#     print("click_me_for_courier")
# lab1=Label(root,text="Username",font=("Helvetica", "20"),fg='white',bg='#181c31')
# lab1.place(x=25,y=140)
# entry=Entry(root,bg='#181c31')
# entry.place(x=25,y=200)
# lab2=Label(root,text="Password",font=("Helvetica", "20"),fg='white',bg='#181c31')
# lab2.place(x=25,y=250)
# entry=Entry(root,bg='#181c31')
# entry.place(x=25,y=300)
# btn=Button(root,text="Sign In",command=click_me_for_courier,bg='#181c31',fg='white')
# btn.place(x=25,y=400)
# lab3=Label(root,text="FASHION STORE",font=("Times", "25", "bold italic"),fg='white',bg='#181c31')
# lab3.pack()
# image=Image.open("C:/Users/DELL/Pictures/CAFE-2.png")
# image1=ImageTk.PhotoImage(image)
# lab_img=Label(root,image=image1,width=700,height=550)
# lab_img.place(x=700,y=250)
# root.geometry('300x400')
# root.mainloop()


 