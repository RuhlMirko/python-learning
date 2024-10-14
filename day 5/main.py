todo_list = []

while True:
    user_action = input("Type add show edit complete or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a to-do: ")
            todo_list.append(todo)
        case 'show':
            for index, item in enumerate(todo_list):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number-1
        case 'complete':
            pass
        case 'exit':
            break

