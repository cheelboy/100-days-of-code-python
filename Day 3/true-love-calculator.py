name_1 = input("Enter your name: ")
name_2 = input("Enter their name: ")

combined_names = name_1 + name_2

lower_case_names = combined_names.lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')

true = t + r + u + e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')

love = l + o + v + e

love_score = str(true) + str(love)
love_score = int(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is: {love_score}%. You go like coke & mentos!")
elif (love_score > 40) and (love_score < 50):
    print(f"Your love score is: {love_score}%. You both are alright together.")
else:
    print(f"Your love score is: {love_score}%")


