
class person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def exibir(self):
        print(self.name, self.age, self.height)
    

x = person("Maria", "56", 1.65)
x.exibir()