Starting_Value = float(input(" Take a note & enter the car odometer value before starting the trip: "))
Ending_Value = float(input(" Enter the car odometer value after ending the trip: "))
Distance_Travelled = Ending_Value - Starting_Value
Fuel_Consumed = float(input(" Enter the fuel consumed value in liters: "))
Mileage = Distance_Travelled / Fuel_Consumed
print( Mileage,'kms','/','Ltr')
