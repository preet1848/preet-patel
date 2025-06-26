print("welcome to the student data organizer")
students = []
subjects_offered = set()

while True:
    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        print("\nEnter student details:")
        student_id = input("Student ID: ")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ").split(",")

        std_dob = (student_id, dob) 
        student = {
            "id_dob": std_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        subjects_offered.update(subjects)
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records.")
        else:
            print("\n--- Student Records ---")
            for i in students:
                std_id, dob = i["id_dob"]
                print(f"ID: {std_id} | Name: {i['name']} | Age: {i['age']} | Grade: {i['grade']} | Subjects: {', '.join(i['subjects'])}")

    elif choice == "3":
        std_id = input("Enter Student ID to update: ")
        found = False
        for i in students:
            if i["id_dob"][0] == std_id:
                i["age"] = int(input("Enter new age: "))
                new_subjects = input("New subjects (comma-separated): ").split(",")
                i["subjects"] = [sub for sub in new_subjects]
                subjects_offered.update(i["subjects"])
                print("Student updated.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        std_id = input("Enter Student ID to delete: ")
        for i in range(len(students)):
            if students[i]["id_dob"][0] == std_id:
                del students[i]
                print("Student deleted.")
                break
        else:
            print("Student not found.")

    elif choice == "5":
        print("\n--- Subjects Offered ---")
        
        print(subjects)

    elif choice == "6":
        print("Thank you for using Student Data Organizer!")
        break

    else:
        print("Invalid choice. Try again.")
