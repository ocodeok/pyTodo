import PySimpleGUI as sq

import modules

label = sq.Text("Type in a to-do")
inputBox = sq.InputText(tooltip="Enter a todo")
addButton = sq.Button("Add")

window = sq.Window("My To-Do App", layout=[[label], [inputBox, addButton]])
window.read()
window.close()