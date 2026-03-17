from DeWeb.browser import DeWebParser

def Init():
    links = {
        "0": "https://www.google.com",
        "1": "https://utiteam-deweb.fandom.com/it/wiki/DeWeb_Wiki",
        "2": "https://example.com"
    }
    
    for key, value in links.items():
        print(f"{key}: {value}")

    code = input("Inserisci il codice del link che vuoi aprire: ")
    
    if code in links:
        DeWebParser.prepare_load()
        DeWebParser.load(links[code], f"Test Page: {links[code]}")
    else:
        print("Codice non valido.")

Init()