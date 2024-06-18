def mes_por_extenso(mes):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril",
        "Maio", "Junho", "Julho", "Agosto",
        "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    return meses[mes - 1]

data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")

dia, mes, ano = map(int, data_nascimento.split('/'))

mes_extenso = mes_por_extenso(mes)

print("Você nasceu em", dia, "de", mes_extenso, "de", ano)
