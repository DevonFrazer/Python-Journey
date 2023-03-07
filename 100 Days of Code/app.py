print("Welcome to the tip calculator! ")
bill = float(input("What is the amount for your bill? $"))
numb_of_people = int(input("How many people would you like to split the bill with? "))
tip_percentage = int(input("What percentage would you like to give? 10, 12, or 15? "))
bill_with_tip = tip_percentage / 100 * bill + bill
bill_per_person = bill_with_tip/numb_of_people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}.")
