#Export file names from a folder to a text file

import PySimpleGUI as sg
import os.path

sg.theme('DarkGrey1') 

#File browse frame

file_list_frame = [
    [
        sg.Text("Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(values=['No Folder selected'], size=(40, 20), key="-FILE LIST-")
    ],
]

#Output frame

output_frame = [
    [
        sg.Text('Exported filename: '),
        sg.In(size=(20,1), default_text='filelist', key='-OUTPUT FILENAME-'),
    ],
    [
        sg.Button('Export', size=(10,1)),
    ],
    [
        sg.Text('Credits to Saruen'),
    ],
]

# -Full layout-
layout = [
    [
        sg.Frame('', file_list_frame),
        sg.VSeperator(),
        sg.Frame('', output_frame),
    ],
]

window = sg.Window('File names exporter', layout)
fnames = []

#Program Loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-FOLDER-' and not values['-FOLDER-']:
        window.Element('-FILE LIST-').update(['No Folder selected'])
    elif event == '-FOLDER-':
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        
        if os.path.exists(folder):
            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
            ]
        else:
            fnames = ['Bad path']
        window['-FILE LIST-'].update(fnames)
    elif event == 'Export':
        ofile = values['-OUTPUT FILENAME-']

        with open(ofile+'.txt', 'w') as file:
            for f in fnames:
                file.write(f + '\n')
            file.write('\nTotal number of files: {}'.format(len(fnames)))
    
window.close()