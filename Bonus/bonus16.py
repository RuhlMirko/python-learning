import ttkbootstrap as tb
from tkinter.filedialog import askopenfile

window = tb.Window(themename="darkly")
window.title("file zipper")


compress_frame = tb.Frame(window)
compress_frame.pack(pady=10, padx=15)

select_lbl = tb.Label(compress_frame, text="Select files to compress")
select_lbl.pack(side="left", padx=5)

select_entry = tb.Entry(compress_frame)
select_entry.pack(side="left", padx=5)

select_btn = tb.Button(compress_frame, text="Select file", command=askopenfile)
select_btn.pack(side="left", padx=5)



file_frame = tb.Frame(window)
file_frame.pack()

window.mainloop()
