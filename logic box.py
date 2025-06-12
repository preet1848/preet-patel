print("Welcome to the pattern generator and number Analyzer\n")

print("1. Right-angled triangle")
print("2. pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of numbers ")
choice = int(input("Enter your choice: "))


if choice == 1:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print("*" * i)

elif choice == 2:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

elif choice == 4 :

  start = int(input("enter the start of range:"))
  end = int(input("enter the end of range:"))
  total=0
  for num in range(start , end +1):
      if num %2 == 0:
          print(f"number {num} is Even ")
          
      else: 
          print(f"number {num} is odd")
      total += num    
  print(f"sum of all numbers from {start}  to {end} is {total}")

else:
    print("invalid choice\n \n ")        

 
print("1. Right-angled triangle")
print("2. pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of numbers ")
choice = int(input("Enter your choice: "))


if choice == 1:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print("*" * i)

elif choice == 2:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

elif choice == 4 :

  start = int(input("enter the start of range:"))
  end = int(input("enter the end of range:"))
  total=0
  for num in range(start , end +1):
      if num %2 == 0:
          print(f"number {num} is Even ")
          
      else: 
          print(f"number {num} is odd")
      total += num    
  print(f"sum of all numbers from {start}  to {end} is {total}")

else:
    print("invalid choice\n \n ")        


print("1. Right-angled triangle")
print("2. pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of numbers ")
choice = int(input("Enter your choice: "))


if choice == 1:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print("*" * i)

elif choice == 2:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

elif choice == 4 :

  start = int(input("enter the start of range:"))
  end = int(input("enter the end of range:"))
  total=0
  for num in range(start , end +1):
      if num %2 == 0:
          print(f"number {num} is Even ")
          
      else: 
          print(f"number {num} is odd")
      total += num    
  print(f"sum of all numbers from {start}  to {end} is {total}")

else:
    print("invalid choice\n \n ")        


print("1. Right-angled triangle")
print("2. pyramid")
print("3. left-angled triangle")
print("4. Analyze a range of numbers ")
choice = int(input("Enter your choice: "))


if choice == 1:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print("*" * i)

elif choice == 2:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * (2*i  -1))

elif choice == 3:
    row = int(input("Enter the number of rows for the pattern "))
    print("pattern: ")
    for i in range(1, row + 1):
        print(" " * (row - i) + "*" * i)

elif choice == 4 :

  start = int(input("enter the start of range:"))
  end = int(input("enter the end of range:"))
  total=0
  for num in range(start , end +1):
      if num %2 == 0:
          print(f"number {num} is Even ")
          
      else: 
          print(f"number {num} is odd")
      total += num    
  print(f"sum of all numbers from {start}  to {end} is {total}")


else:
    print("invalid choice\n \n ")        

print("Thank you for generating pattern and number")
