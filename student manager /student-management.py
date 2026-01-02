students = []
def add_student():
    s_id = int(input("enter the new id of the student:"))
    age = int(input("enter the age of the students:"))
    name = input("enter the name of the student:")
    confirm = input("enter y to confirm else enter n:")
    for student in students:
        if student["id"] == s_id:
            print("ID already exists ❌")
            return
    confirm = confirm.lower()
    if confirm == "y":
        students.append({'id' : s_id,
                         'name' : name,
                         'age' : age})
        print("added sucsesfully")
    else:
        print("addition cancelled")
def view_student():
    if len(students) == 0 :
        print("No students")
    else :
        print (students)
def remove_students():
    remove_id = int(input("Enter the ID of the student to remove: "))
    for student in students:
        if student["id"] == remove_id:
            students.remove(student)
            print("Removed successfully ✅")
            return
    print("Student not found ❌")

while True :
    menu = int(input('1. add student\n'
              "2. view student\n"
              "3.remove student\n"
              "4. exit\n"))
    if menu == 1 :
        add_student()
    elif menu == 2 :
        view_student()
    elif menu == 3 :
        remove_students()
    else :
        break
