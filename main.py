print("Welcome to The Tip Calculator v1.0 by @P0ulp1")
bill = input("What was the total bill ? ")
tip = input("What percentage would you like to give ? Recommended : 10, 15 or 20 ")
people = input("How many people to split the bill ? ")
result = (int(bill) / int(people)) * (int(tip) / 100 + 1)
result = "%.2f" % result
print(f"The total amount per person to pay will be {result} dollars.")
