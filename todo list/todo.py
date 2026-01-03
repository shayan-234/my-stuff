import json 
class todo_list:
    def __init__(self):
        try:
            with open("todo list.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []
    def save_tasks(self):
        with open("todo list.json", "w") as f:
            json.dump(self.tasks, f)
    def add_a_task(self):
        try:
            task = input("enter the task you want to add:")
            vale = int(input("enter the number of this task:"))
            confirm = input("enter y to confirm the addition and n for cancellation:").lower()
            if confirm == 'y':
                for i in self.tasks:
                    if i["num"] == vale:
                        print("Task number already exists ❌")
                        return
                self.tasks.append({'task' : task, 'num' : vale, 'status' : False})
                print("added sucsesfullly")
            elif confirm == 'n':
                print("addtion cancelled")
            else:
                print("WRONG INPUT!!!")
            self.save_tasks()
        except ValueError:
            print("pls enter a valid input")
    def veiw_task(self):
        if len(self.tasks) == 0 :
            print("no tasks")
        else:
            for  i in self.tasks:
                if i['status'] == False :
                    print(f"{i['num']}. {i['task']}")
                    return
            print("every task is completed add a new task")
    def remove_task(self):
        try:
            remove = int(input("enter the num of the task:"))
            for i in self.tasks:
                if i["num"] == remove :
                    self.tasks.remove(i)
                    print("task removed")
                    self.save_tasks()
                    return
            print("no such task")
        except ValueError:
            print("WRONG INPUT!!")
    def comleted_a_task(self):
        try:
            comp = int(input("enter the num of the task which is done:"))
            for i in self.tasks:
                if i["num"] == comp:
                    i["status"] = True
                    self.tasks.remove(i)
                    print("task marked as completed")
                    self.save_tasks()
                    return
            print("no such task ❌")
        except ValueError:
            print("WRONG INPUT!!")
    def menu(self):
        while True :
            menu = int(input('1. add task\n'
                    "2. view task\n"
                    "3.remove task\n"
                    "4. completed a task\n"
                    "5. exit\n"))
            if menu == 1 :
                self.add_a_task()
            elif menu == 2 :
                self.veiw_task()
            elif menu == 3 :
                self.remove_task()
            elif menu == 4 :
                self.comleted_a_task()
            else :
                break
manager = todo_list()
manager.menu()

