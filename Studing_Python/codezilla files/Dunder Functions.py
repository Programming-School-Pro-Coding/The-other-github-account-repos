#print("------------------")
#print (1 + 1)
#print("--------------------")
#print("Codezilla " + " Channel ")
#print("-----------------------------")
#print(3 ** 3)
#print("-------------------------------")
#print("Codezilla " * 3)
#print("----------------------")

#------------------------------------------------------------

# len(), []

a = "Mohamed Ehab"
b = ["Codezilla", "channel"]

#print(len(a))
#print(b[0])

#print(a.__len__())
#print(b.__getitem__(0))

#print(dir(a))

#--------------------------------------------
#overloading len()

class Order:
    def __init__(self, cart, customer, kind):
        self.cart = cart
        self.customer = customer
        self.kind = kind
    
    def __len__(self):
        return len(self.cart)

    def __call__(self):
        print(f"{self.customer}")
    
    def __str__(self):
        return f"{self.customer} bought {self.cart}"
    
    def __repr__(self):
        return f"Order(list of items, customer name)"
    
    def __bool__(self):
        return len(self.cart) > 0
    
    def __iadd__(self, other):
        self.cart.append(other)
        return self
    
    def __imul__(self, mult):
        self.cart.append(mult)
        return self
    
    def __isub__(self, subs):
        self.cart.append(subs)
        return self
    
    def __getitem__(self, key):
        return self.cart[key]
    
    def __setitem__(self, key, value):
        self.cart[key] = value
        return self
    
    
    

    #def add_item(self, other):
    #    return self.cart.append(other)
    
#    def get_cart_len(self):
#        return len(self.cart)
    
#    def get_customer_name(self):
#        return len(self.customer)
    
#    def kind_of_carts(self):
#        return self.kind
    


order = Order(["laptop", "Television", "mouse", "keyboard"], ["Mohamed Ehab", "Anas Ehab"], ["Apple", "TCL"])
#print(order.get_cart_len())
#print(order.get_customer_name())
#print(order.kind_of_carts())
#print(len(order))
#order()
#print(order)
#print(repr(order))
#print(bool(order))
#order.add_item("monitor")
#order += "Mohamed"
#print(order.cart)
#order *= "2"
#print(order.cart)
#order -= "2"
#print(order.cart)
order
print(order[3])
order[3] = "visual studio code"
print(order[3])