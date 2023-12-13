import PySimpleGUI as sq

from modules.functions import getTodos, writeTodos

label = sq.Text("Type in a to-do")
inputBox = sq.InputText(tooltip="Enter a todo", key="todo")
addButton = sq.Button("Add")

window = sq.Window(
    "My To-Do App",
    layout=[[label], [inputBox, addButton]],
    font=("Consolas", 20))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todos = getTodos()
            newTodo = values['todo'] + "\n"
            print(newTodo)
            todos.append(newTodo)
            writeTodos(todos)
        case sq.WINDOW_CLOSED:
            break

window.close()