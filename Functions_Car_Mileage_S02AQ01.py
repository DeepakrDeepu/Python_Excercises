# Mileage calculation using starting and ending value of the car using functions.

def get_fuel():
    return float(input("Enter the fuel consumed value in liters: "))
    
     
def get_number(value):
    return float(input(f"Enter the {value} of the odometer: "))
    
    
starting_value = get_number("starting value")
ending_value = get_number("ending value")
Fuel_Consumed = get_fuel()

Distance_Travelled = ending_value - starting_value
Car_Mileage = Distance_Travelled / Fuel_Consumed

print( Car_Mileage,'kms','/','Ltr')
