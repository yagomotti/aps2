#region import

import tkinter as tk #importa p abrir o explorer
from tkinter import filedialog #importa p abrir o explorer
import sys
import os
import random
import unicodedata



root =tk.Tk() #faz sobrepor o explorer
root.withdraw()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) #Para reiniciar o programa caso a informação fornecida seja inválida

#endregion

def cripto(cifra):
    if cifra==1:
        import cesar
    elif cifra==2:
        import vigenere
    elif cifra==3:
        import rsa
    elif cifra==4:
        import rot13
    else:
        print("A cifra inserida não foi encontrada.")
        print("Deseja tentar novamente?\n"
        "Digite 1 para reiniciar o programa ou 2 para fechar o programa")
        reset = int(input("Escolha: "))
        if reset == 1:    
            restart_program()
        elif reset == 2:
            print("O programa será fechado!")
            sys.exit()
        else:
            print("Comando não reconhecido, fechando o programa!")
        


print("Digite qual cifra será utilizada \n\n"
"1 - Cifra de César\n"
"2 - Cifra de Vigenére\n"
"3 - Cifra de RSA\n"
"4 - Cifra de Rot 13")

x=int(input("Escolha: "))
cripto(x)