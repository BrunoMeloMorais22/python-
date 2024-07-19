class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return 'Au Au!'

class Gato(Animal):
    def fazer_som(self):
        return 'Miau!'

rex = Cachorro('Rex')
print(rex.fazer_som())  # Saída: Au Au!

whiskers = Gato('Whiskers')
print(whiskers.fazer_som())  # Saída: Miau!
