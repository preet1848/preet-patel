print("Welcome to the Data Analyser and Transformer Program\n")

while True:
    
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion) ")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")
    
    choice = int(input("Enter your choice :"))
    
    if choice == 1:
        array_input = input("Enter data for a 1D array (seperated by spaces) : ")
        arr = list(map(int , array_input.split()))
        print("Data has been stored successfully")
    
    elif choice == 2:
        print("Data Summary: ")    
        print("Total element :" , len(arr))
        print("Minimum value :" , min(arr))
        print("Maximum value :" , max(arr))
        print("Sum of all value :" , sum(arr))
        print("Average value : " , sum(arr) / len(arr))

    elif choice == 3:
        num = int(input("Enter a number to Calculate its factrial :"))
        def factorial(num):
            if num == 1:
                return 1
            else :
                return num * factorial(num-1)    
        print(f"factorial of {num} is : " , factorial(num))        

    elif choice == 4:
        num = int(input("\nEnter a threshold value to filter out Data below this value: "))
        filtered_data = list(filter(lambda x: x >= num, arr))
        print(f"\nFiltered Data (value >= {num}):")
        print(*filtered_data, sep=", ")
      
    
    elif choice == 5:
        choice = print("Choose sorting option")
        print("1. Ascending")
        print("2. Descending")
        
        choice = int(input("Enter your choice :"))
        
        if choice == 1:
            sorted_arr = sorted(arr)
            print("Sorted Data in Ascending Order :" , sorted_arr)
            
            
        elif choice == 2:
            sorted_arr = sorted(arr , reverse = True)
            print("Sorted Data in Descending Order :" , sorted_arr)
    
        else:
            print("invalid choice")    
            
            
    elif choice == 6:
        
        print("\nDataset Statisticals :\n")
        print("Minimum value:", min(arr))
        print("Maximum value:", max(arr))
        print("Sum of all value:", sum(arr))
        print("Average value : ", sum(arr) / len(arr))
    
    elif choice == 7:
        print("Thank you for using the data Analyser and transformer program. Goodbye") 
        break
    
    else:
        print("Invalid choice. Please try again")
