import functions
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("To do app")
window.geometry('650x650')


def add_todo_gui(new_todo):
    list_content = functions.get_todo_list()
    list_content.append(new_todo + '\n')
    functions.set_todo_list(list_content)

    print_lbl = tb.Label(list_frame, text=new_todo, bootstyle="success")
    last_index = len(list_content)
    print_lbl.grid(column=0, row=last_index + 1, sticky="w")


def edit_todo(new_todo):
    index_edit = int(index_entry.get())
    print(index_edit)
    list_content = functions.get_todo_list()
    list_content[index_edit] = str(new_todo + '\n')
    functions.set_todo_list(list_content)

    print_lbl = tb.Label(list_frame, text=str(index_edit) + ") " + (" " * 15) + new_todo, bootstyle="warning")
    print_lbl.grid(column=0, row=index_edit, pady=5, sticky="w")


# ---------- Title ---------- #
title_lbl = tb.Label(text="Welcome to the TO DO app", font=("Helvetica", 20, "bold"))
title_lbl.pack(pady=(60, 5))

data_frame = tb.Frame(window)
data_frame.pack()

# ---------- Data Frame ---------- #
style = tb.Style()
style.configure('success.TButton', font=("Helvetica", 12))

new_todo_entry = tb.Entry(data_frame, width=80)
new_todo_entry.pack(pady=10)

new_todo_btn = tb.Button(data_frame, text="Add", bootstyle="success",
                         command=lambda: add_todo_gui(new_todo_entry.get()), width=25)
new_todo_btn.pack(padx=10, pady=(0, 10))

index_lbl = tb.Label(data_frame, text="Enter the index", font=("Segoe UI", 10, "bold"))
index_lbl.pack(pady=(5, 0))

index_entry = tb.Entry(data_frame, width=10)
index_entry.pack(pady=(0, 10))

# ---------- Button Frame ---------- #
btn_frame = tb.Frame(data_frame)
btn_frame.pack()

edit_btn = tb.Button(btn_frame, text="Edit", bootstyle="outline-info", width=10,
                     command=lambda: edit_todo(new_todo_entry.get()))
edit_btn.pack(padx=10, pady=(0, 10), side='left', fill='both')

delete_btn = tb.Button(btn_frame, text="Complete", bootstyle="outline-warning", width=10,
                       command=lambda: edit_todo(new_todo_entry.get()))
delete_btn.pack(padx=10, pady=(0, 10), side='left', fill='both')

list_frame = tb.Frame(data_frame)
list_frame.pack()
content = functions.get_todo_list()
for index, item in enumerate(content):
    actual_string = str(index) + ") " + item.strip('\n')
    print_lbl = tb.Label(list_frame, text=actual_string, font=("Segoe UI", 10, "italic"))
    print_lbl.grid(column=0, row=index, pady=5, sticky="w")

window.mainloop()
