print("Welcome to the Interactive Personal Data Collector!")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_Number = int(input("Please enter your favourite number: "))

print("Thank you! Here is the information we collected: ")


print(f"Name: {name} (Type : {type(name)} , Memory Address : {id(name)})")
print(f"age: {age} (Type : {type(age)} , Memory Address : {id(age)})")
print(f"height: {height} (Type : {type(height)} , Memory Address : {id(height)})")
print(f"favourite number: {favourite_Number} , (Type : {type(favourite_Number)} , Memory Address : {id(favourite_Number)})")

birth_year = 2025 - age
print(f"your birth_year is appoximately:\n{birth_year} (based on your age of {age}")

print("Thank you for using the Data collector. goodbye!")
