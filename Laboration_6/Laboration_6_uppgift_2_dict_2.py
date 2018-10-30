# Uppgift 2

# Skriv ett program som

# konverterar ett tryck till nästkommande.

# myString = input("Vilket tryck är det? (t.ex 1013 mbar): ")

# NumberString = myString.split()[0]
# Unit = myString.split()[1]

NumberString = input("Vilket tryck är det?: ")
Unit = input("Vilken enhet för tryck är det?: ")
PressureDict= {"mbar":["torr", 760/1013],
               "torr":["pascal", 101325/760],
               "pascal":["atm", 1/101325],
               "atm":["mbar", 1013]}


"""
NumberString kommer att bli den sträng som matas in, samma gäller för Unit.
Numberstring förväntar sig ett tal, och Unit ett av de key-ord som finns i dict.
PressureDict är ett dictionairy där varje key-ord är de olika enheterna,
och listan som hör till key-ordet är nästkommande enhetstyp, och konverteringstalet.
"""

def convertMain(number, sort, aDict):
    if sort in aDict:
        try:
            number = float(number)
            number = convertToNextValue(number, sort, aDict)
            sort = nextUnit(sort)
            print("Trycket blir omvandlat: ", number, sort)
        except ValueError:
            print("Du måste skriva in ett tal som tryck.")
    else:
        print("Du måste skriva in en enhet för tryck. (mbar, torr, pascal eller atm)")


"""
Precis som föregående testas så att vi matat in rätt. 
Trycket och enhet kommer att omvandlas till nästkommande typ med hjälp av funktionerna nedan.
"""


def nextUnitInner(aUnit, aDict):
    aUnit = aDict[aUnit][0]
    return aUnit


"""
Denna funktion kommer givet en enhet och dictionaryn över att hämta ut nästkommande enhet,
genom att hämta ut första värdet i listan som tillhör key-ordet.
"""

def nextUnit(aUnit):
    aUnit = nextUnitInner(aUnit, PressureDict)
    return aUnit


"""
Gör inget speciellt, jag definierar bara nextUnit som funktionen över med ett fördefinierat dictionary,
så jag får en mindre parameter.
"""

def convertToNextValue(pressure, sort, aDict):
    pressure = pressure * aDict[sort][1]
    return pressure


"""
Kommer multiplicera det nuvarande trycket med konverteringstalet för nästkommande, vilket är sparat
som det andra elementet i varje lista som hör till respektive key-word i dictionaryt.
"""


convertMain(NumberString, Unit, PressureDict)