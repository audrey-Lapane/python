#Fuel cost calculator

km = float(input("How many kilometers do you want to drive: "))
fuel_price = float(input("What is the current petrol price per litre: "))

liters_needed = km / 10

total_cost = liters_needed * fuel_price

print(f"For a {km}km drive and the petrol price is R{fuel_price} per liter, the total cost of petrol will be R{round(total_cost,2)}")