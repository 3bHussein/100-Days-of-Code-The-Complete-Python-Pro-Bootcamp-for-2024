print("welcome to the tip calculator")

total_bill = float(input("what was the total bills ? \n"))
people = int(input("how many people to split the bill? \n"))
tip = int(input("what percentage tip would you like to give ? 10 ,12 or 15 ?\n "))


if tip == 10:
    tip = total_bill * tip / 100
elif tip == 12:
    tip = total_bill * tip / 100
elif tip == 15:
    tip = total_bill * tip / 100
else:
    tip=0

bill_plus_tip = float(tip) + total_bill
bill_per_person = bill_plus_tip / people
# bill_per_person = round(bill_plus_tip / people,2)

print("Each person should pay: $" + str(round(bill_per_person,2 )))
# print(f"Each person should pay: $ { str(bill_per_person)}" )

