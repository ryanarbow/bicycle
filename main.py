from bicycles import Bicycle, BikeShop, Customer, Wheel, Frame, BicycleManufacturer

if __name__ == '__main__':
    # create 3 different wheel types
    small = Wheel("small", 5, 10)
    medium = Wheel("medium", 10, 15)
    large = Wheel("large", 15, 20)
    wheels = [small, medium, large]
    
    # create 3 diffferent frames
    aluminum = Frame("aluminum", 5, 10)
    carbon = Frame("carbon", 15, 20)
    steel = Frame("steel", 25, 30)
    frames = [aluminum, carbon, steel]
    
    # create a bike shop
    road = Bicycle("road", small, carbon)#, 25, 500)
    mountain = Bicycle("mountain", large, carbon)#, 55, 150)
    hybrid = Bicycle("hybrid", medium, steel)#, 30, 250)
    cruiser = Bicycle("cruiser", large, steel)#, 60, 200)
    bmx = Bicycle("bmx", small, aluminum)#, 55, 300)
    tandem = Bicycle("tandem", large, aluminum)#, 75, 600)
    inventory = [road, mountain, hybrid, cruiser, bmx, tandem]
    mellow = BikeShop("mellow", inventory, 20)
    mellow.print_inventory()
    
    # create 3 customers
    han = Customer("Han", 200)
    luke = Customer("Luke", 500)
    leia = Customer("Leia", 1000)
    customers = [han, luke, leia]
    
    print('<== bikes affordable for each customer ==>')
    for customer in customers:
        customer.print_affordable_bikes(mellow)
        
    print('<== each customer purchases a bike ==>')
    han.purchase_bike(mountain, mellow)
    luke.purchase_bike(hybrid, mellow)
    leia.purchase_bike(road, mellow)
    mellow.print_inventory()
    
