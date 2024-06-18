def calcular_digitos_verificadores(cpf):
    cpf_numerico = [int(digito) for digito in cpf if digito.isdigit()]
    soma = sum((cpf_numerico[i] * (10 - i)) for i in range(9))
    resto = soma % 11

    if resto < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - resto

    cpf_com_primeiro_digito = cpf_numerico + [primeiro_digito]
    soma = sum((cpf_com_primeiro_digito[i] * (11 - i)) for i in range(10))
    resto = soma % 11

    if resto < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - resto
    return primeiro_digito, segundo_digito

def validar_cpf(cpf):
    if len(cpf) != 14:
        return False
    primeiro_digito_esperado, segundo_digito_esperado = calcular_digitos_verificadores(cpf)

    return int(cpf[12]) == primeiro_digito_esperado and int(cpf[13]) == segundo_digito_esperado

cpf_usuario = input("Digite o CPF na forma XXX.XXX.XXX-XX: ")

if validar_cpf(cpf_usuario):
    print("CPF válido")
else:
    print("CPF inválido")
