from pacotes.produtos import exibir_lista_produtos
from pacotes.compras import adicionar_no_carrinho, exibir_produtos_carrinho, carrinho


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

    if carrinho == {}:
        opcao = int(input("Seu carrinho esta vazio. Deseja adicionar produtos? (1 - sim 2 - nao): "))

        if opcao == 1:
            print("Produtos disponiveis no mercado: ")
            adicionar_produto()
        else:
            print("O que deseja fazer? ")  

    else:
        exibir_produtos_carrinho()

def adicionar_produto():

        exibir_lista_produtos()

        adicionar_no_carrinho()

def remover_produto():
    exibir_carrinho()
    print("remover produto")

def esvaziar_carrinho():

    print("esvaziado")


    exibir_carrinho()

    confirmar = int(input("Tem certeza que quer remover os produtos? Digite 1 para sim e 2 para nao: "))

    if confirmar == 1:
        segunda_chance_compra = int(input("Carrinho vazio. Deseja efetuar compras? Digite 1 para sim e 2 para nao: "))

        if segunda_chance_compra == 1:
            listar_produtos()
        elif segunda_chance_compra == 2:
            print("Obrigado pela visita. Volte sempre.")        

if __name__ == "__main__":
    main()
