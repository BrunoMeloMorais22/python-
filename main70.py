
class car:
    def __init__(self, modelo, marca, cor, portas):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.portas = portas
    
    def show(self):
        print(self.modelo, self.marca, self.cor, self.portas)
    
x = car("Toyota", "Corola", "Red", 4)
x.show()