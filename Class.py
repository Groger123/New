import pickle
class car():

        def __init__(self, max_speed = 0, akcelerace = 0, výrobce = "BMW", druh = "Sedan"):

            self.max_speed = max_speed
            self.akcelerace = akcelerace
            self.výrobce = výrobce
            self.druh = druh

        def __str__(self):
                return f"Maximální rychlost je {self.max_speed}, Akcelerace vozu je {self.akcelerace}, Výrobce je {self.výrobce}, a druh je {self.druh}"
class Bus():

        def __init__(self, max_speed = 0, akcelerace = 0, výrobce ="", váha = 0):

            self.max_speed = max_speed
            self.akcelerace = akcelerace
            self.výrobce = výrobce
            self.váha = váha

        def __str__(self):
            return f"Maximální rychlost je {self.max_speed} (Km/h), Akcelerace vozu je {self.akcelerace} (m/s2), Výrobce je {self.výrobce}, a váha je {self.váha} t"
class Motorcycle():

        def __init__(self, max_speed = 0, akcelerace = 0, výrobce = "", počet_kol = 0):

            self.max_speed = max_speed
            self.akcelerace = akcelerace
            self.výrobce = výrobce
            self.počet_kol = počet_kol

        def __str__(self):
            return f"Maximální rychlost je {self.max_speed} (Km/h), Akcelerace vozu je {self.akcelerace} (m/s2), Výrobce je {self.výrobce}, a počet kol má {self.počet_kol}"



ve1 = car(max_speed=140, výrobce="BMW", druh="sedan")
ve2 = Bus(max_speed= 110, akcelerace=80, výrobce="Mercedes", váha=5 )
ve3 = car(max_speed=180, akcelerace=50, výrobce="BMW", druh="sedan")
ve4 = car(max_speed=110, akcelerace=20, výrobce="Toyota", druh="combi")
ve5 = car(max_speed=100, akcelerace=40, výrobce="Toyota", druh="Hachback")
ve6 = car(max_speed=160, akcelerace=40, výrobce="BMW", druh="sedan")
ve7 = car(max_speed=120, akcelerace=40, výrobce="Audi", druh="sedan")

with open("ve1.pickle", "wb") as f:
    pickle.dump(ve1, f)

print(ve1)
print(ve2)
print(ve3)
print(ve4)
print(ve5)
print(ve6)
print(ve7)


aa










