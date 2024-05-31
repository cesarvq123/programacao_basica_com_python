n = int(input("Digite quantos números serão analisados: "))
maior = 0
while n > 0:
    x = int(input("Digite informe o número: "))
    if x > maior:
        maior = x
    n -= 1
print (maior)