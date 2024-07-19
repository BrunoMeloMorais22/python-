def Celsius_para_Fahrenheit(Celsius):
    return (Celsius * 9/5) + 32

def Fahrenheit_para_Celsius(Fahrenheit):
    return (Fahrenheit - 32) * 5/9

temp = float(input("Digite a temperatura: "))
escala = input("Digite a escala (C para Celsius, F para Fahrenheit):").upper()

if escala == 'C':
    resultado = Celsius_para_Fahrenheit(temp)
    print(f'A temperatu em Fahrenheit é : {resultado:.2f} F')

elif escala == 'F':
    resultado = Fahrenheit_para_Celsius(temp)
    print(f'A Temperatura em Celsius é : {resultado:.2f} C')

else:
    print("Digite uma temperatura válida.")

