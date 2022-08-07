from pacotes.produtos import produtos_disponiveis, exibir_lista_produtos

import csv

carrinho = {}

def adicionar_no_carrinho():

    codigo = (int(input("Digite o codigo do produto: ")))
    quantidade = int(input("Quantidade: "))
    carrinho[codigo] = quantidade


def exibir_produtos_carrinho():
    valor_total_a_pagar = 0

    if len(carrinho.keys()) < 1:
        print("O seu carrinho esta vazio")
    
    else:
        print("ID", "PRODUTO", "VALOR UNITARIO", "QUANTIDADE", "VALOR TOTAL")
        for id_produto_do_carrinho, quantidade in carrinho.items():
            nome, valor = produtos_disponiveis[id_produto_do_carrinho]
            valor_total_por_produto = valor * quantidade
            valor_total_a_pagar += valor_total_por_produto
            print(id_produto_do_carrinho, nome, valor, quantidade, valor_total_por_produto)
        print("Total a pagar: R$", valor_total_a_pagar)


def retornar_produtos_carrinho():

    valor_total_a_pagar = 0

    for id_produto_do_carrinho, quantidade in carrinho.items():
        nome, valor = produtos_disponiveis[id_produto_do_carrinho]
        valor_total_por_produto = valor * quantidade
        valor_total_a_pagar += valor_total_por_produto
        return id_produto_do_carrinho, nome, valor, quantidade, valor_total_por_produto


def valor_total_da_compra():
    valor_total_a_pagar = 0

    for id_produto_do_carrinho, quantidade in carrinho.items():
        nome, valor = produtos_disponiveis[id_produto_do_carrinho]
        valor_total_por_produto = valor * quantidade
        valor_total_a_pagar += valor_total_por_produto
    return valor_total_a_pagar

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

def finalizar_compra():

    if len(carrinho.keys()) < 1:
        print("O seu carrinho esta vazio")

    else:
        compra_finalizada = int(input("Deseja finalizar compra? 1 para sim 2 para nao: "))
            
        if compra_finalizada == 1:
            exibir_produtos_carrinho()

            metodo_pagamento = int(input("1 - dinheiro\n2 - debito\n3 - credito\nSelecione o metodo de pagamento: "))

            if metodo_pagamento == 1 or metodo_pagamento == 2:
                valor_total = valor_total_da_compra()
                valor_total -= 0.05 * valor_total
                print("O valor a pagar : R$", valor_total)
            elif metodo_pagamento == 3:
                valor_total = valor_total_da_compra()
                print("O valor a pagar : R$", valor_total)
            else:
                print("Opcao invalida. ")

            with open("arquivos/CupomFiscal.csv", "w+", newline="") as fcsv:
                escrever = csv.writer(fcsv, delimiter = ',')
                escrever.writerow(("ID", "PRODUTO", "VALOR UNITARIO", "QUANTIDADE", "VALOR TOTAL"))
                escrever.writerow(retornar_produtos_carrinho())
                escrever.writerow(("Valor total da compra", valor_total))

            with open ("arquivos/CupomFiscal.csv","r") as fcsv:
                csv.reader(fcsv)

def encerrar_programa():

    if len(carrinho.keys()) > 0:

        programa_encerrado = print(int(input("Voce tem produtos no carrinho. Tem certeza que deseja sair? 1 para sim 2 para nao: ")))

    if programa_encerrado == 1:
        print("Programa encerrado. Volte sempre!")

    elif programa_encerrado == 2:
        print("O que deseja fazer agora?")

    else:
        print("Programa encerrado. Volte sempre!")
