
# todos = ["clean\n", "prepare\n", "learn\n"]
todos = []

while True:
    userAction = input("\nType add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    if "add" in userAction:
        todo = userAction[4:] + "\n"

        with open("files/tasks.tsk", "r") as file:
            todos = file.readlines()

        todos.append(todo.capitalize())

        with open("files/tasks.tsk", "w") as file:
            file.writelines(todos)
    elif "show" in userAction:
        with open("files/tasks.tsk", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            print(f"[№ {index}] {item}", end="")
    elif "edit" in userAction:
        with open("files/tasks.tsk", "r") as file:
            todos = file.readlines()

        number = int(userAction[5:])

        newTodo = input("Enter a new todo: ")
        todos[number] = newTodo + "\n"

        with open("files/tasks.tsk", "w") as file:
            file.writelines(todos)
    elif "complete" in userAction:
        with open("files/tasks.tsk", "r") as file:
            todos = file.readlines()

        number = int(userAction[9:])
        removedTodo = todos[number].strip("\n")
        todos.pop(number)

        with open("files/tasks.tsk", "w") as file:
            file.writelines(todos)

        message = f"Todo {removedTodo} was removed from the list."
        print(message)
    elif "exit" in userAction:
        break
    else:
        print("Our product does not support such a command")

print("Thank you for using our service")