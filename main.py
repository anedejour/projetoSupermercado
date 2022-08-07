from pacotes.produtos import exibir_lista_produtos
from pacotes.compras import adicionar_no_carrinho, exibir_produtos_carrinho, carrinho, remover_produto_do_carrinho, excluir_todos_itens_do_carrinho, exibir_produtos_carrinho, finalizar_compra, encerrar_programa



def main():
    while menu_principal():
        pass

def menu_principal():
    print("MENU PRINCIPAL")
    print("1 - Listar produtos")
    print("2 - Exibir carrinho")
    print("3 - Adicionar produto ao carrinho")
    print("4 - Remover produto do carrinho")
    print("5 - Finalizar compra")
    print("6 - Esvaziar carrinho")
    print("7 - Encerrar programa")

    opcao = opcao_menu()

    if opcao == 1:
        exibir_lista_produtos()
    
    elif opcao == 2:
        exibir_produtos_carrinho()
        
    
    elif opcao == 3:
        exibir_lista_produtos()
        adicionar_no_carrinho()
    
    elif opcao == 4:
        exibir_produtos_carrinho()
        remover_produto_do_carrinho()


    elif opcao == 5:
        finalizar_compra()

    elif opcao == 6:
        excluir_todos_itens_do_carrinho()
    
    elif opcao == 7:
        encerrar_programa()
        return False

        
    elif opcao is None:
        return
    
    return True


def opcao_menu():
    opcao = input("Digite a opcao: ")
        

    try:
        opcao_int = int(opcao)
        return opcao_int
    except ValueError:
        print("Opcao invalida.")
        return None

if __name__ == "__main__":
    main()
