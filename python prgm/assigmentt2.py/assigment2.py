# 3.

# list=['maths','chemistry',1997,2000]
# list.append(20783)
# print(list)
# list.insert(2,345)
# print(list)
# list=[1,2,3,4,5]
# print(sum(list))
# print(len(list))3
# print(list.count(1))
# print(list.pop())
# print(list.index(2))

# 6.
# list=[2,3,4,5,6]
# print(sum(list))

# 8.
# str=input("input a string")
# d=l=0
# for i in str:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#             l=l+1
#     else:
#             pass
# print("letters",l)
# print("digit",d)

# 12.
# list1=[1,5,6,8,10]
# # print(min(list1))
# print(max(list1))

# 10.
# fruits=["apple","orange","banana","kiwi"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#      newlist.append(x)
# print(newlist)

# square=[]
# for i in range(20):
#    square.append(i*i)
# print(square)

# 13.

# remove=[1,2,3,4,6,8,9,10]
# remove=[x for x in remove if x%2!=0]
# print(remove)

# 14.

# def printvalues():
#     l=list()
#     for i in range(1,31):
#         l.append(i**2)
#     print(l)
# printvalues()

# 15.
 
# list=["banana","apple","orange"]
# list_1="fruit_"
# list_3=[list_1 + item for item in list]
# print(list_3)


# 1.
# x=[[3,4],
#    [2,1],
#    [5,6]]
# result=[[0,0,0],
#        [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#  print(r)


# 2.
# sentence= "I love PYTHON"
# capitalized_string=sentence.capitalize()
# print(capitalized_string)

# 16.
# x=[1,2,3,4]
# y=['a','b','c','d']
# for x,y in zip(x,y):
#     print(x,y)

# 11.
# dict={'apple':'fruit','pea':'vegetable'}
# dict1={dict[key]:key for key in dict}
# print(dict1)

# 5.
# dict={'id':123,'name':'xyx', 'place':'zxc'}
# print(dict)
# print(len(dict))
# dict.values()
# print(dict.values())
# dict.keys()
# print(dict.keys())
# dict.items()
# print(dict.items())
# dict.clear()
# print(dict.clear())
# print(str(dict))

# 4.
# dict={12,'xyz',34}
# dict1={'id','name','age'}
# dict.update(dict1)
# print(dict)

# 7.
# n=int(input("input the number"))
# d=dict()
# for x in range(1,n+1):
#     d[x]=x*x
# print(d)


# 17.
# dict={'id':23,'name':'xyz','age':25,'place':'cvb'}
# dict['company']="spectrum"
# print(dict)

# 18.
# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4={}
# for d in(dict1,dict2,dict3):
#     dict4.update(d)
# print(dict4)

# 19.
# d={'red':1,'blue':2,'green':3}
# for key,value in d.items():
#     print(key,value)

# 20.
# dict={1:2,2:5,9:8,}
# result=sum(dict.values())
# print(result)

# 21.
# pet={'dog':'willie','cat':'mikky','cow':'ammu'}
# for pet_name,pet_type in pet.items():
#     print(f"{pet_name} is a {pet_type}")


# 23.
# str=input()
# d={'digit':0,'letter':0}
# for i in str:
#     if i.isdigit():
#      d["digit"]+=1
#     elif i.isalpha():
#        d["letter"]+=1
#     else:
#        pass
# print("letters",d["letter"])
# print("digit",d["digit"])


# d=dict()
# n=9
# for x in range(1,n):
#     d[x]=x**2
# print(d)


# 9.
# data=[1,2,3,4,5]
# # r1=map(lambda x:x*2,data)
# # print(list(r1))
# # r2=filter(lambda x:x%2==0,data)
# # print(list(r2))
# from functools import reduce
# r3=reduce(lambda x,y:x*y,data)
# print(r3)

# # 22.
# def filter_mark(marks):
#      filter_mark={subject: mark for subject, mark in marks.items() if mark >50}
#      return filter_mark     
# marks={'math':60,'chemistry':46,'hindi':30,'physics':70,'english':40}
# filter_mark=filter_mark(marks)
# print(filter_mark)
