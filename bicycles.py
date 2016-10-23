class Wheel(object):
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

class Frame(object):
    def __init__(self, material, weight, cost):
        self.material = material
        self.weight = weight
        self.cost = cost

class Bicycle(object):
    def __init__(self, name, wheel, frame):
        self.name = name
        self.weight =  int(wheel.weight*2) + int(frame.weight)
        self.cost = (wheel.cost*2) + (frame.cost)
        self.wholesale_cost = 0
        self.retail_cost = 0

    def __repr__(self):
        return ('{}:{}').format(self.name, self.wholesale_cost)
        
class BicycleManufacturer(object):
    def __init__(self, name, supply, margin):
        self.name = name
        self.supply = supply
        self.margin = 1 + margin / 100
        self.wholesale_cost(self.supply)
    
    def wholesale_cost(self, supply):
        for bike in supply:
            bike.wholesale_cost = self.margin * bike.cost
    
    def print_inventory(self):
        print('<== {} inventory ==>'.format(self.name))
        for bike in self.supply:
            print('{}'.format(bike))
        
class BikeShop(object):
    def __init__(self, name, margin, manufacturer):
        self.name = name
        self.inventory = manufacturer.supply
        self.margin = 1 + margin / 100
        self.retail_cost = 0
        self.profit = 0
    
    def retail_cost(self):
        for bike in self.inventory:
            bike.retail_cost = self.margin * bike.wholesale_cost
    
    def print_inventory(self):
        print('<== {} shop inventory ==>'.format(self.name))
        for bike in self.inventory:
            print('{}'.format(bike))
            
    def find_affordable_bikes(self, customer):
        bikes_within_budget = []
        available_fund = customer.fund
        for bike in self.inventory:
            if bike.retail_cost <= available_fund:
                bikes_within_budget.append(bike)
                available_fund -= bike.retail_cost
        return bikes_within_budget
        
    def sell_bike(self, bike):
        self.profit = bike.retail_cost - bike.wholesale_cost
        self.inventory.remove(bike)
    
           
class Customer(object):
    def __init__(self, name, fund):
        self.name = name
        self.fund = fund
    
    def print_affordable_bikes(self, bike_shop):
        affordable_bikes = bike_shop.find_affordable_bikes(self)
        print('Customer: {0} can afford {1}'.format(self.name, 
                                            affordable_bikes))  
                                            
    def purchase_bike(self, bike, bike_shop):
        affordable_bikes = bike_shop.find_affordable_bikes(self)
        if bike in affordable_bikes:
            bike_shop.sell_bike(bike)
            self.fund -= bike.retail_cost
            print('{} purchased {} bike for {} with balance fund now {}'.format(
                self.name, bike.name, bike.retail_cost, self.fund))