import time
import os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
g = Fore.LIGHTGREEN_EX

def choix2():
    # Charger tous les contacts du fichier
    with open('fichier.txt', 'r') as f:
        lignes = f.readlines()

    # Afficher la liste des noms des contacts enregistrés
    if lignes:
        print("Voici la liste des personnes enregistrées :")
        for i, ligne in enumerate(lignes, 1):
            nom = ligne.split(' ')[0]  # Récupérer juste le nom de la personne
            print(f"{i}. {nom}")  # Afficher seulement le nom
    else:
        print("Le répertoire est vide.")
        time.sleep(3)
        menu()
        return

    # Demander la recherche (par nom ou par numéro)
    recherche = input("\nVoulez-vous rechercher par nom (1) ou par numéro (2) ? : ")
    
    if recherche == '1':  
        nom = input("Qui recherchez-vous ? : ")
        contacts_trouves = []
        
        # Recherche des contacts par nom
        for ligne in lignes:
            if ligne.startswith(nom + ' '):
                contacts_trouves.append(ligne.strip())  # Ajouter l'information complète du contact
        
        if contacts_trouves:
            print(f"Contacts trouvés pour {nom} :\n")
            for contact in contacts_trouves:
                print(contact)
                
            fichier_contact = f"Contact/{nom}.txt"
            if os.path.exists(fichier_contact):
                print("\nDétails du contact :")
                with open(fichier_contact, 'r') as f:
                    print(f.read())
        else:
            print(f"{nom} n'est pas enregistré dans votre répertoire !")
        time.sleep(3)
        menu()
    
    elif recherche == '2':  
        numero = input("Quel numéro recherchez-vous ? : ")
        contacts_trouves = []
        
        # Recherche des contacts par numéro
        for ligne in lignes:
            if numero in ligne:
                contacts_trouves.append(ligne.strip())  # Ajouter l'information complète du contact
        
        if contacts_trouves:
            print(f"Contacts trouvés pour le numéro {numero} :\n")
            for contact in contacts_trouves:
                print(contact)  # Afficher toutes les informations du contact
        else:
            print(f"{numero} n'est pas enregistré dans votre répertoire !")
        
        time.sleep(3)
        menu()
        
    else:
        print("Option invalide. Veuillez choisir 1 ou 2.")
    menu()




def choix1():
    nom = input('Entrez un nom : ')
    numero = input('Entrez le numéro associé à ce nom : ')
    
    informations = f"{nom} {numero}"  # Informations de base
    categories = {}
    
    # Ajout de catégories supplémentaires
    while True:
        categorie = input("Entrez une catégorie supplémentaire (ex : Adresse, Email, Profession, Discord) ou appuyez sur Entrée pour terminer : ")
        if not categorie.strip():  # Si l'entrée est vide, on arrête
            break
        valeur = input(f"Entrez la valeur pour {categorie} : ")
        categories[categorie] = valeur  # Ajoute la catégorie et sa valeur
        informations += f" | {categorie} : {valeur}"  # Ajoute au texte à sauvegarder
    
    # Ajouter au fichier global (fichier.txt)
    with open('fichier.txt', 'a') as f:
        f.write(informations + '\n')

    if not os.path.exists("Contact"):
        os.makedirs("Contact")
    
    # Créer un fichier individuel pour chaque contact
    with open(f"Contact/{nom}.txt", 'w') as f:
        f.write(f"Nom : {nom}\nNuméro : {numero}\n")
        for categorie, valeur in categories.items():
            f.write(f"{categorie} : {valeur}\n")  # Sauvegarde toutes les catégories dans le fichier individuel
    
    print(f"{nom} a été ajouté au répertoire avec les informations suivantes : {informations}")
    time.sleep(3)
    menu()


def choix3():
    nom = input("Entrez le nom de la personne à modifier : ")
    with open('fichier.txt', 'r') as f:
        lignes = f.readlines()
    
    for i, ligne in enumerate(lignes):
        if ligne.startswith(nom + ' '):
            print(f"Informations actuelles : {ligne.strip()}")
            
            # Modifier les informations de base
            nouveau_nom = input("Entrez le nouveau nom (ou appuyez sur Entrée pour conserver l'ancien) : ") or nom
            nouveau_numero = input("Entrez le nouveau numéro (ou appuyez sur Entrée pour conserver l'ancien) : ") or ligne.split(' ')[1]
            
            # Gérer les catégories existantes
            categories_existantes = {c.split(" : ")[0]: c.split(" : ")[1] for c in ligne.strip().split(" | ")[2:] if " : " in c}
            
            while True:
                action = input("Voulez-vous modifier une catégorie existante (1), ajouter une nouvelle catégorie (2), ou terminer (3) ? : ")
                if action == '1':
                    categorie_a_modifier = input("Entrez le nom de la catégorie à modifier : ")
                    if categorie_a_modifier in categories_existantes:
                        nouvelle_valeur = input(f"Entrez la nouvelle valeur pour {categorie_a_modifier} : ")
                        categories_existantes[categorie_a_modifier] = nouvelle_valeur
                    else:
                        print("Cette catégorie n'existe pas.")
                elif action == '2':
                    nouvelle_categorie = input("Entrez le nom de la nouvelle catégorie : ")
                    nouvelle_valeur = input(f"Entrez la valeur pour {nouvelle_categorie} : ")
                    categories_existantes[nouvelle_categorie] = nouvelle_valeur
                elif action == '3':
                    break
                else:
                    print("Option invalide.")
            
            # Construire les nouvelles informations
            nouvelles_infos = f"{nouveau_nom} {nouveau_numero}"
            for categorie, valeur in categories_existantes.items():
                nouvelles_infos += f" | {categorie} : {valeur}"
            
            # Mettre à jour le fichier global
            lignes[i] = nouvelles_infos + '\n'
            with open('fichier.txt', 'w') as f:
                f.writelines(lignes)
            
            # Mettre à jour le fichier individuel dans "Contact"
            dossier_contact = "Contact"
            os.makedirs(dossier_contact, exist_ok=True)
            chemin_fichier = os.path.join(dossier_contact, f"{nouveau_nom}.txt")
            
            with open(chemin_fichier, 'w') as f:
                f.write(f"Nom : {nouveau_nom}\nNuméro : {nouveau_numero}\n")
                for categorie, valeur in categories_existantes.items():
                    f.write(f"{categorie} : {valeur}\n")
            
            print(f"Les informations de {nom} ont été mises à jour.")
            time.sleep(3)
            menu()
    
    print(f"{nom} n'est pas enregistré dans le répertoire !")
    time.sleep(1)
    print("Retour au menu !")
    menu()



def choix0():
    print("Merci d'avoir utilisé le répertoire. À bientôt !")
    time.sleep(1)
    exit()


def menu():
    choix = int(input(f""" 
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
 └─┬─────────┤   {w}Répertoire{g}    ├
   │         └─────────────────┘         
   ├─ [{w}1{g}] Enregistres le nom de quelqu'un.
   ├─ [{w}2{g}] Regardes les informations de quelqu'un.
   ├─ [{w}3{g}] Modifies les informations de quelqu'un 
   └─ [{w}0{g}] Quittes le programme.               
                  

    Entrez votre choix : """))

    if choix == 0:  
        choix0()
    elif choix == 1:
        choix1()
    elif choix == 2:
        choix2()
    elif choix == 3:
        choix3()
    else:
        print("Option invalide. Veuillez sélectionner une option valide.")
        
menu()