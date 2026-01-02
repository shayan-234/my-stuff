import json
class Students:
    def __init__(self):
        try:
            with open("students.json", "r") as f:
                self.students = json.load(f)
        except FileNotFoundError:
            self.students = []
    def save_to_file(self):
        with open("students.json", "w") as f:
            json.dump(self.students, f)
    def add_student(self):
        s_id = int(input("enter the new id of the student:"))
        age = int(input("enter the age of the students:"))
        name = input("enter the name of the student:")
        confirm = input("enter y to confirm else enter n:")
        for student in self.students:
            if student["id"] == s_id:
                print("ID already exists ❌")
                return
        confirm = confirm.lower()
        if confirm == "y":
            self.students.append({'id' : s_id,
                            'name' : name,
                            'age' : age})
            print("added sucsesfully")
        else:
            print("addition cancelled")
        self.save_to_file()
    def view_student(self):
        if len(self.students) == 0 :
            print("No students")
        else :
            for student in self.students:
                print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']}")
    def remove_students(self):
        remove_id = int(input("Enter the ID of the student to remove: "))
        for student in self.students:
            if student["id"] == remove_id:
                self.students.remove(student)
                print("Removed successfully ✅")
                self.save_to_file()
                return
        print("Student not found ❌")
    def menu(self):
        while True :
            menu = int(input('1. add student\n'
                    "2. view student\n"
                    "3.remove student\n"
                    "4. exit\n"))
            if menu == 1 :
                self.add_student()
            elif menu == 2 :
                self.view_student()
            elif menu == 3 :
                self.remove_students()
            else :
                break
manager = Students()
manager.menu()
