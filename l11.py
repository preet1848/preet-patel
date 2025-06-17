user = [
    {"id":1 , "name":"alice" , "age":25},
    {"id":2 , "name":"melisha" , "age":27}

]

while True:
    print("CRUD Operator in python!!")
    print("1. create user")
    print("2. read user")
    print("3. update user")
    print("4. delete user")
    print("5. exit ")


    choice = input("Enter your choice(1-5) : ")

    if choice == "1":

        try:
            user_id = int(input("Enter id : "))
            name = input ("Emter name :")
            age = int(input("Enter age :"))
            user.append({"id":user_id , "name":name , "age":age})

            print ("user successfully added!!")


        except:
            print("Ivalid input!!")


    elif choice == "2":
        if not user:
            print("No user found.")

        else:
            print("User list:")
            for user in user:
                print(user)

    elif choice == "3":

        try:

            user_id = int(input("Enter update user id : "))

            found = False 

            for user in user:

                if user["id"] == user_id:
                 
                    field = input("Enter your field to update (name/age):").lower()
                 
                    if field in user:
                     
                        if field == "age":
                         
                            user["age"] = int(input("Enter new age :"))

                        else:
                            user["name"] = input("Enter new name: ")

                            print ("User update successfully!!")

                else:

                    print("Invalid field")

                found = True

                break
        
            if not found:

                print("user not found!!") 

        except:

            print("invalid input!!!") 

    elif choice == "4":          

        try:

            user_id = int(input("Enter ID to Delete User : "))

            for user in user:

                new_user = []

                if user["id"] != user_id:

                    new_user.append(user)

                    users = new_user

                    print("user delete successfully!!")

        except:

            print("invalid input!!!")    

    elif choice == "5":

        print("Program exit successfully!!")    


    else:

        print("Invalid choice, please Enter number of 1 to 5.")        



    


        
        

    





                
                     

