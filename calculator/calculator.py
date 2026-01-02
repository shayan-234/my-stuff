import json
class Calculator:
    def __init__(self):
        try:
            with open("calculator.json", "r") as f:
                self.history = json.load(f)
        except FileNotFoundError:
            self.history = []
    def save_to_file(self):
        with open("calculator.json", "w") as f:
            json.dump(self.history, f)
    def calculate(self):
        num2  = int(input("enter the first num:"))
        num1  = int(input("enter the second num:"))
        operator = input("enter the operator:")
        if operator == '+':
            result = num1 + num2
            print(result)
        elif operator == '-':
            result = num1 - num2
            print(result)
        elif operator == '*':
            result = num1 * num2
            print(result)
        elif operator == '/':
            result = num1 / num2
            print(result)
        else:
            print("WRONG INPUT!!!!")
        self.history.append({'num1' : num1,
                            'num2' : num2,
                            'operator' : operator,
                            'result' : result})
        self.save_to_file()
    def view_history(self):
        if len(self.history) == 0 :
            print("no history")
        else:
            for record in self.history:
                   print(f"expression = {record['num1'], record['operator'], record['num2']}= {record['result']}")
    def remove_history(self):
        remove_history = input("Enter the y to remove n to cancell: ").lower()
        if remove_history == 'y':
                self.history.clear()
                print("Removed successfully ✅")
                self.save_to_file()
                return
        print("cancelled")
    def menu(self):
        while True :
            menu = int(input('1. calculate\n'
                    "2. view history\n"
                    "3.remove history\n"
                    "4. exit\n"))
            if menu == 1 :
                self.calculate()
            elif menu == 2 :
                self.view_history()
            elif menu == 3 :
                self.remove_history()
            else :
                break
manager = Calculator()
manager.menu()
