#region import
import tkinter as tk #importa p abrir o explorer
from tkinter import filedialog #importa p abrir o explorer
import sys
import os
import re
import unicodedata

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
    texto = data.read().upper() # Solicitando o texto a ser encriptado ou decriptado:

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

chave = input('Entre com a chave (Caracteres): ') # Chave a ser utilizada
if chave.isalpha():
    chave = chave
else:
    print("Digite uma chave válida! Apenas caracteres, caracteres especiais não são permitidos!\n")
    chave = input("Entre com a chave: ")
modo = input('Escolha C para cifrar ou D para decifrar o texto: ') # Determinar modo de operação (E = encriptar; D = decriptar)
texto = texto.upper() # Converter todo o texto em maiúsculas:
modo = modo.upper() # Converter todo o modo em maiúsculas:   #TUDO EM MINUSCULO CONVERTE DPS
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

texto  = ''.join(ch for ch in unicodedata.normalize('NFKD', texto)     #retirar acentuação
    if not unicodedata.combining(ch))
texto = re.sub("[,/!.:;? ']", "" ,  texto)



#endregion



#region funções 
   
def encrypt(texto, chave):
    convertido = ''
    for i in range(len(texto)):
        texto_letra_index = alfabeto.index(texto[i])
        chave_letra_index = alfabeto.index(chave[((i) % len(chave))].upper())
        index = (texto_letra_index + chave_letra_index + 1) % len(alfabeto) 
        convertido += alfabeto[index]
    if (ext == 1):
        data_1 = open(path, 'w')
        data_1.close()
        data_1 = open(path, 'w')
        data_1.write(convertido)
        data_1.close()
        return(convertido)
    else:  
        return convertido


def decrypt(texto, chave):
    convertido = ''
    for i in range(len(texto)):
        texto_letra_index = alfabeto.index(texto[i])
        chave_letra_index = alfabeto.index(chave[((i) % len(chave))].upper())
        index = (texto_letra_index - chave_letra_index - 1) % len(alfabeto) 
        convertido += alfabeto[index]
    if (ext == 1):
        data_1 = open(path, 'w')
        data_1.close()
        data_1 = open(path, 'w')
        data_1.write(convertido)
        data_1.close()
        return(convertido)
    else:  
        return convertido

#endregion

#region output
if modo == 'C':
    print (encrypt(texto, chave))
elif modo == 'D':
    print (decrypt (texto,chave ))
else:
    print ('Não conheço esse comando')
#endregion