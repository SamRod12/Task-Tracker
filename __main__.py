from task_tracker import read_file, add_task, list_tasks, file_path, update_task, is_file_exists, write_in_file
from pprint import pprint
from time import sleep

def main():
    while True:
        tasks: list = read_file(path=file_path) if  is_file_exists(path=file_path) else []
        identifier: int = len(tasks) + 1
        sleep(1)
        option = int(input("What want to do?\n1. Add Task\n2. List Tasks\n3. Update Task\n4. Delete Task\n5. Exit\n\n"))
        
        if type(option) != int:
            print("did you wrote an invalid caracter, please input a valid option")
        if option >= 5:
            print("closing program")
            sleep(1)
            break
        if option == 1:
            task_input = input("Write a new task:\n")
            new_task = add_task(id=identifier, description= task_input)
            tasks.append(new_task)
            identifier += 1
            write_in_file(tasks, file_path)
            sleep(1)
        if option == 2:
            update_option = int(input("which task do you want to consult?\n1. To do\n2. In Progress\n3. Done\n4. List all\n5. Cancel\n\n"))
            task_finded = list_tasks(option=update_option, list_tasks= tasks)
            pprint(task_finded)
            sleep(1)
        if option == 3:
            task_input_id = int(input("write id of the task:\n\n"))
            response = update_task(id = task_input_id, list_tasks= tasks)
            pprint(response)
            sleep(1)
        if option == 4:
            task_input_id = int(input("write id of the task:\n\n"))
            task_to_remove = next((task for task in tasks if task["id"] == task_input_id), None)
            
            if task_to_remove:
                confirm_option = int(input("are you sur+e delete the task?\n1. Yes\n2. No\n\n"))
                if confirm_option > 1:
                    print("task didn't deleted")
                else:
                    task_input.remove(task_to_remove)
                    write_in_file(tasks, file_path)

            sleep(1)

# Esto asegura que el código solo se ejecute si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()