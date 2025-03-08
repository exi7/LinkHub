import time
import os

from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
g = Fore.LIGHTGREEN_EX

def wahl2():
    # Alle Kontakte aus der Datei laden
    with open('fichier.txt', 'r') as f:
        zeilen = f.readlines()

    # Die Liste der gespeicherten Kontaktpersonen anzeigen
    if zeilen:
        print("Hier ist die Liste der registrierten Personen:")
        for i, zeile in enumerate(zeilen, 1):
            name = zeile.split(' ')[0]  # Nur den Namen der Person extrahieren
            print(f"{i}. {name}")  # Nur den Namen anzeigen
    else:
        print("Das Verzeichnis ist leer.")
        time.sleep(3)
        menu()
        return

    # Abfrage der Suche (nach Name oder Nummer)
    suche = input("\nMöchten Sie nach Name (1) oder nach Nummer (2) suchen? : ")
    
    if suche == '1':  
        name = input("Wen suchen Sie? : ")
        gefundene_kontakte = []
        
        # Suche der Kontakte nach Namen
        for zeile in zeilen:
            if zeile.startswith(name + ' '):
                gefundene_kontakte.append(zeile.strip())  # Füge die vollständige Kontaktinformation hinzu
        
        if gefundene_kontakte:
            print(f"Gefundene Kontakte für {name} :\n")
            for kontakt in gefundene_kontakte:
                print(kontakt)
                
            datei_kontakt = f"Contact/{name}.txt"
            if os.path.exists(datei_kontakt):
                print("\nKontaktdetails :")
                with open(datei_kontakt, 'r') as f:
                    print(f.read())
        else:
            print(f"{name} ist nicht in Ihrem Verzeichnis registriert!")
        time.sleep(3)
        menu()
    
    elif suche == '2':  
        nummer = input("Welche Nummer suchen Sie? : ")
        gefundene_kontakte = []
        
        # Suche der Kontakte nach Nummer
        for zeile in zeilen:
            if nummer in zeile:
                gefundene_kontakte.append(zeile.strip())  # Füge die vollständige Kontaktinformation hinzu
        
        if gefundene_kontakte:
            print(f"Gefundene Kontakte für die Nummer {nummer} :\n")
            for kontakt in gefundene_kontakte:
                print(kontakt)  # Zeige alle Kontaktinformationen an
        else:
            print(f"{nummer} ist nicht in Ihrem Verzeichnis registriert!")
        
        time.sleep(3)
        menu()
        
    else:
        print("Ungültige Option. Bitte wählen Sie 1 oder 2.")
    menu()

def wahl1():
    name = input('Geben Sie einen Namen ein: ')
    nummer = input('Geben Sie die Nummer für diesen Namen ein: ')
    
    informationen = f"{name} {nummer}"  # Grundlegende Informationen
    kategorien = {}
    
    # Hinzufügen zusätzlicher Kategorien
    while True:
        kategorie = input("Geben Sie eine zusätzliche Kategorie ein (z.B. Adresse, E-Mail, Beruf, Discord) oder drücken Sie Enter, um zu beenden: ")
        if not kategorie.strip():  # Wenn die Eingabe leer ist, beenden
            break
        wert = input(f"Geben Sie den Wert für {kategorie} ein: ")
        kategorien[kategorie] = wert  # Füge die Kategorie und ihren Wert hinzu
        informationen += f" | {kategorie} : {wert}"  # Füge dem zu speichernden Text hinzu
    
    # Füge die Informationen der globalen Datei hinzu (fichier.txt)
    with open('fichier.txt', 'a') as f:
        f.write(informationen + '\n')

    if not os.path.exists("Contact"):
        os.makedirs("Contact")
    
    # Erstelle eine individuelle Datei für jeden Kontakt
    with open(f"Contact/{name}.txt", 'w') as f:
        f.write(f"Name : {name}\nNummer : {nummer}\n")
        for kategorie, wert in kategorien.items():
            f.write(f"{kategorie} : {wert}\n")  # Speichere alle Kategorien in der individuellen Datei
    
    print(f"{name} wurde mit den folgenden Informationen zum Verzeichnis hinzugefügt: {informationen}")
    time.sleep(3)
    menu()

