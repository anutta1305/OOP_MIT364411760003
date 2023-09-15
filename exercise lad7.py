class ThaiEvCar:
    #class attribute
    my_ThaiEvCar = []

def input_ev_car_data():
    id = input("Enter ev_car id: ")
    brand = input("Enter ev_car brand: ")
    model = input("Enter ev_car model: ")
    acc_rate = int(input("Enter ev_car acc_rate: "))
    hp = int(input("Enter ev_car hp: "))
    range = int(input("Enter ev_car randge: "))
    price = float(input("Enter vehicle price: "))

    ThaiEvCar.myThaiEvCar.append(ThaiEvCar(id,brand,model,acc_rate,hp,range,price))
    print("\n------------------------------------")
    print("Already ass vehicle to sto")
    print("------------------------------------\n")

def display_ThaiEvCar():
    if len(ThaiEvCar.my_ThaiEvcar) ==0:
        print("You had no ThaiEvCar data.")
    else:
        print(f'You had {len(ThaiEvCar.my_ThaiEvCar)} following:')
        n = 1 #count
        for x in ThaiEvCar.my_ThaiEvCar:
            print(f'[{n}]:',end="")
            x.ThaiEvCar_detail()
            n = n+1
            print("\n")
