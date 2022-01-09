import PySimpleGUI as sg

config_column = [
    [
        sg.Image(
            filename="assets/images/CodeRush_logo.png",
            subsample=2,
            pad=((50, 0), (0, 25))
        )
    ],
    [
        sg.Text(
            text="Arquivo (.csv / .json)",
            pad=((10, 0), (10, 0))
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
            ),
            size=(8, 1)
        )
    ],
    [
        sg.Text(
            text="Pasta de destino",
            pad=((10, 0), (10, 0))
        ),
    ],
    [
        sg.In(
            key="folderBrowserInput",
            disabled=True,
        ),
        sg.FolderBrowse(
            button_text="Procurar",
            key="folderBrowserInput",
            auto_size_button=True,
            size=(8, 1)
        )
    ],
    [
        sg.Text(
            text="Cor de fundo",
            pad=((10, 0), (10, 0))
        ),
    ],
    [
        sg.In(
            key="colorChooserButton",
        ),
        sg.ColorChooserButton(
            button_text="Escolher",
            key="colorChooserButton",
            size=(8, 1)
        )
    ],
    [
        sg.Button(
            button_text="Gerar",
            expand_y=True,
            expand_x=True,
            pad=((0, 0), (40, 0)),
            key="generateButton"
        )
    ]
]

layout = [
    [
        sg.Column(config_column)
    ]
]
