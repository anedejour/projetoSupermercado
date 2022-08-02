from pacotes.produtos import produtos_disponiveis

carrinho = {}

def adicionar_no_carrinho():
    
    codigo = (int(input("Digite o codigo do produto: ")))
    quantidade = int(input("Quantidade: "))

    carrinho[codigo] = quantidade


# minha_dupla = ("algo", 300)
# nome = minha_dupla[0]
# valor = minha_dupla[1]
# _, valor = minha_dupla

# def calcular_total_por_produto():

#     for produto_comprado in carrinho.keys():
#         for produto in produtos_disponiveis.keys():
#             if produto_comprado == produto:
#                 valor_unitario = pegar_valor()
#     return valor_unitario


def exibir_produtos_carrinho():

    print("ID -  PRODUTO,VALOR  -   QUANTIDADE")

    for id_produto, produto_e_valor in carrinho.items():
        for id_produto_disponivel, produto_e_valor_que_existem_no_mercado in produtos_disponiveis.items():
            if id_produto == id_produto_disponivel:
                print(produtos_disponiveis[id_produto_disponivel])

