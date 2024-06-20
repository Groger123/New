
slot=2



def aer():

    try:
        if slot == 2:
            p21 = str(input("Vlož jméno 2. postavy: "))
            p22 = str(input("Vlož povolání 2. postavy: "))
            if p22 == "Válečník":
                pass
            elif p22 == "Kouzelník":
                pass
            elif p22 == "Zvěd":
                pass
            elif p22 == "Rytíř":
                pass
            else:
                raise NameError
    except NameError:
        print("Spatná třída")
        return aer()


aer()