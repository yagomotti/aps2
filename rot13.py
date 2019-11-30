def rot13(s):
    result = ""

    # Loop dos caracteres
    for v in s:
        # Converte pra número
        c = ord(v)

        # Altera o número pra frente ou pra trás
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        # Append no resultado
        result += chr(c)

    # Retorna o resultado
    return result


def ask(mii):
    num=int(input("Deseja Criptografar uma frase ou Decriptografar em ROT13? \n 1-Criptografar \n 2-Decriptografar\n"))
    if num == 1:
        frase=str(input("Digite uma frase para ser Criptografada:\n "))
        print("Frase Criptografada: ",rot13(frase))
        ask(2)
    elif num == 2:
        frase2=str(input("Digite uma frase para ser Decriptografar:\n "))
        print("Frase Descriptografada: ",rot13(frase2))
        ask(2)
    else: 
        print("numero inválido")
        ask(2)
ask(2)