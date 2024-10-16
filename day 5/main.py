while True:
    user_action = input("Command prompts "
                        "add <String>, "
                        "show, edit <Int>, "
                        "complete <Int> or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = (user_action[4:] + '\n').capitalize()

        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()

        todo_list.append(todo)

        with open('files/todo.txt', 'w') as file:
            todo_list = file.writelines(todo_list)

    elif user_action.startswith('show'):
        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()

        # new_todo_list = [item.strip('\n') for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = f"{index + 1}) {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()

            new_todo = input("Enter new todo: ")

            todo_list[number] = new_todo + '\n'
            with open('files/todo.txt', 'w') as file:
                file.writelines(todo_list)
        except ValueError:
            print("Invalid")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])

            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()
            todo_to_remove = todo_list[number - 1].strip('\n')
            print(f"Todo {number}) '{todo_to_remove}' was removed.")

            todo_list.pop(number - 1)
            with open('files/todo.txt', 'w') as file:
                file.writelines(todo_list)
        except IndexError:
            print(f"Todo number {number} doesn't exist")
        except ValueError:
            print("Enter a valid number")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid prompt")
