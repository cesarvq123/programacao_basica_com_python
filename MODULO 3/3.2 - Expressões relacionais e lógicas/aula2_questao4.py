print("Classes possíveis: guerreiro, mago, arqueiro.")
print("Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.")
print("Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.")
print("Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.")

classe = input("Digite qual será a sua classe (guerreiro, mago, arqueiro): ")

pontos_de_forca = int(input("Digite os pontos de força (de 1 a 20): "))
pontos_de_magia = int(input("Digite os pontos de magia (de 1 a 20): "))

atributos_validos = False

atributos_validos = (
    (classe == "guerreiro" and pontos_de_forca >= 15 and pontos_de_magia <= 10) or
    (classe == "mago" and pontos_de_forca <= 10 and pontos_de_magia >= 15) or
    (classe == "arqueiro" and pontos_de_forca > 5 and pontos_de_forca <= 15 and pontos_de_magia > 5 and pontos_de_magia <= 15)
)

print(f"Pontos de atributo consistentes com a classe escolhida: {atributos_validos}")

