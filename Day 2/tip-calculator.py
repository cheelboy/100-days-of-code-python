print("-----------------------------------------------")
print("|           Welcome To Tip Calculator         |")
print("-----------------------------------------------")

bill = input("How much is the total bill? $")
persons = input("How many people to split the bill? ")
tip = input("How much tip would you like to pay? 10%, 15%, 20% ? ")

bill_per_person = int(bill) / int(persons)

tip_per_person = bill_per_person + (bill_per_person * int(tip)/100)

print('The tip per person is: ' + "$" + str(tip_per_person))
