#Create classes to represent Bicycles, Bike shops, and Customer
class bicycle(object):
    def __init__(self, model_name, weight, prodcost):
        self.model_name = model_name
        self.weight = weight
        self.prodcost = prodcost

class bike_shop(object):
    def __init__(self, name, inventory, margin, profit):
        self.bike_shop = bike_shop
        self.name = name
        self.inventory = inventory
        self. margin = margin
        self.profit = profit

class customers(object):
    def __init__(self, name, budget, own):
        self.name = name
        self.budget = budget
        self.own = own

#bike models
road = bicycle("road", 25, 500)
mountain = bicycle("mountain", 55, 50)
hybrid = bicycle("hybrid", 30, 250)
cruiser = bicycle("cruiser", 60, 200)
bmx = bicycle("bmx", 55, 500)
tandem = bicycle("tandem", 75, 600)



stock = {
    road:5,
    mountain:6,
    hybrid:7,
    cruiser:8,
    tandem:4,
}

#Create a bicycle shop that has 6 different bicycle models in stock. 
#The shop should charge its customers 20% over the cost of the bikes. 
mellow = bike_shop("Mellow Johnnys", stock, .2, 0)

#Create three customers. One customer has a budget of $200, the second 
#$500, and the third $1000.


han = customers("Han", 200, 0)
luke = customers("Luke", 500, 0)
leia = customers("Leia", 1000, 0)
names = [han.name, luke.name, leia.name]

for name in names:
    if 
    print (name)

#if __name__ == '__main__':
