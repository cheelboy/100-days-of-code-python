row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]

my_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? (Example: '23' i.e. 2nd row of 3rd column):  ")

horizontal = int(position[0])
vertical = int(position[1])

# selected_row = my_map[vertical - 1]
# selected_row[horizontal - 1] = "❌"

my_map[vertical - 1][horizontal - 1] = "❌"

print(f"{row1}\n{row2}\n{row3}")

