produtos_disponiveis = {
    1:("arroz",20.00), 
    2:("feijao",10.00), 
    3:("macarrao",5.00), 
    4:("farinha",5.00), 
    5:("refrigerante",7.00), 
    6:("bolacha",2.00), 
    7:("pao",1.00)}



def exibir_lista_produtos():
    print("{0: <5} {1: <12} {2: >5}".format("ID", "PRODUTO", "VALOR"))
    for codigo_do_produto, nome_e_valor_unitario in produtos_disponiveis.items():
        nome, valor_unitario = nome_e_valor_unitario
        print(f"{codigo_do_produto: <5} {nome: <12} {valor_unitario: >5}")
        