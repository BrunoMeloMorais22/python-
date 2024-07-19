

def cadastrofilmes(filmes):
    if not filmes:
        print("Nenhum filme cadastrado")
    else:
        print("Filmes Cadastrados")
        for i, filmes in enumerate(filmes, 1):
            print(f"{i}, {filmes}")
        
def main():

    filmes = []

    while True:
        print("\nEscolha uma opção por favor")
        print("1. Cadastrar Filme")
        print("2. Ver lista de filme cadastrados")
        print("3. Sair do Sistema")

        escolha = input("Por favor, escolha umas das opções (1/2/3) ")

        if escolha == '1':
            nome_filme = input("Digite o nome do filme por favor: ")
            genero_filme = input("Digite o gênero do filme por favor: ")
            ano_filme = input("Digite o ano do filme por favor: ")

            filmes.append({'nome_filme': nome_filme, 'genero_filme': genero_filme, 'ano_filme': ano_filme})
        
        elif escolha == '2':
            cadastrofilmes(filmes)
        
        elif escolha == '3':
            print("Saindo do Sistema")
            break
main()









