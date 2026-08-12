students = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30,  "student_id": 11230, "grades": {"Pythonprogrammering 1": 1, "Databasteknik": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32,  "student_id": 11231, "grades": {"Pythonprogrammering 1": 1, "Pythonprogrammering 2": 3}},
    {"name": "Daniel Eliasson", "age": 29,  "email": "daniel.eliasson@yh.nackademin.se", "student_id": 11233, "grades": {"Pythonprogrammering 1": 1, "Affärsmannaskap": 2}},
    {"name": "Magdalena Andersson", "age": 50,  "email": "magdalena.andersson@yh.nackademin.se", "student_id": 11234, "grades": {"Pythonprogrammering 1": 1, "Webbramverk inom python": 5}},
]

# Display list of students logic
def list_all_students():
    if not students:
        print("No students in the registery.")
        return
    
    for student in students:
        print(f"student ID: {student["student_id"]} - {student["name"]}, age: {student["age"]} - {student["email"]} ")


# Add student logic
def add_student():
    id = input("Enter the stundents ID")
    if not id:
        print("You must enter a student id")
        return
    if not id.isdigit():                # Error handlig: If the input is not a number
        print("Student ID must be numeric only")
        return
    
    first_name = input("Enter the students name: ").lower().strip()      # The input is only in lowercase and spaces are removed
    if not first_name:
        print("You must enter a name")
        return
    if not first_name.replace(" ", "").isalpha():      # No special carraters are allowed only alphabetical caracters.
        print("Names can only contain letters and spaces")
        return
    
    last_name = input("Enter the students last name: ").lower().strip()
    if not last_name:
        print("You must enter a name")
        return
    if not last_name.replace(" ", "").isalpha():
        print("Names can only contain letters and spaces")
        return
    
    age = input("Enter the students age")
    if not age:
        print("You must enter the students age")
        return
    if not age.isdigit():
        print("An age can only be numeric")
        return

    email = f"{first_name}.{last_name}@yh.nackademin.se"         # Automatic email creation
    print("This is the students email:", email)

    students.append({                   # Add the input into the list.
        "student_id": int(id),
        "name": first_name + " " + last_name,
        "age": age, "email": email})
    
    print(f"\nStudents {first_name + " " + last_name} added successfully")

# remove a student logic
def remove_student():
    if not students:
        print("There are no students to remove")
        return
   
    for student in students:
        print(f"ID: {student["student_id"]} - {student["name"]}")

    
    try:    
        choice =  int(input("Choose student to remove based on their id."))    # input is default a string and needs to be an int
    except:
        print("Chose a ID number")
        return
        
    for i in range(len(students)):       # Range is used since we need the position (index) to use .pop(i)
        if students[i]["student_id"] == choice:      # if the ID given by input is found in any of the indexes remove it.
                removed = students.pop(i)
                print(f"{removed["name"]} has been removed from the list")
                return
        





print("Welcome to my student handeling menue")

while True:
    print("\nRead the following and input ypu choice")
    print("\n[1]: List all students from the registry ")
    print("[2]: Add a student to the registry")
    print("[3]: Remove a student from the registry")
    print("[4]: Exit the program ")    

    
    try:
        choice = input("\nEnter you choice:")

        if choice == "1":
            list_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            print("Hope you liked my program, give me G plzz")
            break
    except:
        print("Enter a valid number please")