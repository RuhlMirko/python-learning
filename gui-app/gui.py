import functions
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("To do app")
window.geometry('650x650')

# ---------- Title ---------- #
title_lbl = tb.Label(text="Welcome to the TO DO app", font=("Helvetica", 20, "bold"))
title_lbl.pack(pady=(60, 5))

data_frame = tb.Frame(window)
data_frame.pack()


def add_todo_gui(new_todo):
    list_content = functions.get_todo_list()
    list_content.append(new_todo + '\n')
    functions.set_todo_list(list_content)

    print_lbl = tb.Label(list_frame, text=new_todo)
    last_index = len(list_content)
    print_lbl.grid(column=0, row=last_index+1, sticky="w")



def edit_todo(new_todo, index_edit):
    print(index_edit)
    list_content = functions.get_todo_list()
    list_content[index_edit] = str(new_todo)
    functions.set_todo_list(list_content)

    print_lbl = tb.Label(list_frame, text=new_todo, bootstyle="warning")
    print_lbl.grid(column=0, row=index_edit, pady=5, sticky="w")


# ---------- Data Frame ---------- #
style = tb.Style()
style.configure('success.TButton', font=("Helvetica", 16))

new_todo_entry = tb.Entry(data_frame, width=80)
new_todo_entry.pack(pady=10)

new_todo_btn = tb.Button(data_frame, text="Add", bootstyle="success", command=lambda: add_todo_gui(new_todo_entry.get()))
new_todo_btn.pack(padx=10, fill="both", pady=(0, 10))

list_frame = tb.Frame(data_frame)
list_frame.pack()
content = functions.get_todo_list()
for index, item in enumerate(content):
    print_lbl = tb.Label(list_frame, text=item.strip("\n"), font=("Segoe UI", 10, "italic"))
    print_lbl.grid(column=0, row=index, pady=5, sticky="w")

    edit_btn = tb.Button(list_frame, text="Edit", bootstyle="secondary", command=lambda: edit_todo(new_todo_entry.get(), index))
    edit_btn.grid(column=1, row=index, padx=20)

window.mainloop()
