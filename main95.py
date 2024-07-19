


def mostrarproduto(produtos):
    if not produtos:
        print("Não há produtos cadastrado")
    
    else: 
        print("Seus produtos cadastrados")
        for i, produtos in enumerate(produtos, 1):
            print(f"{i}. {produtos}")
    
def main():
    produtos = []

    print("Veja já os produtos que você já anunciou!")

    while True:
        print("\nEscolha uma opção")
        print("1. Cadastrar Produtos")
        print("2. Produtos Cadastrados")
        print("3. Sair do sistema.")

        escolha = input("Digite sua opção: ")

        if escolha == '1':
            nome_produto = input("Digite o nome do produto que deseja postar: ")
            valor_produtor = int(input("Digite o valor do seu produto em R$: "))

            if valor_produtor > 50:
                mudanca_preco = valor_produtor * 0.10
                mudanca_preco = valor_produtor + mudanca_preco
                print(f'Produto cadastrado, com alteração. Valor final de {mudanca_preco:.2f}')
            
            else:
                print("Produto cadastrado")

            produtos.append({'nome': nome_produto, 'valor': valor_produtor})
        
        elif escolha == '2':
            mostrarproduto(produtos)

        elif escolha == '3':
            print("Saindo do sistema.")
            break

if __name__ == "__main__":
    main()
