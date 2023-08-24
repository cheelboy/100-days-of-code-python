height = float(input("Enter your height in Meter (m): "))
weight = float(input("Enter your weight in Kilograms (kg): "))

weight_status = ["Underweight", "Healthy Weight", "Overweight", "Obesity"]

bmi = round(weight/height ** 2)

if bmi < 18.5:
    print(f"You BMI result is: {weight_status[0]}")
elif 18.5 <= bmi < 24.9:
    print(f"You BMI result is: {weight_status[1]}")
elif 25.0 <= bmi < 29.9:
    print(f"You BMI result is: {weight_status[2]}")
else:
    print(f"You BMI result is: {weight_status[3]}")