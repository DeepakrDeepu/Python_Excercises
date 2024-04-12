# To calculate no of stops taken to refuel the vehicle.

def get_mileage():
    return float(input("Enter the car Mileage: "))
    
def get_capacity():
    return float(input("Enter the tank capacity of the car: "))
    
Car_Mileage = get_mileage()
Tank_Capacity = get_capacity()

Distance_Travelled = 560
#Car_Mileage = float(input("Enter the car Mileage: "))
#Tank_Capacity = float(input("Enter the tank capacity of the car: "))
Total_Fuel_Needed = Distance_Travelled / Car_Mileage
Number_Stops = Total_Fuel_Needed / Tank_Capacity
Number_Stops = int(Number_Stops) + 1
print ("Number of stops taken during the travell from bangalore to goa: ", Number_Stops)
