

print("Welcome back")
user_input = input("Type add or show: ").lower().strip()

todo_list = []
while True:
    match user_input:
        case "add":
            while True:
                todo_input = input("Enter a todo: ").capitalize()
                if todo_input == "exit":
                    break
                todo_list.append(todo_input)
        case "show":
            print(todo_list)
        case "exit":
            break

    user_input = input("Type add or show: ").lower()






