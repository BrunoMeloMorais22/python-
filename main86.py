
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = calcular_imc(peso, altura)

if imc >= 28.80:
    print("Você está entrando na fase de obesidade.")
elif imc >= 33.90:
    print("Você está na fase de sedentarismo, cuidado.")
else:
    print("Você está no estado perfeito")

print(f'Seu IMC é: {imc:.2f}')
