# 1.
# f1=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/files.txt","r") 
# print(f1.read())
# f2=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/filewrite.txt","w")
# f2.write("hello\nmy name is pretty\nfrom kasargod,")
# f2.close()

# 2.
# f=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/f.txt","r")
# print(f.read())
# print(f.readline())

# 4.
# import csv
# with open("C:/Users/DELL/Downloads/size(1).csv","r") as file:
#     reader=csv.reader(file)
#     for row in reader:
#         print(row)
# with open ("C:/Users/DELL/Downloads/weekday.csv","w") as file:
#     writer=csv.writer(file)
#     writer.writerow(["Name","Abbreviation","Numeric",])

# # 5.
# import json
# f={
#    "firstName": "Joe",
#    "lastName": "Jackson",
#    "gender": "male",
#    "age": 28,
#    "address": {
#        "streetAddress": "101",
#        "city": "San Diego",
#        "state": "CA"
#    },
#    "phoneNumbers": [
#        { "type": "home", "number": "7349282382" }
#    ]
# }
# with open ("C:/Users/DELL/Downloads/sample2.json","w")as file:
#     json.dump(f,file)
# 6.
# f1=open("C:/Users/DELL/Desktop/python prgm/assigmentt2.py/f.txt","a")
# f1.writelines("\n me , love , pizza\n")
# f1.close()