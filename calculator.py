# simple calculator using ladder statement

operator = input("Enter an Operator(+,-,*,/):")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

# perform for calculation

if operator == '+':
    result = num1 + num2
    print(f"sum of {num1}+{num2} = {result}")
elif operator =='*':
    result = num1 * num2
    print(f"sum of {num1} * {num2} = {result}")
elif operator =='-':
    result = num1 - num2
    print(f"sum of {num1} - {num2} = {result}")
elif operator =='/':
    result = num1 / num2
    print(f"sum of {num1} / {num2} = {result}")
    
else:
    print("The operator is not found")

      
  




             
            
