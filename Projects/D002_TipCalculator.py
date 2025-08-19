# tipCalculator.py
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip_amount = int(input("What amount you would like to tip? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))  
total_bill = bill + tip_amount
amount_per_person = total_bill / people
print(f"Each person should pay: ${amount_per_person:.2f}")

