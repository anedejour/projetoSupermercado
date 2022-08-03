from pacotes.produtos import exibir_lista_produtos
from pacotes.compras import adicionar_no_carrinho, exibir_produtos_carrinho, carrinho, remover_produto_do_carrinho, excluir_todos_itens_do_carrinho, exibir_produtos_carrinho



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

    opcao = opcao_menu()

    if opcao == 1:
        listar_produtos()
        return True
    
    elif opcao == 2:
        exibir_carrinho()
        return True
    
    elif opcao == 3:
        adicionar_produto()
        return True
    
    elif opcao == 4:
        remover_produto()
        return True

    elif opcao == 5:
        return False

    elif opcao == 6:
        esvaziar_carrinho()
        return False
        
    elif opcao is None:
        return True


    return True

def opcao_menu():
    opcao = input("Digite a opcao: ")
        

    try:
        opcao_int = int(opcao)
        return opcao_int
    except ValueError:
        print("Opcao invalida.")
        return None

def listar_produtos():

    exibir_lista_produtos()

def exibir_carrinho():

    exibir_produtos_carrinho()

def adicionar_produto():

    exibir_lista_produtos()

    adicionar_no_carrinho()

def remover_produto():
    exibir_carrinho()

    remover_produto_do_carrinho()

def esvaziar_carrinho():

    excluir_todos_itens_do_carrinho()

if __name__ == "__main__":
    main()
