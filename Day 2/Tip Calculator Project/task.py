from functools import total_ordering

print("Welcome to the tip calculator")
bill= float(input("How much was the bill?"))
tip= float(input("Hom much tip would you like to give? 10,12 or 15%"))
people= int(input("How many people sharing the bill?"))
tip_in_percent = tip / 100
total_tip = bill * tip_in_percent
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Every person should pay: ${final_amount}")