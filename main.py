
todos = []
while True:
    userAction = input("Type add, show or exit: ")
    userAction = userAction.strip()

    match userAction:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for item in todos:
                print(item)
        case "exit":
            break
        case whatever:
            print("Our product does not support such a command")

print("Thank you for using our service")