from OOP_Exercise_Chapter6 import  vehicle

# option
def display_option():
    print("Welcome to Vehicle Data Store System (VDSS)")
    print("1.Add Vehicle")
    print("2.Delete Veheicle")
    print("3.Edit Vehicle price")
    print("4.Edit Vehicle color")
    print("5.Display all Veheicle")
    print("6.exit")
    select = int(input("select(1-6) ? : "))
    if select == 1:
        input_vehicle_data()
    elif select== 2:
        delete_vehicle()
    elif select == 3:
        edit_vehicle_price()
    elif select == 4:
        edit_vehicle_color()
    elif select == 5:
        display_vehicle()
    elif select == 6:
        print("Good Bye.")
        exit(0)

        print("Please,select number 1-6.")

    # add data
def input_vehicle_data():
        brand = input("Enter vehicle brand: ")
        model = input("Enter vehicle model: ")
        color = input("Enter vehicle color: ")
        maxspeed = int(input("Enter vehicle max speed: "))
        price = float(input("Enter vehicle price: "))

        vehicle.my_vehicle.append(vehicle(brand,model,color,maxspeed,price))
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# display data
def display_vehicle():
    if len(vehicle.my_vehicle) ==0:
        print("You had no vehicle data.")
    else:
        print(f'You had {len(vehicle.my_vehicle)} following:')
        n = 1 #count
        for x in  vehicle.my_vehicle:
            print(f'[{n}]:',end="")
            x.vehicle_detail()
            n = n+1
            print("\n")

#delete vehicle
def delete_vehicle():
    #display all data in list
    display_vehicle()
    if len(vehicle.my_vehicle) == 0:
        print("You had no data to dalete.")
        s = int(input("Select to delete ?: "))

        vehicle.delete_vehicle(vehicle, s-1)
        vehicle.delete_vehicle(s-1)
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

# edit vehicle price
def edit_vehicle_price():
    display_vehicle()
    if len(vehicle.my_vehicle) != 0:
        s = int(input("Select to edit ?: "))
        #display previous price
        print(f'previous price: {vehicle.my_vehicle[s-1].price}')
        new_price = input("new price: ")
        vehicle.edit_vehicle_price(vehicle,s-1,new_price)
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

def edit_vehicle_color():
    display_vehicle()
    if len(vehicle.my_vehicle) != 0:
        s = int(input("Select to edit ?: "))
        # display previous color
        print(f'previous color: {vehicle.my_vehicle[s - 1].color}')
        new_color = input("new color: ")
        vehicle.edit_vehicle_color(vehicle, s - 1, new_color)
        print("\n------------------------------------")
        print("Already ass vehicle to sto")
        print("------------------------------------\n")

       # run
#my_vehicle = []
s = 0
while s == 0:
    display_option()

