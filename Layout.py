import PySimpleGUI as sg

config_column = [
    [
        sg.Text(
            text="Arquivo (.csv / .json)",
            pad=((10, 0), (25, 0))
        ),
    ],
    [
        sg.In(
            key="fileBrowserInput",
            disabled=True,
        ),
        sg.FileBrowse(
            button_text="Abrir",
            target="fileBrowserInput",
            file_types=(
                ("CSV Files", "*.csv"),
                ("JSON Files", "*.json")
            )
        )
    ],
    [
        sg.Text(
            text="Pasta de destino",
            pad=((10, 0), (25, 0))
        ),
    ],
    [
        sg.In(
            key="folderBrowserInput",
            disabled=True,
        ),
        sg.FolderBrowse(
            button_text="Procurar",
            key="folderBrowserInput"
        )
    ],
    [
        sg.Text(
            text="Cor de fundo",
            pad=((10, 0), (25, 0))
        ),
    ],
    [
        sg.In(
            key="colorChooserButton",
        ),
        sg.ColorChooserButton(
            button_text="Escolher",
            key="colorChooserButton"
        )
    ],
    [
        sg.Button(
            button_text="Gerar",
            key="generateButton"
        )
    ]
]

layout = [
    [
        sg.Column(config_column),
        sg.VSeparator(),
    ]
]