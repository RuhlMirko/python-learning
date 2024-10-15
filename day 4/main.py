

print("Welcome back")
user_input = input("Type add, show, edit, remove or exit: ").lower().strip()

todo_list = []
while True:
    match user_input:
        case "add":
            while True:
                todo_input = input("Enter a todo: ").capitalize()
                if todo_input == "Exit":
                    break
                todo_list.append(todo_input)
        case "show":
            for index, item in enumerate(todo_list):
                print(index, '-', item)
        case "edit":
            print(todo_list)
            user_edit = input("Type the word you want to edit: ").capitalize()
            index = todo_list.index(user_edit)
            todo_list[index] = input("Type the new word: ")
        case "remove":
            for index, item in enumerate(todo_list):
                print(index, '-', item)
            user_pop = input("Enter the number of the todo to remove: ")
            todo_list.pop(int(user_pop))
        case "exit":
            break

    user_input = input("Type add, show, edit, remove or exit: ").lower()





