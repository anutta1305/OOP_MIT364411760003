class Customer:
    def __init__(self,id,name):
        self.id = id
        self.name = name

    def customre_info(self):
        print(f'Cus ID: {self.id}  Cus Na,e: {self.name}')

class Cart:
    def __init__(self,Customer):
        self.cart_customer = Customer # object parameter
        self.list_product = list()

    def cart_info(self):
        # display owenr of cart
        print(f'Owner Cart ID: {self.cart_customer.id}) '
              f'Owner name : {self.cart_customer.name}')
        # display products in cart
        print('List of products: ')
        for x in self.list_product:
            x.product_info()

        # display total pricd
        total = 0
        t = [total + x.price for x in self.list_product]
        print(f'Total price : {t}')
        for x in self.list_product:
            total += x.price
        print(f'Total price: {total}')



    def add_product(self,Product):
        self.list_product.append(Product)

class Product:
    def __init__(self,id,product_name,price):
        self.id = id
        self.product_name = product_name
        self.price = price

    def product_info(self):
        print(f'Pro ID: {self.id} Pro name: {self.product_name} '
              f'price: {self.price}')


# create object
# customer
c = Customer("C001","Tukta")
c.customre_info()

# product
p1 = Product("P001","Americano",50.0)
p2 = Product("P002","Ice Tea",35.5)
p3 = Product("P003","Ice Chocolate",40.0)



# cart
cart1 = Cart(c)
# add product to cart
cart1.add_product(p1)
cart1.add_product(p2)
cart1.add_product(p3)
