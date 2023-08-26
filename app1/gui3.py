from modules import functions
import PySimpleGUI as sg

sg.theme("DarkBlue")

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo ", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            add_todo = values["todo"] + "\n"
            todos.append(add_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todos = functions.get_todos()
            todo_to_edit = values["todos"][0]
            index = todos.index(todo_to_edit)
            new_todo = values["todo"]
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)

        case "todos":
            window["todo"].update(value=(values["todos"][0]).strip())

        case sg.WIN_CLOSED:
            break

window.close()
