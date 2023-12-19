# 3.
# year = 2000
# if (year%400 == 0):
#     print("leap year")
# else:
#     print(" not a leap year")

# 1.
# var = (int(input("enter a num:")))
# if var >0:
#     print("positive")
# else:
#     print("negative")


# 2.
# var1 = input("enter the first varible")
# var2 = input("enter the second varible")
# temp = var1
# var1 = var2
# var2 = temp
# print("the value of the first varible after swapping is:", var1)
# print("the value of the second varible after swapping is:",var2)


# 4.
# num = int(input("enter the num:"))
# if (num%2==0):
#     print("{0} is an even num.")
# else:
#     print("{0} is an odd num.")
    


# 5.
# def Fib(n):
#    if n <= 1:
#        return n
#    else:
#        return (Fib(n - 1) + Fib(n - 2))  # function calling itself(recursion)


# n = int(input("Enter the Value of n: "))  # take input from the user
# print("Fibonacci series :")
# for i in range(n):
#    print(Fib(i),end = " ")


# 7.
# lower = int(input("enter lower limit (>1):"))
# upper = int(input("enter upper limit :"))
# for i in range(lower, upper+1):
#     if i >1:
#         for num in range(2,i):
#             if i%num==0:
#              break
#         else:
#             print(i)

# 8.
# print("/show 1 to 50 sum of odd number\n")
# sum=0
# for i in range (1,51):
#     rem=i%2
#     if rem!=0:
#         sum=sum+i
#         print("\n first 1 to 50 sum of odd number is ",sum)
# 

# 9.
# num = int(input("enter the number"))
# factorial=1
# if num<0:
#     print(" factorial does not exit for negative number")
# elif num ==0:
#      print("fatorial of 0 is 1")
# else:
#           for i in range(1,num+1):
#            factorial = factorial*i
#            print("The factorial of",num,"is",factorial)

# 10.
# st=input("enter the string:")
# if st==st[::-1]:
#     print("palindrome")
# else:
#     print(" not palindrome")
    
# 11.
# sum=0
# for n in range(101,200):
#     if n%7==0:
#         sum+=n
#         print("sum divisible by 7:",sum)

# # 12.
# num =20
# for i in range (1,19):
#     print(num,'x',i,'=',num*i)


# 13.
# l=int(input("length :"))

# w=int(input("writh :"))
# area=l*w
# perimeter=2*(l+w)
# print("area of rectangle:",area)
# print("perimeter of rectangle:",perimeter)

# 14.
# number,sum=6,0
# for i in range(number+1):
#     sum+=i
#     print(sum)

# 16.
# num1 = 15
# num2 = 18
# num3 = 17
# if (num1 >= num2) and (num1 >= num3):
#     largest = num1
# elif (num2>=num1) and (num2 >= num3):
#     largest = num2
# else:
#     largest = num3
# print(" the largest number is",largest)


# 19.
# string = input('enter the string :')
# count =0
# string=string.lower()
# for i in string:
#     if i == 'a' or i=='e'or i=='i' or i=='o' or i== 'u':
#         count+=1
#         if count ==0:
#             print('no vowels found')
#         else:
#             print('total vowels are:' + str(count))


# 20.
# print("addition of two complex number:" , (4+3j)+(3-7j))
# print("substraction of two complex number:" , (4+3j)-(3-7j))
# print("multiplication of two complex number:" , (4+3j)*(3-7j))
# print("division of two complex number :", (4+3j)/(3-7j))

# 21.

# num_1= 10
# num_2 = 11
# # num_3 = num_1%num_2
# # print(num_3)
# # num_4=num_1 - num_2
# # print(num_4)
# num_5=num_1 * num_2
# print(num_5)


# 6.
# rows=6
# for i in range(rows,0,-1):
#     for j in range (0,i-1):
#          print("*",end='')
#     print("\r")



# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end='')
#     print("")
# print('')
# for i in range(rows+1,0,-1):
#         for j in range(0,i-1):
#             print("*",end='')
#         print('')


# rows=5
# for i in range(0,rows):
#     for j in range(0,i+1):
#         print("*",end='')
#     print('')
# for i in range(rows,0,-1):
#     for j in range(0,i-1):
#         print("*",end='')
#     print('')


# size=7
# m=(2*size)-2
# for i in range(0,size):
#     for j in range (0,m):
#         print("*",end="")
#     m=m-1
#     for j in range (0,i+1):
#         print("*",end='')
#     print("")


# 18.
# rows=5
# for num in range(rows):
#     for row in range(num):
#         print(num,end="")
#     print("")


# rows=5
# b=0
# for i in range (rows,0,-1):
#     b+=1
#     for j in range(1,i+1):
#         print(b,end='')
#     print('')



# rows=5
# for row in range(1,rows+1):
#     for column in range(1,row+1):
#         print(column,end="")
#     print('')


# 22.

# num_1=7
# num_2=6
# # num_3=num_1<num_2
# print(num_3)
# num_4=num_1>num_2
# print(num_4)
# num_5=num_1<=num_2
# print(num_5)
# num_6=num_1>=num_2
# print(num_6)

# 23.
# num_1=3
# num_2=4
# # num_3=(num_1<num_2) and (num_1!=num_2)
# # print(num_3)
# # num_4=(num_2>+num_1) and (num_1>num_2)
# # print(num_4)
# num_5=not(num_1==num_2)
# print(num_5)

# 24.
# i=1
# while(i<6):
#     i=i+1
#     print(i)

# 25.
# customer_num=5
# invoice_num =1212
# print("Invoice No(s):")
# while(customer_num>0):
#  print("INV -", invoice_num)
#  invoice_num = invoice_num +3
#  customer_num = customer_num -1


# 26.

# string=input()
# if len("string")<5:
#       print('string')
# elif string [-5:]=='ing':
#  print(string+'php')
# else :
#     print(string + 'java')

# # 28.
# def is_seed(first, second):
#     digits = [int(digit) for digit in str(first)]
#     product = first * (sum(digits))
#     return product == second
# num1 = 145
# num2 = 2900
# result = is_seed(num1, num2)
# print(result)  

