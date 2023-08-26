import PySimpleGUI as sg
from modules import zip_extractor as zip_ex

sg.theme("Black")

label1 = sg.Text("Select archive file: ")
input1 = sg.Input(key="file_path")
choose_button1 = sg.FileBrowse("Choose", key="archive", file_types=(("Zip Files", "*.zip"),))

label2 = sg.Text("Select archive file: ")
input2 = sg.Input(key="dir_path")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract", key="extract")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("Archive Extractor",
                   layout=[ [label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    if event == "extract":
        zip_ex.extract_archive(values["archive"], values["folder"])
        # output_label.update("Archive extracted successfully!") # Code autogenerated
        window["output"].update("Extraction Completed!")
    if event == sg.WIN_CLOSED:
        break

window.close()