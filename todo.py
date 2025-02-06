import os
import json
from datetime import date

"""""
2/3/25 Update: changed todo file from .txt to json since
I plan to intergrate this code into bigger projects where 
json is much more easier to parse through. ex: website

Moreover, I find using creating the underlying needs and motivations
easier using the json format rather than using dictionaires :p
"""""

# this file is used to store tasks
todoFile = "todo.json"


def loadTasks():
    """

    """
    if os.path.exists(todoFile):
        with open(todoFile, "r") as file:
            return json.load(file)
    return {}

# this function saves a list of tasks to todo.txt
# listOfNewTasks: array of strings
def saveTasks(listOfTasks ):
    with open(todoFile, "w") as file:
        json.dump(listOfTasks, file, indent=4)


#this function shows all existing tasks on todo.txt
# listOfNewTasks: array of strings
def showTasks(listOfTasks ):
    today = date.today()
    if "":
        print("There is no existing tasks at this time. Add a task or check code for error.")
    else:
        print("Here is your To-Do List as of", today)
        for i, (listOfTasks, listOfNeeds)  in enumerate(listOfTasks.items(), start=1):
            print(f"{i}. {listOfTasks }")
            for j, listOfNeeds in enumerate(listOfNeeds, start=1):
                print(f" {i}.{j}. {listOfNeeds}")

#this function will add a task from the array listOfTasks
# listOfNewTasks: array of strings
def addTask(listOfTasks):
    task = input("Enter a new task: ") 
    if task in listOfTasks:
        print("Task already exists")
    else:
        listOfTasks[task] = []
        saveTasks(listOfTasks=listOfTasks)
        print(f"{task} has been added to the to the list of tasks.")

def addNeed(listOfTasks):
    showTasks(listOfTasks)
    try:
        taskNum = int(input("Enter the task number you want to add your need under:"))
        if 1 <= taskNum <= len(listOfTasks):
            task = list(listOfTasks.keys())[taskNum -1]
            need = input("Enter the need you fulfill when you complete this task: ")
            listOfTasks[task].append(need)
            saveTasks(listOfTasks)
            print(f"Added need meet by completeing task: {need} to {task}")
        else:
            print("Task number does not exist")
    except ValueError:
        print("Not a number. Please input a valid integer. ex: 1, 2, 3")
            

#this function will delete a task from the array listOfTasks
# listOfNewTasks: array of strings
def deleteTask(listOfTasks):
    showTasks(listOfTasks)
    try:
        taskNum = int(input("Enter the task number to delete: "))
        if 1 <= taskNum <= len(listOfTasks):
            task = list(task.keys())[taskNum - 1]
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
        print("3. Add a need")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            showTasks(listOfTasks=listOfTasks)
        elif choice == "2":
            addTask(listOfTasks=listOfTasks)
        elif choice == "3":
            addNeed(listOfTasks=listOfTasks)
        elif choice == "4":
            deleteTask(listOfTasks=listOfTasks)
        elif choice == "5":
            print("Goodbye. Come back soon! :)")
            break
        else:
            print("Invalid choice. PLease try again.")

if __name__ == "__main__":
    main()

