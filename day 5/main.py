while True:
    user_action = input("Command prompts "
                        "\nadd/new <String>,"
                        "\nshow, edit <Int>,"
                        "\ncomplete <Int> or exit: ").strip().lower()

    if 'add' in user_action or 'new' in user_action:
        todo = (user_action[4:] + '\n').capitalize()

        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()

        todo_list.append(todo)

        with open('files/todo.txt', 'w') as file:
            todo_list = file.writelines(todo_list)

    elif 'show' in user_action:
        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()

        # new_todo_list = [item.strip('\n') for item in todo_list]

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = f"{index + 1}) {item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()

        new_todo = input("Enter new todo: ")

        todo_list[number] = new_todo + '\n'
        with open('files/todo.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'complete' in user_action:
        number = int(user_action[8:])

        with open('files/todo.txt', 'r') as file:
            todo_list = file.readlines()
        todo_to_remove = todo_list[number - 1].strip('\n')
        print(f"Todo {number}) '{todo_to_remove}' was removed.")

        todo_list.pop(number - 1)
        with open('files/todo.txt', 'w') as file:
            file.writelines(todo_list)

    elif 'exit' in user_action:
        break

    else:
        print("Invalid prompt")
