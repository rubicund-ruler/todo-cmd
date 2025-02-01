import os
from datetime import date

# this file is used to store tasks
todoFile = "todo.txt"

#this function loads tasks from todo.txt
def loadTasks():
    listOfTasks = []
    if os.path.exists(todoFile):
        with open(todoFile, "r") as file:
            tlistOfTasks =  file.readlines()
    for task in listOfTasks:
        task.strip()
    return listOfTasks

# this function saves a list of tasks to todo.txt
# listOfNewTasks: array of strings
def saveTasks(listOfTasks ):
    with open(todoFile, "w") as file:
        for task in listOfTasks :
            file.write(task + "\n")

#this function shows all existing tasks on todo.txt
# listOfNewTasks: array of strings
def showTasks(listOfTasks ):
    today = date.today()
    if "":
        print("There is no existing tasks at this time. Add a task or check code for error.")
    else:
        print("Here is your To-Do List as of", today)
        for i, listOfTasks  in enumerate(listOfTasks , start=1):
            print(f"{i}. {listOfTasks }")

#this function will add a task from the array listOfTasks
# listOfNewTasks: array of strings
def addTask(listOfTasks):
   task = input("Enter a new task: ") 
   listOfTasks.append(task)
   saveTasks(listOfTasks=listOfTasks)
   print(f"{task} has been added to the to the list of tasks.")

#this function will delete a task from the array listOfTasks
# listOfNewTasks: array of strings
def deleteTask(listOfTasks):
    showTasks(listOfTasks)
    try:
        taskNum = int(input("Enter the task number to delete: "))
        if 1 <= taskNum <= len(listOfTasks):
            removeTask = listOfTasks.pop(taskNum - 1)
            saveTasks(listOfTasks=listOfTasks)
            print(f"{removeTask} has been removed from task list.")
        else:
            print("Task number inputted is invalid")
    except ValueError:
        print("Please enter a valid number.")

def main():
    listOfTasks = loadTasks() 
    while True:
        print("\nOptions:")
        print("1. View Tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice ==  "1":
            showTasks(listOfTasks=listOfTasks)
        elif choice == "2":
            addTask(listOfTasks=listOfTasks)
        elif choice == "3":
            deleteTask(listOfTasks=listOfTasks)
        elif choice == "4":
            print("Goodbye. Come back soon! :)")
            break
        else:
            print("Invalid choice. PLease try again.")

if __name__ == "__main__":
    main()

