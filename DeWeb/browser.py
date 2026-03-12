from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sys

class DeWebParser:

    @staticmethod
    def prepare_load():
        charged = False

        print("===============================")
        print("          DeWeb Parser         ")
        print("===============================")
        print("Questo file usa DeWeb, grazie per il supporto!")
        print("DeWeb sta caricando l'interfaccia... attendi")

        charged = True

        if charged:
            print("Caricato con successo!")

    @staticmethod
    def load(url="https://www.google.com", pagetitle="DeWeb"):
        app = QApplication(sys.argv)
        view = QWebEngineView()
        view.load(QUrl(url))
        view.setWindowTitle(pagetitle if pagetitle else url)
        view.show()
        sys.exit(app.exec())