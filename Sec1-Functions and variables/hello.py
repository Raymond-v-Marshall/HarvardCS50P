#Ask user for their name

name = input("What is your name? ")
name = name.strip().title()
#split users name into first and last name
first, last = name.split(" ")
#greats user
print(f"Hello, {first} {last}!")