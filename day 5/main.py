while True:
    user_action = input("Type add show edit complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ") + "\n"

            file = open("files/todo.txt", 'r')
            todo_list = file.readlines()
            file.close()

            todo_list.append(todo)

            file = open("files/todo.txt", 'w')
            file.writelines(todo_list)
            file.close()
        case 'show':
            file = open('files/todo.txt', 'r')
            todo_list = file.readlines()
            file.close()

            # new_todo_list = [item.strip('\n') for item in todo_list]

            for index, item in enumerate(todo_list):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todo_list[number] = new_todo
        case 'complete':
            number = int(input("Number of to-do to complete: "))
            todo_list.pop(number-1)
        case 'exit':
            break

