from Layout import *
from FileReader import *
from CardGenerator import *


def generateFiles(path):
    cards = readCSV(path) if path.endswith(".csv") else readJSON(path)
    print(cards)
    generateIndividualCardsJPEG(cards, values["colorChooserButton"])


if __name__ == '__main__':
    window = sg.Window(
        title="CodeRush - Gerador de Cartas",
        layout=layout,
        margins=(200, 150)
    )

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == "generateButton":
            # VERIFICAR OUTROS CAMPOS #
            if values["fileBrowserInput"]:
                generateFiles(values["fileBrowserInput"])
    window.Close()
