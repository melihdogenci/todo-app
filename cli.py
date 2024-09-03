import time
import functions

now = time.strftime("%Y-%m-%d %H:%M:%S")
print("It is:", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        with open("todos.txt", "a") as file:
            file.write(todo)

    elif user_action.startswith("show"):
        todos= functions.get_todos()
        for index, todo in enumerate(todos):
            item = todo.strip("\n")
            row = f"{index + 1} - {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            todos= functions.get_todos()
            number = int(user_action[5:]) - 1
            if 0 <= number < len(todos):
                new_todo = input("Enter a new todo: ") + "\n"
                todos[number] = new_todo
                functions.write_todos(todos)
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")
            continue

    elif user_action.startswith("complete"):
        try:
            todos= functions.get_todos()
            number = int(user_action[9:]) - 1
            if 0 <= number < len(todos):
                removed_todo = todos[number].strip("\n")
                todos.pop(number)
                functions.write_todos(todos)

                message = f"Todo '{removed_todo}' has been removed."
                print(message)
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid command, please try again.")

print("Bye!")


