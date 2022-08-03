from pacotes.produtos import produtos_disponiveis

carrinho = {}

def adicionar_no_carrinho():
    
    codigo = (int(input("Digite o codigo do produto: ")))
    quantidade = int(input("Quantidade: "))

    carrinho[codigo] = quantidade

def exibir_produtos_carrinho():

    if len(carrinho.keys()) < 1:
        print("O seu carrinho esta vazio")
    
    else:
        print("ID", "PRODUTO", "VALOR UNITARIO", "QUANTIDADE", "VALOR TOTAL")
        for id_produto_do_carrinho, quantidade in carrinho.items():
            nome, valor = produtos_disponiveis[id_produto_do_carrinho]
            valor_total_por_produto = valor * quantidade
            print(id_produto_do_carrinho, nome, valor, quantidade, valor_total_por_produto)

def excluir_todos_itens_do_carrinho():

    excluir_todos_itens = int(input("Deseja excluir todos os itens do seu carrinho? 1 para sim e 2 para nao: "))

    if excluir_todos_itens == 1:
        carrinho.clear()
        print("Carrinho vazio! O que deseja fazer agora? ")

    elif excluir_todos_itens == 2:
        print("O que deseja fazer agora?")

def remover_produto_do_carrinho():

    codigo_do_produto_para_excluir = int(input("Digite o codigo do produto que deseja excluir: "))

    for codigo in carrinho.copy():
        if codigo_do_produto_para_excluir == codigo:
            carrinho.pop(codigo)
            print("Produto excluido")

