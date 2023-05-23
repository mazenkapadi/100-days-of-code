#Tip Calculator
print("Calculates your tip!")
bill = float(input("What was the bill? $"))
tip = int(input("How much do you want to tip? 12, 15, 18, 20?"))
people = int(input("How many are going to split the bill?"))

tipPercent = tip / 100
totalTip = bill * tipPercent
totalBill = bill +totalTip
billPerson = totalBill / people

finalAmount = round(billPerson, 2)

print(f"Each person should pay: ${finalAmount}")