
class car:
    def __init__(self, modelo, marca, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
    
    def exibir(self):
        print(self.modelo, self.marca, self.cor, self.ano)

x = car("Corolla", "Toyota", "Preto", 2022)
x.exibir()