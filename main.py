
todos = ["clean", "prepare", "learn"]
while True:
    userAction = input("Type add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    match userAction:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case "show":
            for index, item in enumerate(todos):
                print(f"[№ {index}] {item}")
        case "edit":
            number = int(input("Number of the todo to edit: "))

            newTodo = input("Enter a new todo: ")
            todos[number] = newTodo
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            break
        case whatever:
            print("Our product does not support such a command")

print("Thank you for using our service")