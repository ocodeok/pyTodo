def getTodos(filepath="files/tasks.tsk"):
    """ Read a text file and return the list of to-do items\n
    --------- ---------------------------------------------------------------\n
    'filepath'      the base path to the file and default value is "files/tasks.tsk" """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def writeTodos(todos, filepath="files/tasks.tsk"):
    """ Write the to-do items list in the text file\n
    --------- ---------------------------------------------------------------\n
    'filepath'      the base path to the file and default value is "files/tasks.tsk"\n
    'todos' - list of to-do items """

    with open(filepath, "w") as file:
        file.writelines(todos)

# todos = ["clean\n", "prepare\n", "learn\n"]
todos = []

while True:
    userAction = input("\nType add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    if userAction.startswith("add"):
        todo = userAction[4:]

        todos = getTodos()

        todos.append(todo.capitalize() + "\n")

        writeTodos(todos)
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

            writeTodos(todos)
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

                writeTodos(todos)

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
