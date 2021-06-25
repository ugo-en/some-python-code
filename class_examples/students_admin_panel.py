# STUDENTS ADMIN PANEL

# create list of students
students_list = ["John","Angel","Arnold","Phil"]


def show_students():
    # use for loop to display students
    for student in students_list:
        print("-->",student)


def add_student():
    new_student = input("Enter the name of the new student: ")
    students_list.append(new_student)

    # show students again to reflect changes
    print(new_student,"has been added!")
    show_students()


def remove_student():
    # remove a student
    student = input("Which student do you want to remove: ")

    if student in students_list:
        students_list.remove(student)
    else:
        print(student,"is not in the list!")


menu = '''
Pick an option from this menu:
1. Show all students
2. Add a new student
3. Remove a student 
'''

print("WELCOME TO THE STUDENT'S ADMIN PANEL")

while True:
    print(menu)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        show_students()
    elif choice == 2:
        add_student()
    elif choice == 3:
        remove_student()
    else:
        print("Invalid option!")

    should_continue = input("Do you want to continue? (Y/N) ")
    if should_continue == "Y":
        continue
    else:
        break
