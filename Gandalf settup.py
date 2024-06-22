import pickle

u1 = 1




print("Přejete si pokračovat ve hře? Ano/Ne")
load = str(input("Přejete? : "))
if load == "Ne":
    print("What is you Avatar Name?")

    namep = str(input("Name?: "))

    print("Now we can chose atributs of our mage for battle")

    p12 = str(input("What class do you have: "))



    class osoba:
        def __init__(self, name="", classs="", level=0):
            self.name = name
            self.classs = classs
            self.level = level

        def __str__(self):
            return (f"{self.name} is {self.classs} {self.level}. level ")

    postava = osoba(name=name, classs=p12, level=u1)

    with open("postava.pickle", "wb") as f:
        pickle.dump(postava, f)

    print(postava)

elif load == "Ano":
    class osoba:
        def __init__(self, name="", classs="", level=0):
            self.name = name
            self.classs = classs
            self.level = level

        def __str__(self):
            return(f"{self.name} is {self.classs} {self.level}. level ")

    postava = osoba(name=None, classs=None, level=None)

    with open("postava.pickle", "rb") as f:
        postava = pickle.load(f)

        print(postava)

else:
    raise NameError


