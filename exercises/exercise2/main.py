import FreeSimpleGUI as sg

lbl1 = sg.Text("Enter feet:")
entry1 = sg.Input()

lbl2 = sg.Text("Enter inches:")
entry2 = sg.Input()

convert_btn = sg.Button("Convert")

window = sg.Window("File Compressor", layout=[
    [lbl1, entry1],
    [lbl2, entry2],
    [convert_btn]
]
                   )

window.read()
window.close()
