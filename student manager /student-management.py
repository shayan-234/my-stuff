import pymysql
class Students:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="shayan",          
            password="YourPassword123!",  
            database="students"
        )
        self.cursor = self.db.cursor()

    def add_student(self):
        s_id = int(input("Enter the new id of the student: "))
        age = int(input("Enter the age of the student: "))
        name = input("Enter the name of the student: ")
        confirm = input("Enter y to confirm else n: ").lower()

        self.cursor.execute("SELECT id FROM student WHERE id=%s", (s_id,))
        if self.cursor.fetchone():
            print("ID already exists")
            return

        if confirm == "y":
            sql = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (s_id, name, age))
            self.db.commit()
            print("Added successfully")
        else:
            print("Addition cancelled")

    def view_student(self):
        self.cursor.execute("SELECT * FROM student")
        students = self.cursor.fetchall()

        if not students:
            print("No students")
        else:
            for student in students:
                print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]}")

    def remove_students(self):
        remove_id = int(input("Enter the ID of the student to remove: "))

        self.cursor.execute("SELECT id FROM student WHERE id=%s", (remove_id,))
        if not self.cursor.fetchone():
            print("Student ID not found")
            return

        self.cursor.execute("DELETE FROM student WHERE id=%s", (remove_id,))
        self.db.commit()
        print("Removed successfully")

    def menu(self):
        while True:
            try:
                menu = int(input(
                    "1. Add student\n"
                    "2. View students\n"
                    "3. Remove student\n"
                    "4. Exit\n"
                ))

                if menu == 1:
                    self.add_student()
                elif menu == 2:
                    self.view_student()
                elif menu == 3:
                    self.remove_students()
                elif menu == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice")

            except ValueError:
                print("Please enter a number")

manager = Students()
manager.menu()
