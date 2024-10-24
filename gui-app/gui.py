import functions
import ttkbootstrap as tb

window = tb.Window(themename="darkly")
window.title("To do app")
window.geometry('700x500')

# ---------- Title ---------- #
title_lbl = tb.Label(text="Welcome to the TO DO app", font=("Helvetica", 20, "bold"))
title_lbl.pack(pady=(60, 5))

data_frame = tb.Frame(window)
data_frame.pack()

# ---------- Data Frame ---------- #
style = tb.Style()
style.configure('success.TButton', font=("Helvetica", 16))

new_todo_entry = tb.Entry(data_frame, width=80)
new_todo_entry.pack(pady=10)

new_todo_btn = tb.Button(data_frame, text="Add", bootstyle="success", command=lambda: print(new_todo_entry.get()))
new_todo_btn.pack(padx=10, fill="both", pady=(0, 10))

list_frame = tb.Frame(data_frame)
list_frame.pack()
content = functions.get_todo_list()
for index, item in enumerate(content):
    print_lbl = tb.Label(list_frame, text=item.strip("\n"), font=("Segoe UI", 10, "italic"))
    print_lbl.grid(column=0, row=index, ipady=0, sticky="w")

window.mainloop()
