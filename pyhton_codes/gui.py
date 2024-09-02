import functions
import FreeSimpleGUI as sg
import time
import os

# creates "todos.txt" for the first time.
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass


sg.theme('DarkPurple4')

# Define GUI elements
clock = sg.Text("", key="CLOCK")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Type in a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=[todo.strip() for todo in functions.get_todos()],
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

mylayout = [[clock],
            [label],
            [input_box, add_button],
            [list_box, edit_button, complete_button],
            [exit_button]]

# Create the window
window = sg.Window("My To-Do App",
                   layout=mylayout,
                   font=("Helvetica", 20))

# Event loop
while True:
    event, values = window.read(timeout=10)

    # Handle the window being closed with "X" or 'Exit' button
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break

    window["CLOCK"].update(value=time.strftime("%Y-%m-%d %H:%M:%S"))

    match event:
        case "Add":
            new_todo = values["todo"].strip()  # Get the input text
            if new_todo:  # Check if the input is not empty
                todos = functions.get_todos()  # Get the current list of to-dos
                todos = [todo.strip() for todo in todos]  # Remove newline characters
                todos.append(new_todo)  # Add the new to-do
                functions.write_todos([todo + "\n" for todo in todos])  # Write to file with newlines
                window["todos"].update(values=todos)  # Update the listbox with the new list
                window["todo"].update("")  # Clear the input field after adding
            else:
                sg.popup("Please enter a to-do item!", title="Error")

        case "Edit":
            try:
                selected_todo = values["todos"][0]  # Get the selected to-do item
                new_todo = sg.popup_get_text("Edit To-Do", default_text=selected_todo,
                                             font=("Helvetica", 20))  # Get new input from the user
                if new_todo:  # If the new input is not empty
                    todos = functions.get_todos()
                    todos = [todo.strip() for todo in todos]  # Remove newline characters
                    index = todos.index(selected_todo)
                    todos[index] = new_todo  # Replace the selected to-do
                    functions.write_todos([todo + "\n" for todo in todos])  # Write to file with newlines
                    window["todos"].update(values=todos)  # Update the listbox with the new list
            except IndexError:
                sg.popup("Please select a to-do to edit!", title="Error", font=("Helvetica", 15))

        case "Complete":
            try:
                to_do_tocomplete = values["todos"][0]
                todos = functions.get_todos()
                todos = [todo.strip() for todo in todos]  # Remove newline characters
                todos.remove(to_do_tocomplete)
                functions.write_todos([todo + "\n" for todo in todos])
                window["todos"].update(values=todos)
                window["todo"].update("")  # Clear the input field after completing
            except IndexError:
                sg.popup("Please select a to-do to complete!", title="Error", font=("Helvetica", 15))


window.close()