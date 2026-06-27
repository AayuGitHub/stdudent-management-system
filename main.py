from StudentManager import StudentManager
# from Student import Student

manager = StudentManager()

manager.load_data()

while True:
    # Print menu options:
    print("=========================")
    print("Student Management")
    print("=========================")
    print("1. Add student") 
    print("2. View student") 
    print("3. Search student") 
    print("4. Update student") 
    print("5. Delete student") 
    print("6. Exit") 

    # Get user choice
    choice = input("enter your choice (1-6): ").strip()

    # Handle choice using conditional statements
    if choice == "1":
        print("\nPlease fill below details of student:\n")

        name = input("Enter the name of student: ").strip()
        while name == "":
            name = input("Name cannot be empty. Please enter a valid name: ").strip()
                
        while True:
            try:
                age = int(input("Enter the age of student: "))
                break
            except ValueError:
                print("Invalid Input! Age must be a whole number. Please try again.")
        course = input("Enter the course of student enrolled in: ")
        while course == "":
            course = input("\nPlease enter the valid course: ")

        success = manager.add_student(name, age, course)
        if success:
            print(f"\n{name} added successfully...")    
        else:
            print(f"\n{name} already exists in the students' list. Please add another student.")

    elif choice == "2":
        records = manager.view_students()
        if records is None:
            print("No student record found.")
        else:
            print(f"\nEach student and their details: \n")
            for student in records:
                student.display_info()

    elif choice == "3":
        name = input("\nEnter the name of student whom you want to search: ").strip()
        student = manager.search_student(name)

        if student:
            print(f"\n{name} exists in directory and here are their details: ")
            # student_instance = Student(student.name, student.age, student.course)
            # student_instance.display_info()
            student.display_info()
        else:
            print(f"\n{name} doesn't exist in students directory currently. Please use '1' to add them first!")

    elif choice == "4":
        name = input("\nEnter the name of student whom you want to update: ").strip()
        student = manager.search_student(name)
        if not student:
            print(f"\n{name} doesn't exist in student's directory!")
        else:
            print(f"\nYou can update age and course {name} is enrolled in: ")

            # Collect and validate updated age input right here in the menu layer
            updated_age = None
            while True:
                age_input = input(f"Add updated age of {name} (Leave blank to skip): ").strip()
                if age_input == "":
                    break
                try:
                    updated_age = int(age_input)
                    break
                except ValueError:
                    print("Invalid input! Age must be a whole number. Please try again!")
            
            course_input = input(f"Updated course of {name} (Leave blank to skip): ").strip()
            updated_course = course_input if course_input != "" else None
            
            manager.update_student(name, new_age=updated_age, new_course=updated_course)
            print(f"\n{name}'s details have been updated!")

    elif choice == "5":
        name = input(f"\nEnter the name of student whom you want to delete: ")
        print(f"\nDeleting {name} from student list...")    

        if manager.delete_student(name):
            print(f"\nSuccesfully removed {name} from the directory!!")
        else:
            print(f"{name} was not found in the directory!")

    elif choice == "6":
        print("\nSaving database records before shutdown...")
        manager.save_data() # Save everything right before exiting
        print("Exiting program. Goodbye! ")
        break

    else:
        # Handle invalid inputs
        print("Invalid choice! Please enter 1, 2, 3, 4, 5, or 6.")
    

