def get_todo_list(filepath="files/todo.txt"):
    """ Returns the content of the file to use it later """
    with open(filepath, 'r') as file:
        content = file.readlines()
    return content


def set_todo_list(def_list, filepath="files/todo.txt"):
    """ Modifies the file with a new list """
    with open(filepath, 'w') as file:
        file.writelines(def_list)


while True:
    user_action = input("\nCommand prompts "
                        "add <String>, "
                        "show, edit <Int>, "
                        "complete <Int> or exit: ").strip().lower()

    if user_action.startswith('add'):
        todo = (user_action[4:] + '\n').capitalize()
        todo_list = get_todo_list()
        todo_list.append(todo)

        set_todo_list(todo_list)

    elif user_action.startswith('show'):
        todo_list = get_todo_list()

        for index, item in enumerate(todo_list):
            item = item.strip('\n')
            row = f"{index + 1}) {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todo_list = get_todo_list()
            new_todo = input("Enter new todo: ")
            todo_list[number] = new_todo + '\n'

            set_todo_list(todo_list)

        except ValueError:
            print("Invalid")

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[8:])
            todo_list = get_todo_list()
            todo_to_remove = todo_list[number - 1].strip('\n')
            print(f"Todo {number}) '{todo_to_remove}' was removed.")
            todo_list.pop(number - 1)

            set_todo_list(todo_list)

        except IndexError:
            print(f"Todo number {number} doesn't exist")
        except ValueError:
            print("Enter a valid number")

    elif user_action.startswith('exit'):
        break

    else:
        print("Invalid prompt")
