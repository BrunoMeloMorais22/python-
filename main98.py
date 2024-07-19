

def mostrarfuncionarios(funcionarios):
    if not funcionarios:
        print("Nenhum funcionario cadastrado")
    
    else:
        print("Funcionarios cadstrados")
        for i, funcionarios in enumerate(funcionarios, 1):
            print(f"{i}. {funcionarios}")

def main():
    
    funcionarios = []

    while True:
        print("\nEscolha uma opção")
        print("1. Cadastrar funcionario")
        print("2. Mostrar lista de funcionarios")
        print("3. Sair do Sistema")

        escolha = input("Escolha uma opçaõ (1/2/3): ")

        if escolha == '1':
            nome_funcionario = input("Digite o nome e sobrenome do funcionário: ")
            idade_funcionario = input("Digite a idade do funcionário por favor: ")
            cargo = input("Digite o cargo que será excercido: ")

            funcionarios.append({'nome': nome_funcionario, 'idade': idade_funcionario, 'função': cargo})
        
        elif escolha == '2':
            mostrarfuncionarios(funcionarios)
        
        elif escolha == '3':
            print("Saindo do Sistema. Até a próxima")
            break

main()

