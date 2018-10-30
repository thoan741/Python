TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")
NyaSort = input("Vad vill du omvandla till?: ")
omvandlingsLista = ["mbar", float(1013), "torr", float(760), "pascal", float(101325), "atm",float(1)]

def flerStegsOmvandlare(tryck, sort, newsort, ls):
    def NextUnit(tryck,sort,aUnit):
        while newsort != sort:
            for a in range(0, 8, 2):
                if a < 6 and sort == aUnit[a]:
                    tryck = tryck * aUnit[a+3] / aUnit[a+1]
                    sort = aUnit[a + 2]
                    break
                elif a == 6 and sort == aUnit[a]:
                    tryck = tryck * aUnit[1] / aUnit[7]
                    sort = aUnit[0]
                    break
        print("Tryck =", tryck, sort)
    if sort in ls:
        try:
            tryck = float(tryck)
            NextUnit(tryck,sort,ls)
        except ValueError:
            print("Tryck måste matas in som en siffra")
    else:
        print(sort, "är inte en definierad sort")



flerStegsOmvandlare(TryckString,Sort,NyaSort, omvandlingsLista)

