import os
from datetime import datetime
import json

file_path: str = "tasks.json"

def write_in_file(tasks: list, path:str):
    with open(path,"w") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)

def read_file (path:str):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def is_file_exists(path: str):
    return os.path.exists(path)

def add_task(id: int, description: str):
    new_task = {}
    new_task["id"] = id
    new_task["description"] = description
    new_task["status"] = "todo"
    new_task["createdAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return new_task

def list_tasks(option: int, list_tasks: list):
    task_finded: list = []
    if option >= 5:
        return None
    if option == 1:
        task_finded.append(filter(lambda task: task["status"] == "todo", list_tasks))
    if option == 2:
        task_finded.append(filter(lambda task: task["in progress"] == "todo", list_tasks))
    if option == 3:
        task_finded.append(filter(lambda task: task["status"] == "done", list_tasks))
    if option == 4:
        return list_tasks
    return task_finded


def update_task(id: int, list_tasks: list):
    task_finded = filter(lambda task: task["id"] == id, list_tasks)
    if task_finded:
        for task in list_tasks:
            if task["id"] == id:
                update_option = int(input("update the status of the task\n1. To do\n2. In Progress\n3. Done\n4. Cancel\n\n"))
                if update_option >= 4:
                    break
                if update_option == 1:
                    task["status"] = "todo"
                if update_option == 2:
                    task["status"] = "in progress"
                if update_option == 3:
                    task["status"] = "done"
                write_in_file(list_tasks, file_path)  
                return task 
    else:
        return "The task doesn't exists"

