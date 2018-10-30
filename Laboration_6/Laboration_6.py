# laboration 6
# Uppgift 1
# Skriv ett program som:
# - Läser in ett tal till heltalsvariabeln tryck och en teckensträng till strängvariabeln sort.
# - Skriver ut "Tryck = " följt av tryck-värdet och sorten.

TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")
SortLista = ["mbar", "torr", "pascal", "atm"]


def tryckHanterare(tryck, sort, ls):
    if sort in ls:
        try:
            tal = float(tryck)
            print("Tryck = ", tal, sort)
        except ValueError:
            print("Tryck måste matas in som en siffra")
    else:
        print(sort, "är inte en definierad sort")


tryckHanterare(TryckString, Sort, SortLista)


# Uppgift 2


omvandlingsLista = ["mbar", float(1013), "torr", float(760), "pascal", float(101325), "atm",float(1)]
TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")





def tryckOmvandlare(tryck, sort, ls):
    def nextUnit(tryck, sort, aUnit):
        for a in range(0, 8, 2):
            if a < 6 and sort == aUnit[a]:
                tal = tryck * aUnit[a+3] / aUnit[a+1]
                sort = aUnit[a + 2]
                print("Tryck =" , tal, sort)
                break
            elif a == 6 and sort == aUnit[a]:
                tal = tryck * aUnit[1] / aUnit[7]
                sort = aUnit[0]
                print("Tryck =", tal, sort)
                break

    if sort in ls:
        try:
            tryck = float(tryck)
            nextUnit(tryck, sort, ls)
        except ValueError:
            print("Tryck måste matas in som en siffra")
    else:
        print(sort, "är inte en definierad sort")



tryckOmvandlare(TryckString, Sort, omvandlingsLista)

