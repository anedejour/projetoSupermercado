produtos_disponiveis = {1:("arroz",20.00), 2:("feijao",10.00), 3:("macarrao",5.00), 4:("farinha",5.00), 5:("refrigerante",7.00), 6:("bolacha",2.00), 7:("pao",1.00)}



def exibir_lista_produtos():
    print("ID -  PRODUTO,VALOR")
    for c,v in produtos_disponiveis.items():
        print(c, " - ", v)

# def pegar_valor():
#     for valor in produtos_disponiveis.values():
#         preco = valor[1]
#         print(preco)
