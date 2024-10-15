while True:
    user_action = input("Type add show edit complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ") + "\n"

            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()

            todo_list.append(todo)

            with open('files/todo.txt', 'w') as file:
                todo_list = file.writelines(todo_list)

        case 'show':
            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()

            # new_todo_list = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{index + 1}) {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()

            new_todo = input("Enter new todo: ")

            todo_list[number] = new_todo + '\n'
            with open('files/todo.txt', 'w') as file:
                file.writelines(todo_list)

        case 'complete':
            number = int(input("Number of to-do to complete: "))

            with open('files/todo.txt', 'r') as file:
                todo_list = file.readlines()
            todo_to_remove = todo_list[number-1].strip('\n')
            print(f"Todo {number}) '{todo_to_remove}' was removed.")

            todo_list.pop(number - 1)
            with open('files/todo.txt', 'w') as file:
                file.writelines(todo_list)

        case 'exit':
            break
