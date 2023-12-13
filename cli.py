from modules.functions import getTodos, writeTodos

import time

todos = []
now = time.strftime("%d/%m/%Y %H:%M:%S  %B %A")

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

