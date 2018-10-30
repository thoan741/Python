# Uppgift 3

# Skriv ett program som

# konverterar tryck från en typ som till en annan.

NumberString = input("Vilket tryck är det?: ")
Sort = input("Gå från tryckenhet: ")
NewSort = input("Gå till tryckenhet: ")
SortedList = ("mbar", "torr", "pascal", "atm")
ConversionDict = {"mbar": 760 / 1013, "torr": 101325 / 760, "pascal": 1 / 101325, "atm": 1013}


def main():

    convertMain(NumberString, Sort, NewSort, SortedList, ConversionDict)


def convertMain(tal, sort, nySort, ls, aDict):
    if sort in ls and nySort in ls:
        try:
            tal = float(tal)
            while sort != nySort:
                tal = convertToNextValue(tal, sort, aDict)
                sort = nextUnit(sort)
            print("Det omvandlade trycket blir: ", tal, sort)
        except ValueError:
            print("Du måste skriva in ett tal som tryck.")
    else:
        print("Du måste skriva in en enhet för tryck där det efterfrågas. (mbar, torr, pascal eller atm)")


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
    aUnit = nextUnitInner(aUnit, SortedList)
    return aUnit


def convertToNextValue(tryck, sort, aDict):
    tryck = tryck * aDict[sort]
    return tryck





main()