class notebook:
    def __init__(self):
        self.CPU = ""
        self.GPU = ""
        self.RAM = ""
        self.DISPLAY = ""
        self.STORAGE = ""
        self.OS = ""

        # display object attribute
    def notbook_info(self):
        print(f'CPU:{self.CPU} GPU:{self.GPU} RAM:{self.RAM} DISPLAY:{self.DISPLAY} STORAGE:{self.STORAGE} OS:{self.OS}')


s1 = notebook #empty object
# assign data to object attribute
s1.CPU = ""
s1.GPU = ""
s1.RAM = ""
s1.DISPLAY = ""
s1.STORAGE = ""
s1.OS = ""

nd = []

n = int(input('How many Notebook?:'))
for i in range(n) :
    s = notebook
    print((f"Please, enter Notebook info {i+1}:"))
    s.CPU = input("Enter CPU:")
    s.GPU = input("Enter GPU:")
    s.RAM = input("Enter RAM:")
    s.DISPLAY = input("Enter DISPLAY:")
    s.STORAGE = input("Enter STORAGE:")
    s.OS = input("Enter OS:")
    nd.append(s)

# display all notebook in input
for i in nd:
    i.notbook_info()

