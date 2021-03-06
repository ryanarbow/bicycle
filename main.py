from bicycles import Bicycle, BikeShop, Customer, Wheel, Frame, BicycleManufacturer

if __name__ == '__main__':
    # create 3 different wheel types
    small = Wheel("small", 5, 40)
    medium = Wheel("medium", 10, 50)
    large = Wheel("large", 15, 60)
    wheels = [small, medium, large]

    # create 3 diffferent frames
    aluminum = Frame("aluminum", 5, 100)
    carbon = Frame("carbon", 15, 200)
    steel = Frame("steel", 25, 300)
    frames = [aluminum, carbon, steel]

    #create production
    road = Bicycle("road", small, carbon)#, 25, 500)
    mountain = Bicycle("mountain", large, carbon)#, 55, 150)
    hybrid = Bicycle("hybrid", medium, steel)#, 30, 250)
    firstprod = [road, mountain, hybrid]

    #cruiser = Bicycle("cruiser", large, steel)#, 60, 200)
    #bmx = Bicycle("bmx", small, aluminum)#, 55, 300)
    #tandem = Bicycle("tandem", large, aluminum)#, 75, 600)
    #secondprod= [cruiser, bmx, tandem]

    #create 2 suppliers
    bob = BicycleManufacturer("bob", firstprod, 10)
    bob.print_inventory()
    #Tom = BicycleManufacturer("Tom", supply2, 10)

    # create a bike shop
    mellow = BikeShop("mellow", 20, bob)
    mellow.print_inventory()
    # This is due to weird floating point differences. Better solution
    # is to use something like numpy's assert_allclose. For now this works.

    # create 3 customers
    han = Customer("Han", 300)
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
