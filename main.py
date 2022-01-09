from Layout import *
from FileReader import *
from CardGenerator import *


def generateFiles(path):
    cards = readCSV(path) if path.endswith(".csv") else readJSON(path)
    card_imgs = generateIndividualCardsJPEG(cards, values["colorChooserButton"], values["folderBrowserInput"])
    generatePrintablePDFs(card_imgs, values["folderBrowserInput"])


if __name__ == '__main__':
    window = sg.Window(
        title="CodeRush - Gerador de Cartas",
        icon="assets/images/icon.ico",
        titlebar_icon="assets/images/icon.ico",
        layout=layout,
        margins=(50, 50)
    )

    while True:
        event, values = window.read()
        if event == "generateButton":
            if values["fileBrowserInput"] and values["folderBrowserInput"] and values["colorChooserButton"]:
                generateFiles(values["fileBrowserInput"])
        elif event in (None, 'Exit'):
            break

    window.Close()
