from datetime import datetime
class toDO:

    def __init__(self):
        self.tasks = []

    def displayTasks(self):
        if not self.tasks:
            print("List is empty! please add some tasks")
            
        else:    
            for tasks in self.tasks:
                print(f"* {tasks}")
    
    def addTask(self, taskName):
        if taskName in self.tasks:
            print("Task is already added! do u want to replace it")
        else:
            self.tasks.append(taskName)
            print(f"Task {taskName} added successfully at {datetime.now()}")
    
    def deleteTask(self, taskName):
        if taskName in self.tasks:
            self.tasks.remove(taskName)
            print("Task deleted successfully! Hope you completed it !")
        else:
            print("Task not found in the list! Enter a pre-defined task!")
    
class User:

    def addWork(self):
        self.tasks = input("Enter task or work Title: ")
        return self.tasks
    def removeWork(self):
        self.tasks = input("Enter task or work Title you want to delete : ")
        return self.tasks

if __name__ == "__main__":

    todos = toDO()
    user = User()
    
    while(True):
        msg = '''------Welcome to TODOs app------
        Choose an option :
        1. List of tasks 
        2. Add a task
        3. Remove a task
        4. Exit the app'''

        print(msg)
        a=int(input("Enter choice : "))
        if a==1:
            
            todos.displayTasks()
        elif a==2:
            todos.addTask(user.addWork())
        elif a==3:
            todos.deleteTask(user.removeWork())
        elif a==4:
            print("--Thanks for using the app--")
            exit()
        else:
            print("Enter a valid choice!")

