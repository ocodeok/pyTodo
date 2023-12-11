
todos = ["clean", "prepare", "learn"]
while True:
    userAction = input("Type add, show. exit or exit: ")
    userAction = userAction.strip()

    match userAction:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "edit":
            number = int(input("Number of todo to edit: "))

            newTodo = input("Enter a new todo: ")
            todos[number] = newTodo
        case "exit":
            break
        case whatever:
            print("Our product does not support such a command")

print("Thank you for using our service")