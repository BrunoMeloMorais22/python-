
class product:
    def __init__(self, pitem, citem, nitem):
        self.priceItem = pitem
        self.colorItem = citem
        self.nameItem = nitem

    def printname(self):
        print(self.priceItem, self.colorItem, self.nameItem)

x = product(80, 'Black', 'Bolsa')
x.printname()