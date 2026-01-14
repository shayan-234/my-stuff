import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pymysql

# ---------------- MySQL Connection ----------------
class DB:
    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="shayan",
            password="YourPassword123!",
            database="students"
        )
        self.cursor = self.db.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS student (
                id INT PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        """)
        self.db.commit()

    def add_student(self, s_id, name, age):
        self.cursor.execute("SELECT id FROM student WHERE id=%s", (s_id,))
        if self.cursor.fetchone():
            return False, "ID already exists"
        self.cursor.execute("INSERT INTO student (id, name, age) VALUES (%s, %s, %s)", (s_id, name, age))
        self.db.commit()
        return True, "Student added"

    def get_students(self, search=""):
        if search:
            self.cursor.execute("SELECT * FROM student WHERE name LIKE %s", ('%' + search + '%',))
        else:
            self.cursor.execute("SELECT * FROM student")
        return self.cursor.fetchall()

    def remove_student(self, s_id):
        self.cursor.execute("SELECT id FROM student WHERE id=%s", (s_id,))
        if not self.cursor.fetchone():
            return False, "ID not found"
        self.cursor.execute("DELETE FROM student WHERE id=%s", (s_id,))
        self.db.commit()
        return True, "Student removed"

    def update_student(self, s_id, name, age):
        self.cursor.execute("SELECT id FROM student WHERE id=%s", (s_id,))
        if not self.cursor.fetchone():
            return False, "ID not found"
        self.cursor.execute("UPDATE student SET name=%s, age=%s WHERE id=%s", (name, age, s_id))
        self.db.commit()
        return True, "Student updated"

# ---------------- GUI ----------------
class StudentApp:
    def __init__(self, root):
        self.db = DB()
        self.root = root
        self.root.title("🌟 Student Management System")
        self.root.geometry("750x500")
        self.root.configure(bg="#e6f2ff")

        # Top Frame: Title and Search
        top_frame = tk.Frame(root, bg="#e6f2ff")
        top_frame.pack(side="top", fill="x", pady=10)

        title = tk.Label(top_frame, text="Student Management System", font=("Helvetica", 22, "bold"),
                         bg="#e6f2ff", fg="#003366")
        title.pack(pady=5)

        search_frame = tk.Frame(top_frame, bg="#e6f2ff")
        search_frame.pack(pady=5)
        tk.Label(search_frame, text="Search by Name:", font=("Helvetica", 12), bg="#e6f2ff").pack(side=tk.LEFT, padx=5)
        self.search_entry = tk.Entry(search_frame, width=25, font=("Helvetica", 12))
        self.search_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Search", command=self.search_student, bg="#4CAF50", fg="white",
                  font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)
        tk.Button(search_frame, text="Show All", command=self.load_students, bg="#2196F3", fg="white",
                  font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)

        # Middle Frame: Treeview (expandable)
        tree_frame = tk.Frame(root, bg="#e6f2ff")
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.column("ID", width=80, anchor="center")
        self.tree.column("Name", width=400, anchor="center")
        self.tree.column("Age", width=80, anchor="center")
        self.tree.pack(fill="both", expand=True, side="left")

        # Scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", font=("Helvetica", 12), rowheight=25)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        # Bottom Frame: Buttons (fixed)
        btn_frame = tk.Frame(root, bg="#e6f2ff")
        btn_frame.pack(side="bottom", fill="x", pady=10)

        btn_specs = [
            ("➕ Add Student", self.add_student_ui, "#4CAF50"),
            ("✏️ Update Student", self.update_student_ui, "#FF9800"),
            ("🗑 Remove Student", self.remove_student_ui, "#F44336"),
            ("🔄 Refresh List", self.load_students, "#2196F3"),
        ]
        for i, (text, cmd, color) in enumerate(btn_specs):
            tk.Button(btn_frame, text=text, command=cmd, bg=color, fg="white",
                      font=("Helvetica", 12, "bold"), width=18).grid(row=0, column=i, padx=5)

        self.load_students()

    # ---------------- Methods ----------------
    def load_students(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in self.db.get_students():
            self.tree.insert("", tk.END, values=student)

    def search_student(self):
        search_text = self.search_entry.get()
        for row in self.tree.get_children():
            self.tree.delete(row)
        for student in self.db.get_students(search_text):
            self.tree.insert("", tk.END, values=student)

    def add_student_ui(self):
        s_id = simpledialog.askinteger("ID", "Enter Student ID")
        if s_id is None: return
        name = simpledialog.askstring("Name", "Enter Student Name")
        if not name: return
        age = simpledialog.askinteger("Age", "Enter Student Age")
        if age is None: return
        success, msg = self.db.add_student(s_id, name, age)
        messagebox.showinfo("Info", msg)
        self.load_students()

    def remove_student_ui(self):
        s_id = simpledialog.askinteger("Remove", "Enter Student ID to Remove")
        if s_id is None: return
        success, msg = self.db.remove_student(s_id)
        messagebox.showinfo("Info", msg)
        self.load_students()

    def update_student_ui(self):
        s_id = simpledialog.askinteger("Update", "Enter Student ID to Update")
        if s_id is None: return
        name = simpledialog.askstring("Name", "Enter New Name")
        if not name: return
        age = simpledialog.askinteger("Age", "Enter New Age")
        if age is None: return
        success, msg = self.db.update_student(s_id, name, age)
        messagebox.showinfo("Info", msg)
        self.load_students()


# ---------------- Run App ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
