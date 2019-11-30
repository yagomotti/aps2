#region import
import tkinter as tk #importa p abrir o explorer
from tkinter import filedialog #importa p abrir o explorer
import sys
import os


root =tk.Tk() #faz sobrepor o explorer
root.withdraw()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) #Para reiniciar o programa caso a informação fornecida seja inválida
#endregion

#region inputs
print("Escolha como deseja inserir a frase a ser encriptada: \n"
"1 - Importar arquivo de dados\n"
"2 - Digitar a frase a ser encriptada\n\n")
ext = int(input("Escolha:"))
if ext==1:
    path = filedialog.askopenfilename() #abre o explorer para selecionar o arquivo
    data = open(path, 'r+')
    texto = data.read() # Solicitando o texto a ser encriptado ou decriptado:
elif ext==2:
    texto = input("Digite a frase a ser encriptada ou decriptada: ")


else:
        print("Comando não reconhecido.")
        print("Deseja tentar novamente?\n")
        restart = int(input("1 - Sim     2 - Não\n"))
        if restart == 1:
            restart_program()
        else:
            print("O programa será fechado!")
            sys.exit() 

chave = int(input('Entre com o valor da chave (deslocamento): ')) # Chave a ser utilizada
modo = input('Escolha C para cifrar ou D para decifrar o texto: ') # Determinar modo de operação (E = encriptar; D = decriptar)
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Conjunto de caracteres válidos no algoritmo
texto = texto.upper() # Converter todo o texto em maiúsculas:
modo = modo.upper() # Converter todo o modo em maiúsculas:

#endregion

#region funções
def encrypt(message):
    m =''
    for c in message:
        if c in alfabeto:
            c_index=alfabeto.index(c)
            m += alfabeto[(c_index + chave) % len(alfabeto)]
        else:
            m += c
    if (ext == 1):
        data_2 = open(path, 'w')
        data_2.close()
        data_2 = open(path, 'w')
        data_2.write(m)
        data_2.close()
        return m
    else:  
        return m

def decrypt(message):
    m =''
    for c in message:
        if c in alfabeto:
            c_index=alfabeto.index(c)
            m += alfabeto[(c_index - chave) % len(alfabeto)]
        else:
            m += c
    if (ext == 1):
        data_2 = open(path, 'w')
        data_2.close()
        data_2 = open(path, 'w')
        data_2.write(m)
        data_2.close()
        return m
    else:  
        return m
#endregion

#region output
if modo == 'C':
    print (encrypt(texto))
elif modo == 'D':
    print (decrypt (texto))
else:
    print ('Não conheço esse comando')
#endregion