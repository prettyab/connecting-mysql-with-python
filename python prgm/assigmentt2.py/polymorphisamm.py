# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("drivr!")
# class Boat:
#     def __init__(self,band,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("sail!")
# class Plane:
#     def __init__(self,band,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("fly!")
# car1=Car("ford","mustang")
# boat1=Boat("ibiza","touring 20")
# plane1=Plane("indigo","456")
# for x in (car1,boat1,plane1):
#     x.move()
  
# CLASS POLIMORPHISAM
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("move!")
# class Car(Vehicle):,/ 
#     pass
# class Boat(Vehicle):
#     def move(self):
#         print("sail!")
# class Plane(Vehicle):
#     def move(self):
#         print("fly!")
# car1=Car("ford","mustang")
# boat1=Boat("ibiza","touring 20")
# plane1=Plane("indigo","456")
# for i in (car1,boat1,plane1):
#     print(i.brand)
#     print(i.model)
#     i.move()

# METHOD OVERLOADING
# class amazon:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def info(self):
#         print(f"this is product and am class is invoked .the name {self.name}.this cost{self.price} rupees.")
# class flipkart:
#     def __init__(self,name,price):
#          self.name=name
#          self.price=price
#     def info(self):
#         print(f"this is product and fli class is invoked.the name is{self.name}.this cost{self.price} rupees.")
# FLP=flipkart("iphone",2.5)
# AMZ=amazon("iphone",4)
# for p1 in (FLP,AMZ):
#     p1.info()



