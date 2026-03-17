# DeWeb
Un piccolo parser per creare finestre con pagine web usando Python.

---

# Esempi

## Una pagina con Google

Possiamo aprire una pagina con _www.google.com_ così:

```python
from DeWeb.browser import DeWebParser

DeWebParser.prepare_load()
DeWebParser.load("https://www.google.com", "Google")
```
Così verrà caricata la pagina di Google in una finestra separata.

## Una pagina GitHub Pages

Ecco come aprire una pagina su GitHub Pages:

```python
from DeWeb.browser import DeWebParser

DeWebParser.prepare_load()
DeWebParser.load("https://demenigeco.github.io/functions/pk", "Esempio")
```

--

# Licenza
Licenza **Apache 2.0**

--

# Altre librerie

Dai un’occhiata anche al mio pacchetto [utiilityes](https://pypi.org/project/utiilityes)

# Tabbella versioni

 | Versione | Stato | Note |
 | -------- | ----- | ---- |
 | 1.0.0 | Acctabile | - |
 | 1.0.1 | Accetabile | Gestione degli errori | 
 | 1.0.2 | Nuova | test.py nuovo e nuovo SetFlag() |


 # Community Fandom
 
 Fai nella nostra community fandom di DeWeb
 👉 [Vai alla Community](https://utiteam-deweb.fandom.com/it/wiki/DeWeb_Wiki)
 👉 [Documentazione Ufficiale](https://utiteam-deweb.fandom.com/it/wiki/Documentazione_ufficiale)

