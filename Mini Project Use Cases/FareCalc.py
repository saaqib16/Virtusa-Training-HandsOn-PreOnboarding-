
"""
Core Python: The "FareCalc" Travel Optimizer
Business Case: A ride-sharing startup, "CityCab," needs a backend script to calculate fares. The fare isn't flat; it changes based on the time of day (Peak Hours) and the type of vehicle requested.
Problem Statement
Write a script that calculates the final "Ride Estimate" based on distance, vehicle type, and a "Surge Pricing" multiplier.
Student Tasks:
1. Dictionary Mapping: Store rates in a dictionary: {'Economy': 10, 'Premium': 18, 'SUV': 25} (rates per km).
2. Surge Logic: Ask the user for the "Hour of Day" (0-23). If the hour is between 17 and 20 (5 PM - 8 PM), apply a 1.5x Surge Multiplier to the total.
3. Function Definition: Create a function calculate_fare(km, type, hour) that returns the final price.
4. Error Handling: If the user enters a vehicle type not in your dictionary, use a try-except block or an if-in check to provide a "Service Not Available" message.
Deliverable: A .py script that takes user input and prints a formatted "Price Receipt."

"""

def FairCalculator(distance, vehicle_type, hour):
    rates={"Economy": 10, "Premium": 18, "SUV": 25}
    if vehicle_type not in rates:
        return "Service Not Available"
    
    base_fare = rates[vehicle_type] * distance
    if 17 <= hour <= 20:
        base_fare *= 1.5
    return base_fare

print("Welcome to CityCab Fare Calculator!")
try:
    distance=float(input("Enter the distance of your ride in kms: "))
    vehicle_type=input("Enter the type of vehicle (Economy, Premium, SUV): ")
    hour=int(input("Enter the hour of the day (0-23): "))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
else:
    result = FairCalculator(distance, vehicle_type, hour)
    if result == "Service Not Available":
        print("Selected Service Not Available, Please choose from Economy, Premium, or SUV.")
    else:
        print(f"Your estimated fare is: ₹{result:.2f}")

print("Thank you for using CityCab Fare Calculator!")