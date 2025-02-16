# Solusi DDP 1 MOOC Pre-U 2022/2023
# Nama: Gina Pratiwi

# Superclass Animal
class Animal:
    def __init__(self, name, birthdate, diet, colors):
        self.name = name
        self.birthdate = birthdate  
        self.colors = colors

    def eats(self):
        print(self.name, "is eating...")

    def drinks(self):
        print(self.name, "is drinking...")  # Default method

    def birthyear(self):
        return self.birthdate[2]  # Mengembalikan tahun lahir

    def __str__(self):
        return f"Binatang {self.__class__.__name__} berwarna {self.colors} lahir di tahun {self.birthyear()} dengan nama {self.name}"

# Subclass Lion
class Lion(Animal):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate, "Carnivore", ["Gold"])

    def roar(self):
        print("Roarrr!")

# Subclass Giraffe
class Giraffe(Animal):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate, "Herbivore", ["Yellow", "Brown"])

# Subclass Elephant
class Elephant(Animal):
    def __init__(self, name, birthdate):
        super().__init__(name, birthdate, "Herbivore", ["Gray"])

    def drinks(self):
        print(self.name, "is drinking lots of water!")  # Overriding method

# Contoh Interaksi Program
if __name__ == "__main__":
    # Object singa
    simba = Lion("Simba", ("20", "01", "2005"))
    simba.eats()
    simba.drinks()
    print(simba.birthyear())
    print(simba)
    simba.roar()
    print("~~~")

    # Object jerapah
    charles = Giraffe("Charles", ("10", "12", "2004"))
    charles.eats()
    charles.drinks()
    print(charles.birthyear())
    print(charles)
    print("~~~")

    # Object gajah
    tina = Elephant("Tina", ("01", "01", "2020"))
    tina.eats()
    tina.drinks()
    print(tina.birthyear())
    print(tina)