class Vehicle:
    my_vehcle = []
    def __init__(self,brand,model,color,maxspeed,price):
        self.brand = brand
        self.model = model
        self.color = color
        self.maxspeed = maxspeed
        self.price = price

        def Vehcle_info(self):
         print(f'Brand:{self.brand} Model:{self.model} Color:{self.color} Maxspeed:{self.maxspeed} Price:{self.price}')


# s1 = Vehicle
# s1.brand = ""
# s1.model = ""
# s1.color = ""
# s1.maxspeed = ""
# s1.price = "0"
#
# Vc = []
#
# n = int(input('How many Vehicle?:'))
# for i in range(n) :
#     s = Vehicle()
#     print((f"Please, enter Vehicle info {i+1}:"))
#     s.brand = input("Enter brand:")
#     s.model = input("Enter model:")
#     s.color = input("Enter color:")
#     s.maxspeed = input("Enter maxspeed:")
#     s.price = input("Enter price:")
#     Vc.append(s)
#
# # for i in Vc:
#     i.Vehicle_info()