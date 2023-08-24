import random

# Enter the names of the people on the table
people_on_table = input("Type the names of everyone separated by comma(,) [Example: John, Jane, Jack, Joan]: ")

# Converting the String to List by comma separation
people_list = people_on_table.split(", ")

# Randomizing the list index
random_person = random.randint(0, len(people_list) - 1)

# Assigning the random index to the person who will pay
paying_person = people_list[random_person]

# Printing the result
print(f"$$ {paying_person} is going to pay the bill today! $$")
