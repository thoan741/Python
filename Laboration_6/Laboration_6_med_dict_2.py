# Uppgift 2

# Skriv ett program som

# konverterar ett tryck till nästkommande.

talString = input("Vilket tryck är det?: ")
Sort = input("Vilken enhet för tryck är det?: ")
SortedList = ("mbar", "torr", "pascal", "atm")
tryckDict = {"mbar":760/1013, "torr":101325/760, "pascal":1/101325, "atm":1013}


def Utskrift(tal, sort, ls, aDict):
    if sort in ls:
        try:
            tal = float(tal)
            tal = convertToNextValue(tal, sort, aDict)
            sort = nextUnit(sort)
            print("Trycket blir omvandlat: ", tal, sort)
        except ValueError:
            print("Du måste skriva in ett tal som tryck.")
    else:
        print("Du måste skriva in en enhet för tryck. (mbar, torr, pascal eller atm)")


def nextUnitInner(aUnit, ls):
    if ls.index(aUnit) < 3:
        i = ls.index(aUnit)
        i += 1
        aUnit = ls[i]
        return aUnit
    else:
        aUnit = ls[0]
        return aUnit


def nextUnit(aUnit):
    aUnit = nextUnitInner(aUnit,SortedList)
    return aUnit


def convertToNextValue(tryck, sort, aDict):
    tryck = tryck * aDict[sort]
    return tryck






Utskrift(talString, Sort, SortedList, tryckDict)