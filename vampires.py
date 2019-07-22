class Vampire:

    coven = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.in_coffin = False
        self.drank_blood = False

    def drink_blood(self):
        self.drank_blood = True

    def go_home(self):
        self.in_coffin = True

    @classmethod
    def create(cls, name, age):
        vamp = Vampire(name, age)
        cls.coven.append(vamp)
        return vamp
    
    @classmethod
    def sunrise(cls):
        for vamp in cls.coven:
            if vamp.in_coffin == False or vamp.drank_blood == False:
                cls.coven.remove(vamp)

    @classmethod
    def sunset(cls):
        for vamp in cls.coven:
            vamp.in_coffin = False
            vamp.drank_blood = False

tom = Vampire.create('Tom', 140)
alucard = Vampire.create('Alucard', 1001)
belmont = Vampire.create('Belmont', 700)
sloan = Vampire.create('Sloan', 900)
buffy = Vampire.create('Buffy', 240)

for vamp in Vampire.coven:
    print(vamp.name)
print('-----LINE BREAK-----')

tom.drink_blood()
alucard.drink_blood()
alucard.go_home()
belmont.drink_blood()
sloan.go_home()
buffy.drink_blood()
buffy.go_home()

Vampire.sunrise()

for vamp in Vampire.coven:
    print(vamp.name)
print('-----LINE BREAK-----')

Vampire.sunset()

for vamp in Vampire.coven:
    print(vamp.name)
print('-----LINE BREAK-----')