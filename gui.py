import PySimpleGUI as sg

from modules.functions import getTodos, writeTodos

label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter a todo", key="todo")
listBox = sg.Listbox(values=getTodos(), key="todos", enable_events=True, size=(45, 10))

addButton = sg.Button("Add")
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[
        [label],
        [inputBox, addButton],
        [listBox, editButton, completeButton],
        [exitButton]],
    font=("Consolas", 20))

while True:
    event, values = window.read()
    # print("event", event)
    # print("values", values)

    match event:
        case "Add":
            todos = getTodos()
            newTodo = values['todo'] + "\n"
            todos.append(newTodo)
            writeTodos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            selectTodo = values["todos"][0]
            newTodo = values['todo']

            todos = getTodos()
            index = todos.index(selectTodo)
            print(index)
            todos[index] = newTodo
            writeTodos(todos)
        case "Complete":
            todoComplete = values['todos'][0]
            todos = getTodos()
            index = todos.index(todoComplete)
            todos.pop(index)
            writeTodos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break

window.close()