print("-----------------------------------------------")
print("|  Welcome To Days, Weeks, Years Left Till 90 |")
print("-----------------------------------------------")

age = int(input("Enter your age: "))

life_duration = 90

days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12

years_left = life_duration - age
days_left = years_left * days_in_a_year
weeks_left = years_left * weeks_in_a_year
months_left = years_left * months_in_a_year

print(f"You have {days_left} Days, {weeks_left} Weeks, {months_left} Months & {years_left} Years left till you're 90 Years old.")
