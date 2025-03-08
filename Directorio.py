import time
import os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore

y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
g = Fore.LIGHTGREEN_EX

def opcion2():
    with open('archivo.txt', 'r') as f:
        lineas = f.readlines()

    if lineas:
        print("Aquí está la lista de personas registradas:")
        for i, linea in enumerate(lineas, 1):
            nombre = linea.split(' ')[0]
            print(f"{i}. {nombre}")
    else:
        print("El directorio está vacío.")
        time.sleep(3)
        menu()
        return

    busqueda = input("\n¿Quieres buscar por nombre (1) o por número (2)? : ")
    
    if busqueda == '1':  
        nombre = input("¿A quién buscas? : ")
        contactos_encontrados = []
        
        for linea in lineas:
            if linea.startswith(nombre + ' '):
                contactos_encontrados.append(linea.strip())
        
        if contactos_encontrados:
            print(f"Contactos encontrados para {nombre} :\n")
            for contacto in contactos_encontrados:
                print(contacto)
                
            archivo_contacto = f"Contacto/{nombre}.txt"
            if os.path.exists(archivo_contacto):
                print("\nDetalles del contacto:")
                with open(archivo_contacto, 'r') as f:
                    print(f.read())
        else:
            print(f"{nombre} no está registrado en tu directorio!")
        time.sleep(3)
        menu()
    
    elif busqueda == '2':  
        numero = input("¿Qué número buscas? : ")
        contactos_encontrados = []
        
        for linea in lineas:
            if numero in linea:
                contactos_encontrados.append(linea.strip())
        
        if contactos_encontrados:
            print(f"Contactos encontrados para el número {numero} :\n")
            for contacto in contactos_encontrados:
                print(contacto)
        else:
            print(f"{numero} no está registrado en tu directorio!")
        
        time.sleep(3)
        menu()
        
    else:
        print("Opción inválida. Por favor, elige 1 o 2.")
    menu()


def opcion1():
    nombre = input('Introduce un nombre: ')
    numero = input('Introduce el número asociado a este nombre: ')
    
    informacion = f"{nombre} {numero}"
    categorias = {}
    
    while True:
        categoria = input("Introduce una categoría adicional (ej: Dirección, Email, Profesión, Discord) o presiona Enter para terminar: ")
        if not categoria.strip():
            break
        valor = input(f"Introduce el valor para {categoria}: ")
        categorias[categoria] = valor
        informacion += f" | {categoria} : {valor}"
    
    with open('archivo.txt', 'a') as f:
        f.write(informacion + '\n')

    if not os.path.exists("Contacto"):
        os.makedirs("Contacto")
    
    with open(f"Contacto/{nombre}.txt", 'w') as f:
        f.write(f"Nombre: {nombre}\nNúmero: {numero}\n")
        for categoria, valor in categorias.items():
            f.write(f"{categoria} : {valor}\n")
    
    print(f"{nombre} ha sido añadido al directorio con la siguiente información: {informacion}")
    time.sleep(3)
    menu()


def opcion3():
    nombre = input("Introduce el nombre de la persona a modificar: ")
    with open('archivo.txt', 'r') as f:
        lineas = f.readlines()
    
    for i, linea in enumerate(lineas):
        if linea.startswith(nombre + ' '):
            print(f"Información actual: {linea.strip()}")
            
            nuevo_nombre = input("Introduce el nuevo nombre (o presiona Enter para mantener el anterior): ") or nombre
            nuevo_numero = input("Introduce el nuevo número (o presiona Enter para mantener el anterior): ") or linea.split(' ')[1]
            
            categorias_existentes = {c.split(" : ")[0]: c.split(" : ")[1] for c in linea.strip().split(" | ")[2:] if " : " in c}
            
            while True:
                accion = input("¿Quieres modificar una categoría existente (1), añadir una nueva categoría (2), o terminar (3)? : ")
                if accion == '1':
                    categoria_a_modificar = input("Introduce el nombre de la categoría a modificar: ")
                    if categoria_a_modificar in categorias_existentes:
                        nueva_valor = input(f"Introduce el nuevo valor para {categoria_a_modificar}: ")
                        categorias_existentes[categoria_a_modificar] = nueva_valor
                    else:
                        print("Esta categoría no existe.")
                elif accion == '2':
                    nueva_categoria = input("Introduce el nombre de la nueva categoría: ")
                    nueva_valor = input(f"Introduce el valor para {nueva_categoria}: ")
                    categorias_existentes[nueva_categoria] = nueva_valor
                elif accion == '3':
                    break
                else:
                    print("Opción inválida.")
            
            nuevas_infos = f"{nuevo_nombre} {nuevo_numero}"
            for categoria, valor in categorias_existentes.items():
                nuevas_infos += f" | {categoria} : {valor}"
            
            lineas[i] = nuevas_infos + '\n'
            with open('archivo.txt', 'w') as f:
                f.writelines(lineas)
            
            if not os.path.exists("Contacto"):
                os.makedirs("Contacto")
            
            with open(f"Contacto/{nuevo_nombre}.txt", 'w') as f:
                f.write(f"Nombre: {nuevo_nombre}\nNúmero: {nuevo_numero}\n")
                for categoria, valor in categorias_existentes.items():
                    f.write(f"{categoria} : {valor}\n")
            
            print(f"La información de {nombre} ha sido actualizada.")
            time.sleep(3)
            menu()
    
    print(f"{nombre} no está registrado en el directorio!")
    time.sleep(1)
    menu()
    

def menu():
    opcion = int(input(f""" 
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
 └─┬─────────┤   {w}Directorio{g}    ├
   │         └─────────────────┘         
   ├─ [{w}1{g}] Registrar un contacto
   ├─ [{w}2{g}] Ver información de un contacto
   ├─ [{w}3{g}] Modificar un contacto
   └─ [{w}0{g}] Salir            
                  

    Elige una opcion: """))

    if opcion == 0:
        exit()
    elif opcion == 1:
        opcion1()
    elif opcion == 2:
        opcion2()
    elif opcion == 3:
        opcion3()
    else:
        print("Opción inválida.")
        menu()

menu()

