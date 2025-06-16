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


