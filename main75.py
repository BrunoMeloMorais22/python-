
celular = input("Digite uma marca de celular: ")

marcas = ["iphone", "motorola", "sangung", "lg"]

if celular.lower() in marcas:
    print("Escolha aceita")

else:
    print("Marca não exixte")