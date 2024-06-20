import csv


def criar_usuario(id, nome, senha, permissao):
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nome, senha, permissao])

def ler_usuarios():
    usuarios = []
    with open('usuarios.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            usuarios.append({
                'id': row[0],
                'nome': row[1],
                'senha': row[2],
                'permissao': row[3]
            })
    return usuarios

def atualizar_usuario(id, nome=None, senha=None, permissao=None):
    usuarios = ler_usuarios()
    for usuario in usuarios:
        if usuario['id'] == id:
            if nome:
                usuario['nome'] = nome
            if senha:
                usuario['senha'] = senha
            if permissao:
                usuario['permissao'] = permissao
            break
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios:
            writer.writerow([usuario['id'], usuario['nome'], usuario['senha'], usuario['permissao']])

def deletar_usuario(id):
    usuarios = ler_usuarios()
    usuarios = [usuario for usuario in usuarios if usuario['id'] != id]
    with open('usuarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios:
            writer.writerow([usuario['id'], usuario['nome'], usuario['senha'], usuario['permissao']])


def criar_produto(id, nome, preco, quantidade):
    with open('produtos.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nome, preco, quantidade])

def ler_produtos():
    produtos = []
    with open('produtos.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            produtos.append({
                'id': row[0],
                'nome': row[1],
                'preco': float(row[2]),
                'quantidade': int(row[3])
            })
    return produtos

def atualizar_produto(id, nome=None, preco=None, quantidade=None):
    produtos = ler_produtos()
    for produto in produtos:
        if produto['id'] == id:
            if nome:
                produto['nome'] = nome
            if preco is not None:
                produto['preco'] = preco
            if quantidade is not None:
                produto['quantidade'] = quantidade
            break
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for produto in produtos:
            writer.writerow([produto['id'], produto['nome'], produto['preco'], produto['quantidade']])

def deletar_produto(id):
    produtos = ler_produtos()
    produtos = [produto for produto in produtos if produto['id'] != id]
    with open('produtos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for produto in produtos:
            writer.writerow([produto['id'], produto['nome'], produto['preco'], produto['quantidade']])

def buscar_produto(nome):
    produtos = ler_produtos()
    return [produto for produto in produtos if produto['nome'] == nome]

def ordenar_produtos_por_nome():
    produtos = ler_produtos()
    return sorted(produtos, key=lambda x: x['nome'])

def ordenar_produtos_por_preco():
    produtos = ler_produtos()
    return sorted(produtos, key=lambda x: x['preco'])


def main():

    criar_usuario(1, "admin", "admin123", "gerente")
    criar_usuario(2, "funcionario", "func123", "funcionario")
    criar_produto(1, "Produto A", 10.0, 100)
    criar_produto(2, "Produto B", 20.0, 200)

    print("Usuários:")
    print(ler_usuarios())
    
    print("Produtos ordenados por nome:")
    print(ordenar_produtos_por_nome())

    print("Produtos ordenados por preço:")
    print(ordenar_produtos_por_preco())

    print("Busca por Produto A:")
    print(buscar_produto("Produto A"))

if __name__ == "__main__":
    main()
