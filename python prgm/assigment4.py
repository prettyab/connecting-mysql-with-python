# 1.
# def check_even_odd(n):
#     if n%2==0:
#         print("even number")
#     else:
#         print("odd")
# x=int(input("enter the integer num:"))
# check_even_odd(x)

#  2.
# def create_square_dict():
#     square_dict={}
#     for n in range(1,21):
#         square_dict[n]=n**2
#     print(square_dict)
# create_square_dict()

# 3.
# def remove_vowels(string):
#     vowels=['a','e','i','o','u','A','E','I','O','U']
#     result=" "
#     for char in string:
#         if char not in vowels:
#             result+=char
#     return result
# input_string="haii , beauty!"
# output_string=remove_vowels(input_string)
# print(output_string)

# # 4.
# terms=10
# r1=list(map(lambda x:2**x,range(terms)))
# print("the total terms are:",terms)
# for i in range(terms):
#     print("2 raised to power",i,"is",r1[i])

# # 5.
# # def bubble_sort(arr):
# #     n=len(arr)
# #     for i in range(n):
# #         for j in range(n-i-1):
# #             if arr[j]>arr[j+1]:
# #                 arr[j],arr[j+1]=arr[j+1],arr[j]
# # my_array=[2,16,-2,35,-1,10]
# # print("or array:",my_array)
# # bubble_sort(my_array)
# # print("sorted array:",my_array)

# # 6.

    
# def binary_Search(array, x, low, high):
#     if high >= low:
#         mid = low + (high - low)//2
#         if array[mid] == x:
#             return mid
#         elif array[mid] > x:
#             return binary_Search(array, x, low, mid-1)
#         else:
#             return binary_Search(array, x, mid + 1, high)
#     else:
#         return -1
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binary_Search(array, x, 0, len(array)-1)
# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")

# 7.
# def test(keys,values):
#     return dict(zip(keys,values))
# l1=['a','b','c','d']
# l2=[1,2,3,4,]
# print("orginal lists:")
# print(l1)
# print(l2)
# print("combaine the two lists in dict:")
# print(test(l1,l2))

# 8.
# def recr_fibo(n):
#     if n<=1:
#         return n
#     else:
#         return(recr_fibo(n-1)+ recr_fibo(n-2))
# nterms=10
# if nterms<=0:
#         print("enter positive integer")
# else:
#     print("fibonacci sequence:")
#     for i in range(nterms):
#         print(recr_fibo(i))

# 9.
# def recr_facto(n):
#     if n==1:
#         return n
#     else:
#         return n*recr_facto(n-1)
# num=7
# if num<0:
#     print("factorial is does not exit for negative number:")
# elif num==0:
#         print("factorial 0 is 1")
# else:
#         print("the factorial",num,"is",recr_facto(num))

# 11.
# def generator_num(n):
#     for num in range(n+1):
#         if num%5==0 and num%7==0:
#             yield num
# n=int(input("enter the value for n:"))
# result=generator_num(n)
# print(f"Numbers divisible by 5 and 7 between 0 and {n}: {', '.join(map(str, result))}")

# # 12.
# def generote_even_num(n):
#     for num in range(n+1):
#         if num%2==0:
#             yield num
# n=int(input("enter value for n:"))
# result=generote_even_num(n)
# print(f"print the even numbers between 0 and {n}:{','.join(map(str,result))}")

# 13.
# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j >=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#             return arr
# array=[1,5,12,12,2]
# print("orginal array:%s"% array)
# print("sorted array:%s" % insertion_sort(array))
      

# 14.
# def linearsearch(array,n,x):
#     for i in range(0,n,x):
#         if (array[i]==x):
#             return i
#     return -1
# array=[2,4,0,1,9]
# x=1
# n=len(array)
# result=linearsearch(array,n,x)
# if(result==-1):
#         print("element not found")
# else:
#         print("element found at index:",result)

# 15.
# def selection(a,s):
#     for i in range(s):
#         min_index=i
#         for j in range(i+1,s):
#             if a[j]<a[min_index]:
#                 min_index=j
#                 (a[i],a[min_index])=(a[min_index],a[i])
# array=[-2,45,0,11,-9]
# s=len(array)
# selection(array,s)
# print("sorted a in ascending order:")
# print(array)

# 16.
# list= [] 
# n = int(input("Enter the number of elements: "))
# for i in range(1, n+1): 
#     elem = int(input("Enter the elements: ")) 
#     list.append(element) 
# list.sort() 
# print("The sorted list: ", list) 
# print("The second smallest value of this list: ",list[1])

