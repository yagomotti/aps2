'''
Parte A - Criptografia RSA
'''

#region import
import tkinter as tk #importa p abrir o explorer
from tkinter import filedialog #importa p abrir o explorer
import sys
import os
import re
import unicodedata
import random


root =tk.Tk() #faz sobrepor o explorer
root.withdraw()


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv) #Para reiniciar o programa caso a informação fornecida seja inválida
#endregion



'''
Algoritmo para determinar o maior divisor comum
Use a iteração para torná-lo mais rápido para números inteiros maiores
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#region calc
'''
O algoritmo estendido para encontrar o inverso multiplicativo de dois números
'''
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi //e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi
#endregion
'''
Teste para ver se um número é primo.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range (3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def is_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Ambos os números devem ser primos.')
    elif p == q:
        raise ValueError('p e q não pode ser igual')
    #n = pq
    n = p * q

    #Phi é o totient de n
    phi = (p-1) * (q-1)

    #Escolha um número inteiro e tal que e e phi (n) sejam compostos
    e = random.randrange(1, phi)

    #algoritmo para verificar se e e phi (n) são compostos
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #algoritmo estendido para gerar a chave privada
    d = multiplicative_inverse(e, phi)
    
    #Retornar par de chaves público e privado
    #A chave pública é (e, n) e a chave privada é (d, n)
    return ((e, n), (d, n))

def is_encrypt(pk, plaintext):
    #Desembale a chave nos componentes
    key, n = pk
    #Converta cada letra no texto sem formatação em números com base no caractere usando a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    #Retornar a matriz de bytes
    return cipher

def is_decrypt(pk, ciphertext):
    #Desembalar a chave em seus componentes
    key, n = pk
    # Gere o texto sem formatação com base no texto cifrado e na chave usando a ^ b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Retornar a matriz de bytes como uma sequência
    return ''.join(plain)

if __name__ == '__main__':
    '''
    Detectar se o script está sendo executado diretamente pelo usuário
    '''
    print ("Criptografador / decodificador de RSA")
    p = int(input("Digite um número primo (17, 19, 23 etc.): "))
    q = int(input("Digite outro número primo (não o que você digitou acima): "))
    print ("Gerando seus pares de chaves públicos / privados agora...")
    public, private = is_keypair(p, q)
    print ("Sua chave pública é", public ,"e sua chave privada é", private)
    print("Escolha como deseja inserir a frase a ser encriptada: \n"
    "1 - Importar arquivo de dados\n"
    "2 - Digitar a frase a ser encriptada\n\n")
    ext = int(input("Escolha:"))
    if ext == 1:
        path = filedialog.askopenfilename() #abre o explorer para selecionar o arquivo
        data = open(path, 'r+')
        message = data.read().upper() # Solicitando o texto a ser encriptado ou decriptado
        message  = ''.join(ch for ch in unicodedata.normalize('NFKD', message)     #retirar acentuação
            if not unicodedata.combining(ch))
        
    elif ext == 2:
        message = input("Digite a frase a ser encriptada ou decriptada: ")
        message  = ''.join(ch for ch in unicodedata.normalize('NFKD', message)     #retirar acentuação
            if not unicodedata.combining(ch))
    else:
        print("Comando não reconhecido.")
        print("Deseja tentar novamente?\n")
        restart = int(input("1 - Sim     2 - Não\n"))
        if restart == 1:
            restart_program()
        else:
            print("O programa será fechado!")
            sys.exit()


    message = re.sub("[,/!.:;? ']", "" ,  message)
    encrypted_msg = is_encrypt(private, message)
    print ("Sua mensagem criptografada é: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Descriptografando mensagem com chave pública ", public ," . . .")
    print ("Sua mensagem é: ")
    print (is_decrypt(public, encrypted_msg))

