Start=int(input("Enter odometer starting reading value in km:\n"))
End=int(input("Enter odometer ending reading value in km:\n"))
Mileage=int(input("Enter the average Mileage of your car in kmpl\n"))
Consumption=(End-Start)/Mileage
print("the litres of the petrol consumed=\n",Consumption)
Tank=int(input("Enter the capacity of your fuel tank in litres\n"))
print("the stops required to fill the tank is:\n", int(Tank/(560/Mileage)))
