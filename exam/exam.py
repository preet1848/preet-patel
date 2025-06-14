while True:
      
    print("Welcome to the bill spliter app \n")
    bill = float(input("Enter the total bill amount: "))
    people = int(input("Enter number of people:"))
    tip = int(input("0/5/10/15/20 :"))

    if bill <0 or people <=0:
        print("invalid , try again")
        continue

    tip = (tip / 100) * bill
    final_bill = bill + tip 
    per_person = final_bill / people


    print(f"\nTip amount: ₹{tip:.2f}")
    print(f"total bill (with tip): ₹{final_bill:.2f}")
    print(f"Each pearson should pay: ₹{final_bill / people}")

    print("would you like to calculate another bill (y/n): y")
    print(".....\n")   
