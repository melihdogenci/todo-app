def get_todos(filepath="todos.txt"):
    with open("todos.txt", "r") as file:
        todos = file.readlines()
        return todos

def write_todos(todos, filepath="todos.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos)