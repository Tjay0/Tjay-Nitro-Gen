from os import name, chdir, rmdir, mkdir, rename, listdir
from os.path import isdir
from pystyle import Anime, Colorate, Colors, Center, System, Write
from random import choice, shuffle, randint
from binascii import hexlify
from shutil import rmtree
from colorama import Fore, init
from os import system as cmd
from time import sleep
import ctypes
import random
import string
import platform

try:
    import colorama
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

banner1 = """

▀█▀ ░░█ ▄▀█ █▄█
░█░ █▄█ █▀█ ░█░

█▄░█ █ ▀█▀ █▀█ █▀█   █▀▀ █▀▀ █▄░█
█░▀█ █ ░█░ █▀▄ █▄█   █▄█ ██▄ █░▀█`"""[1:].replace('M', '0')


banner2 = """                           

▀█▀ ░░█ ▄▀█ █▄█
░█░ █▄█ █▀█ ░█░

█▄░█ █ ▀█▀ █▀█ █▀█   █▀▀ █▀▀ █▄░█
█░▀█ █ ░█░ █▀▄ █▄█   █▄█ ██▄ █░▀█             Pulse ENTER para abrir el generador"""[1:].replace('m','0')


banner = choice((banner1, banner2))

# __import__('pyperclip').copy('\n'.join(l.rstrip() for l in banner.splitlines()))

ascii = '''


▀▀█▀▀ ──▀ █▀▀█ █──█ 　 ░█▀▀▄ █▀▀ 
─░█── ──█ █▄▄█ █▄▄█ 　 ░█─░█ █── 
─░█── █▄█ ▀──▀ ▄▄▄█ 　 ░█▄▄▀ ▀▀▀'''[1:]


def init():
    System.Clear()
    System.Title("Tjay | Nitro Generator | Pulse la tecla ENTER para abrir el generador")
    System.Size(100, 40)
    Anime.Fade(text=Center.Center(banner2), color=Colors.blue_to_black, mode=Colorate.Diagonal, enter=True)

ctypes.windll.kernel32.SetConsoleTitleW(
    "Discord Nitro Generator | Tjay | v1.0 | Presiona ENTER para abrir el generador")

nitros = open("nitros-tjay.txt", "a")

def main():
    System.Clear()
    print('\n'*2)
    print(Colorate.Horizontal(Colors.blue_to_black, Center.XCenter(ascii)))
    print('\n'*3)
    print(f"{Fore.WHITE}[ {Fore.CYAN}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator Creado Por {Fore.WHITE}tjay{Fore.LIGHTBLACK_EX} | {Fore.WHITE}No me hago responsable del uso de esta herramienta{Fore.RESET}\n{Fore.WHITE}[ {Fore.CYAN}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Me puedes seguir en GitHub: {Fore.WHITE}https://github.com/Tjay0{Fore.RESET}")
    try:
        try:
            nitroAmount = int(input(
                f"\n{Fore.WHITE}[ {Fore.BLUE}@root:~$ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Cuantos codigos desea generar: {Fore.WHITE}"))
        except ValueError:
            print(
                f"{Fore.WHITE}[ {Fore.BLUE}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}La cantidad debe ser {Fore.WHITE}un numero")
            sleep(2)
            return main()

        nitroType = input(f"{Fore.WHITE}[ {Fore.BLUE}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Que tipo de nitro desea generar? {Fore.WHITE}classic {Fore.LIGHTBLACK_EX}o {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}? (El Nitro Classic contiene 16 charácteres de palabras y el Nitro Boost contiene 24): {Fore.WHITE}")

        if nitroType == "boost" or nitroType == "classic":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.BLUE}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}La respuesta debe ser {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}o {Fore.WHITE}classic{Fore.RESET}")
            sleep(2)
            return main()

        nitroLink = input(
            f"{Fore.WHITE}[ {Fore.BLUE}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Quieres {Fore.WHITE}https://discord.com/gifts/ {Fore.LIGHTBLACK_EX}detras de los codigos ? ({Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no): {Fore.WHITE}")

        if nitroLink == "yes" or nitroLink == "no":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.BLUE}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Debes responder {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no{Fore.RESET}")
            sleep(2)
            return main()
    except KeyboardInterrupt:
        clear_console()
        exit()

    gen(nitroAmount, nitroType, nitroLink)


def gen(nitroAmount, nitroType, nitroLink):

    amount = 0

    with open("nitros-Tjay.txt", "w") as file:
        file.write("")

    for _ in range(nitroAmount):
        genCode = "".join(random.choice(string.digits+string.ascii_letters)
                          for _ in range(24)) if nitroType == "boost" else "".join(random.choice(string.digits+string.ascii_letters)
                                                                                   for _ in range(16))
        nitro = f"https://discord.com/gifts/{genCode}" if nitroLink == "yes" else genCode

        try:
            print(
                f"{Fore.WHITE}[ {Fore.BLUE}- {Fore.WHITE}] {Fore.RESET}{nitro}")
            nitros.write(
                f"{nitro}\n")
            amount += 1
        except:
            break

    nitros.close()
    input(
        f"\n{Fore.WHITE}[ {Fore.BLUE}> {Fore.WHITE}] {amount} nitros fueron generados con exito. Se guardaron en el documento (nitros-tjay). (Presiona una TECLA para volver al GENERADOR)")


def clear_console():
    if platform.system() == "Windows":
        cmd("cls")
    else:
        cmd("clear")





if __name__ == '__main__':
    init()
    while True:
        main()