def wahl3():
    name = input("Geben Sie den Namen der zu bearbeitenden Person ein: ")
    with open('fichier.txt', 'r') as f:
        zeilen = f.readlines()
    
    for i, zeile in enumerate(zeilen):
        if zeile.startswith(name + ' '):
            print(f"Aktuelle Informationen : {zeile.strip()}")
            
            # Bearbeite die grundlegenden Informationen
            neuer_name = input("Geben Sie den neuen Namen ein (oder drücken Sie Enter, um den alten beizubehalten): ") or name
            neue_nummer = input("Geben Sie die neue Nummer ein (oder drücken Sie Enter, um die alte zu behalten): ") or zeile.split(' ')[1]
            
            # Bestehende Kategorien verwalten
            bestehende_kategorien = {c.split(" : ")[0]: c.split(" : ")[1] for c in zeile.strip().split(" | ")[2:] if " : " in c}
            
            while True:
                aktion = input("Möchten Sie eine bestehende Kategorie ändern (1), eine neue Kategorie hinzufügen (2) oder beenden (3)? : ")
                if aktion == '1':
                    kategorie_aendern = input("Geben Sie den Namen der zu ändernden Kategorie ein: ")
                    if kategorie_aendern in bestehende_kategorien:
                        neue_werte = input(f"Geben Sie den neuen Wert für {kategorie_aendern} ein: ")
                        bestehende_kategorien[kategorie_aendern] = neue_werte
                    else:
                        print("Diese Kategorie existiert nicht.")
                elif aktion == '2':
                    neue_kategorie = input("Geben Sie den Namen der neuen Kategorie ein: ")
                    neuer_wert = input(f"Geben Sie den Wert für {neue_kategorie} ein: ")
                    bestehende_kategorien[neue_kategorie] = neuer_wert
                elif aktion == '3':
                    break
                else:
                    print("Ungültige Option.")
            
            # Neue Informationen zusammenstellen
            neue_infos = f"{neuer_name} {neue_nummer}"
            for kategorie, wert in bestehende_kategorien.items():
                neue_infos += f" | {kategorie} : {wert}"
            
            # Die globale Datei aktualisieren
            zeilen[i] = neue_infos + '\n'
            with open('fichier.txt', 'w') as f:
                f.writelines(zeilen)
            
            # Die individuelle Datei im Ordner "Contact" aktualisieren
            ordner_contact = "Contact"
            os.makedirs(ordner_contact, exist_ok=True)
            datei_pfad = os.path.join(ordner_contact, f"{neuer_name}.txt")
            
            with open(datei_pfad, 'w') as f:
                f.write(f"Name : {neuer_name}\nNummer : {neue_nummer}\n")
                for kategorie, wert in bestehende_kategorien.items():
                    f.write(f"{kategorie} : {wert}\n")
            
            print(f"Die Informationen von {name} wurden aktualisiert.")
            time.sleep(3)
            menu()
    
    print(f"{name} ist nicht im Verzeichnis registriert!")
    time.sleep(1)
    print("Zurück zum Menü!")
    menu()

def wahl0():
    print("Danke, dass Sie das Verzeichnis verwendet haben. Bis bald!")
    time.sleep(1)
    exit()

def menu():
    wahl = int(input(f""" 
                {g}
                 ██▓     ██▓ ███▄    █  ██ ▄█▀ ██░ ██  █    ██  ▄▄▄▄   
                ▓██▒    ▓██▒ ██ ▀█   █  ██▄█▒ ▓██░ ██▒ ██  ▓██▒▓█████▄ 
                ▒██░    ▒██▒▓██  ▀█ ██▒▓███▄░ ▒██▀▀██░▓██  ▒██░▒██▒ ▄██
                ▒██░    ░██░▓██▒  ▐▌██▒▓██ █▄ ░▓█ ░██ ▓▓█  ░██░▒██░█▀  
                ░██████▒░██░▒██░   ▓██░▒██▒ █▄░▓█▒░██▓▒▒█████▓ ░▓█  ▀█▓
                ░ ▒░▓  ░░▓  ░ ▒░   ▒ ▒ ▒ ▒▒ ▓▒ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░▒▓███▀▒
                 ░ ▒  ░ ▒ ░░ ░░   ░ ▒░░ ░▒ ▒░ ▒ ░▒░ ░░░▒░ ░ ░ ▒░▒   ░ 
                  ░ ░    ▒ ░   ░   ░ ░ ░ ░░ ░  ░  ░░ ░ ░░░ ░ ░  ░    ░ 
                    ░  ░ ░           ░ ░  ░    ░  ░  ░   ░      ░      
                                                     ░ 
{g}------------------------------------------------------------------------------------------------------------------------\n{w}https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.com/exi7 {b}|{w} https://github.c\n{g}------------------------------------------------------------------------------------------------------------------------\n{w}
 {g}┌                                                                                              
 ├           ┌─────────────────┐       
 └─┬─────────┤   {w}Verzeichnis{g}    ├
   │         └─────────────────┘         
   ├─ [{w}1{g}] Name von jemandem registrieren.
   ├─ [{w}2{g}] Informationen von jemandem ansehen.
   ├─ [{w}3{g}] Informationen von jemandem bearbeiten.
   └─ [{w}0{g}] Programm beenden.               
                  

    Geben Sie Ihre Wahl ein: """))

    if wahl == 0:  
        wahl0()
    elif wahl == 1:
        wahl1()
    elif wahl == 2:
        wahl2()
    elif wahl == 3:
        wahl3()
    else:
        print("Ungültige Option. Bitte wählen Sie eine gültige Option.")
        
menu()
