Start=int(input("Enter the starting odometer reading in km:\n"))
End=int(input("Enter the ending odometer reading in km:\n"))
Litres=int(input("How many litres of petrol you have used\n"))
mileage=(End-Start)/Litres
print("The mileage of the car is ",mileage,"kmpl")
