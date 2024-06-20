# Trabalho Prático - Sistema de Gerenciamento de Usuários e Produtos/Serviços

## Introdução

Este trabalho prático consiste na implementação de um sistema de gerenciamento de dados para uma empresa fictícia. O sistema é capaz de gerenciar informações sobre usuários e produtos/serviços, utilizando operações CRUD (Create, Read, Update, Delete). A empresa possui diferentes tipos de usuários, como gerente e funcionário, e oferece diversos produtos com atributos como preço e quantidade.

## Implementação

### Usuários

1. **Estrutura de Dados Escolhida**
   - Utilizamos uma lista de dicionários para carregar as informações dos usuários. Cada dicionário representa um usuário e contém os campos `id`, `nome`, `senha` e `permissao`.

2. **Estrutura do Arquivo de Registro**
   - O arquivo de registro dos usuários é um CSV (`usuarios.csv`) com as seguintes colunas: `id`, `nome`, `senha`, `permissao`.

3. **Funcionalidades**
   - **Create (Criar)**
     - Função: `criar_usuario`
     - Descrição: Adiciona um novo usuário ao sistema e salva no arquivo `usuarios.csv`.
   - **Read (Ler)**
     - Função: `ler_usuarios`
     - Descrição: Lê todos os usuários do arquivo `usuarios.csv` e os carrega na estrutura de dados.
   - **Update (Atualizar)**
     - Função: `atualizar_usuario`
     - Descrição: Atualiza as informações de um usuário existente.
   - **Delete (Deletar)**
     - Função: `deletar_usuario`
     - Descrição: Remove um usuário do sistema.

### Produtos/Serviços

1. **Estrutura de Dados Escolhida**
   - Utilizamos uma lista de dicionários para carregar as informações dos produtos/serviços. Cada dicionário representa um produto/serviço e contém os campos `id`, `nome`, `preco` e `quantidade`.

2. **Estrutura do Arquivo de Registro**
   - O arquivo de registro dos produtos/serviços é um CSV (`produtos.csv`) com as seguintes colunas: `id`, `nome`, `preco`, `quantidade`.

3. **Funcionalidades**
   - **Create (Criar)**
     - Função: `criar_produto`
     - Descrição: Adiciona um novo produto ao sistema e salva no arquivo `produtos.csv`.
   - **Read (Ler)**
     - Função: `ler_produtos`
     - Descrição: Lê todos os produtos do arquivo `produtos.csv` e os carrega na estrutura de dados.
   - **Update (Atualizar)**
     - Função: `atualizar_produto`
     - Descrição: Atualiza as informações de um produto existente.
   - **Delete (Deletar)**
     - Função: `deletar_produto`
     - Descrição: Remove um produto do sistema.
   - **Buscar**
     - Função: `buscar_produto`
     - Descrição: Busca um produto pelo nome.
   - **Ordenar por Nome**
     - Função: `ordenar_produtos_por_nome`
     - Descrição: Imprime os registros de produtos ordenados por nome.
   - **Ordenar por Preço**
     - Função: `ordenar_produtos_por_preco`
     - Descrição: Imprime os registros de produtos ordenados por preço.

## Conclusão

Durante a implementação deste trabalho prático, enfrentamos alguns desafios, principalmente relacionados à manipulação de arquivos CSV. No entanto, conseguimos superá-los utilizando o módulo `csv` do Python. A escolha de usar listas de dicionários como estrutura de dados facilitou a manipulação e a leitura dos registros.

Algumas melhorias que poderiam ser feitas incluem:
- Implementação de uma interface gráfica para tornar o sistema mais amigável.
- Adição de mais níveis de permissão de usuários.
- Validações mais robustas para entradas do usuário.

## Arquivos do Projeto

- **Script Principal**: `Trabalho Prático.py`
- **Arquivo de Usuários**: `usuarios.csv`
- **Arquivo de Produtos/Serviços**: `produtos.csv`
