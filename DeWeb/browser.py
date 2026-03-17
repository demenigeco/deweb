from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
import sys

class DeWebParser:

    charged = False

    @staticmethod
    def DeWebError(code):
            print(f"Avviso: {code}:")
            if code=="DeWebParserInitError":
                print("+DeWebParser        :        Errore nell'interprete")
                print("+InitError          :        Errore nell'inizializzazione")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("È possibile risolvere al link https://utiteam-deweb.fandom.com/it/wiki/Codici_Errore")
                raise SystemExit
            elif code=="DeWebParserLogInited":
                    print("+DeWebParser        :        Errore nell'interprete")
                    print("+LogInited          :        I log sono stati inizzializzati")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("È possibile risolvere al link https://utiteam-deweb.fandom.com/it/wiki/Codici_Errore")
            elif code=="DeWebSecureDead":
                    print("+DeWebParser        :        Errore nell'interprete")
                    print("+Secure             :        Avviso di sicurezza")
                    print("+Dead               :        Esecuzione Bloccata")
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("È possibile risolvere al link https://utiteam-deweb.fandom.com/it/wiki/Codici_Errore")
                    raise SystemExit
            elif code=="QtFlagsError":
                        print("+Qt                 :        Errore in QtWebEngine/Chromium")
                        print("+FlagsError         :        Errore di flags")
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        print("È possibile risolvere al link https://utiteam-deweb.fandom.com/it/wiki/Codici_Errore")




    @staticmethod
    def SetFlag(flag, value):
        # Flag di QtWebEngine
        # Se ci sono -> OK
        # Se non ci sono: DeWebError("QtFlagsError")

        from PySide6.QtWebEngineCore import QWebEngineSettings

        # Ottieni le impostazioni globali
        settings = QWebEngineSettings.defaultSettings()

        try:
            # Ottieni il flag da Qt (enum WebAttribute)
            qt_flag = getattr(QWebEngineSettings.WebAttribute, flag)

            #   Imposta il valore (True/False)
            settings.setAttribute(qt_flag, value)

        except AttributeError:
            # Flag non esistente
            DeWebParser.DeWebError("QtFlagsError")

    @staticmethod
    def prepare_load():

        print("===============================")
        print("          DeWeb Parser         ")
        print("===============================")
        print("Questo file usa DeWeb, grazie per il supporto!")
        print("DeWeb sta caricando l'interfaccia... attendi")

        DeWebParser.charged = True

        if DeWebParser.charged:
            print("Caricato con successo!")

        print("")
        print("================================")
        print("                LOGS            ")
        print("================================")
        DeWebParser.DeWebError("DeWebParserLogInited")
        

    @staticmethod
    def load(url="https://www.google.com", pagetitle="DeWeb"):
        if DeWebParser.charged:
            app = QApplication(sys.argv)
            view = QWebEngineView()
            view.load(QUrl(url))
            view.setWindowTitle(pagetitle if pagetitle else url)
            view.show()
            sys.exit(app.exec())
        else:
            DeWebParser.DeWebError("DeWebParserInitError")