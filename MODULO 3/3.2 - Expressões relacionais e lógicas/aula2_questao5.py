genero = input("Qual o seu gênero? (responda com M ou F): ")

idade = int(input("Informe sua idade: "))
tempo_servico = int(input("Informe o seu temo de serviço em anos: "))

a = (genero == "f" and idade >= 60) or (genero == "m" and idade >=65)
b = (tempo_servico >= 30)
c = (idade >= 60 and tempo_servico >= 25)

print (f"Você pode ser aposentar? {a or b or c}")