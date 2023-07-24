height = float(input("Enter your height (meters): "))
weight = float(input("Enter your weight (kilograms): "))

bmi = weight / (height ** 2)

print("Your BMI (body mass index) is: " + str(bmi))
