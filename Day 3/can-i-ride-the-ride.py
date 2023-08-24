height = int(input("Enter your height in centimeters (cm): "))

bill = 0

if height > 120:
    age = int(input("You're tall enough to ride! How old are you? "))
    if age < 12:
        bill = 5
        print(f"The ticket for {age} years old is $5.")
    elif age <= 18:
        bill = 7
        print(f"The ticket for {age} years old is $7.")
    else:
        bill = 12
        print(f"The ticket for {age} years old is $12.")

    want_photos = input("Do you want photos for $3? Y or N: ")

    if want_photos == 'Y' or 'y':
        bill += 3

    print(f"Your total bill is: ${bill}")

else:
    print(f"Sorry! You're not tall enough to ride.")
