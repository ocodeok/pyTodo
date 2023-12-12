def getTodos():
    with open("files/tasks.tsk", "r") as file:
        todos = file.readlines()
    return todos

# todos = ["clean\n", "prepare\n", "learn\n"]
todos = []

while True:
    userAction = input("\nType add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        todo = userAction[4:]

        todos = getTodos()

        todos.append(todo.capitalize() + "\n")

        with open("files/tasks.tsk", "w") as file:
            file.writelines(todos)
    elif userAction.startswith("show"):
        todos = getTodos()

        for index, item in enumerate(todos):
            print(f"[№ {index}] {item}", end="")
    elif userAction.startswith("edit"):
        try:
            todos = getTodos()

            number = int(userAction[5:])

            newTodo = input("Enter a new todo: ")
            todos[number] = newTodo + "\n"

            with open("files/tasks.tsk", "w") as file:
                file.writelines(todos)
        except ValueError:
            print("Incorrect command form. You only need to enter the task number")
            continue
    elif userAction.startswith("complete"):
        try:
            try:
                todos = getTodos()

                number = int(userAction[9:])
                removedTodo = todos[number].strip("\n")
                todos.pop(number)

                with open("files/tasks.tsk", "w") as file:
                    file.writelines(todos)

                message = f"Todo {removedTodo} was removed from the list."
                print(message)
            except IndexError:
                print("There is no element with this number. Use the 'show' command")
                continue
        except ValueError:
            print("Incorrect command form. You only need to enter the task number")
            continue
    elif userAction.startswith("exit"):
        break
    else:
        print("Our product does not support such a command")

print("Thank you for using our service")