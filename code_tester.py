for num in range (1,101):
    days_chars = "Day " + str(num) + ": "
    dash = ""
    for days_char in range(0, len(days_chars) - 1):
        dash += "-"
    print(days_chars)
    print(dash)
    print("\n\n")
