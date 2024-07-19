
def verifica_numero_par_ou_impar(numero):
    try:
        # Tentar converter o número para inteiro
        numero = int(numero)
        
        # Verificar se o número é par ou ímpar
        if numero % 2 == 0:
            print("O número é par.")
        else:
            print("O número é ímpar.")
    except ValueError:
        # Se ocorrer um erro de ValueError (não é possível converter para inteiro)
        print("Por favor, insira um número válido.")

# Solicitar ao usuário que insira um número
numero_digitado = input("Por favor, insira um número: ")

# Chamar a função para verificar se o número é par ou ímpar
verifica_numero_par_ou_impar(numero_digitado)

