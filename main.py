
# todos = ["clean\n", "prepare\n", "learn\n"]
todos = []

while True:
    userAction = input("Type add, show. exit, complete or exit: ")
    userAction = userAction.strip()

    match userAction:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("files/tasks.tsk", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo.capitalize())

            file = open("files/tasks.tsk", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("files/tasks.tsk", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                print(f"[№ {index}] {item}", end="")
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