
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def show(self):
        print(self.firstname, self.lastname)
  
x = Person("Bruno", "Melo")

x.show()
