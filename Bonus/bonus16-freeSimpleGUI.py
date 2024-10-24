import FreeSimpleGUI as sg

lbl1 = sg.Text("Select files to compress: ")
entry1 = sg.Input()
btn1 = sg.FilesBrowse("Choose")

lbl2 = sg.Text("Select destination folder: ")
entry2 = sg.Input()
btn2 = sg.FolderBrowse("Confirm")

confirm_btn = sg.Button("Confirm")

window = sg.Window("File Compressor", layout=[
    [lbl1, entry1, btn1],
    [lbl2, entry2, btn2],
    [confirm_btn]
]
                   )

window.read()
window.close()
