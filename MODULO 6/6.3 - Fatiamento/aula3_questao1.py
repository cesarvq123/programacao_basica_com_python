def solicitar_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número inteiro para montar sua lista de números (ou digite 0 para parar): "))
            if num == 0:
                if len(numeros) < 4:
                    print("Por favor, forneça pelo menos 4 números inteiros.")
                else:
                    break
            else:
                numeros.append(num)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    return numeros

numeros = solicitar_numeros()

print("Lista original:", numeros)
print("Os 3 primeiros elementos:", numeros[:3])
print("Os 2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Os elementos de índice par:", numeros[::2])
print("Os elementos de índice ímpar:", numeros[1::2])