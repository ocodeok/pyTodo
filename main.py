
# todos = ["clean\n", "prepare\n", "learn\n"]
todos = []

while True:
    userAction = input("\nType add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    match userAction:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            with open("files/tasks.tsk", "r") as file:
                todos = file.readlines()

            todos.append(todo.capitalize())

            with open("files/tasks.tsk", "w") as file:
                file.writelines(todos)
        case "show":
            with open("files/tasks.tsk", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"[№ {index}] {item}", end="")
        case "edit":
            with open("files/tasks.tsk", "r") as file:
                todos = file.readlines()

            number = int(input("Number of the todo to edit: "))

            newTodo = input("Enter a new todo: ")
            todos[number] = newTodo + "\n"

            with open("files/tasks.tsk", "w") as file:
                file.writelines(todos)
        case "complete":
            with open("files/tasks.tsk", "r") as file:
                todos = file.readlines()

            number = int(input("Number of the todo to complete: "))
            removedTodo = todos[number].strip("\n")
            todos.pop(number)

            with open("files/tasks.tsk", "w") as file:
                file.writelines(todos)

            message = f"Todo {removedTodo} was removed from the list."
            print(message)
        case "exit":
            break
        case whatever:
            print("Our product does not support such a command")

print("Thank you for using our service")