# Laboration 6

# Uppgift 1

# Skriv ett program som

# läser in ett tal till heltalsvariabeln tryck och en teckensträng till strängvariabeln sort.
# skriver ut "Tryck = " följt av tryck-värdet och sorten.
# Med snygg felhantering.

# myString = input("Vilket tryck är det? (t.ex 1013 mbar): ")

# NumberString = myString.split()[0]
# Unit = myString.split()[1]

NumberString = input("Vilket tryck är det?: ")
Unit = input("Vilken enhet för tryck är det?: ")
PressureDict = {"mbar": ["torr", 760/1013],
                "torr": ["pascal", 101325/760],
                "pascal": ["atm", 1/101325],
                "atm": ["mbar", 1013]}

"""
NumberString kommer att bli den sträng som matas in, samma gäller för Unit.
Numberstring förväntar sig ett tal, och Unit ett av de key-ord som finns i dict.
PressureDict är ett dictionairy där varje key-ord är de olika enheterna,
och listan som hör till key-ordet är nästkommande enhetstyp, och konverteringstalet.
"""


def utskrift(number, sort, aDict):
    if sort in aDict:
        try:
            number = float(number)
            print("Trycket blir: ", number, sort)
        except ValueError:
            print("Du måste skriva in ett tal som tryck.")
    else:
        print("Du måste skriva in en enhet för tryck. (mbar, torr, pascal eller atm)")


"""
Denna funktion kommer att först se om enheten som matades in tillhör en av de definierade typerna.
Om den inte är det skrivs ett felmeddelande ut. Sedan testas om vi matade in ett tal.
Om så är fallet skrivs trycket ut, annars ett annat felmeddelande.
"""

utskrift(NumberString, Unit, PressureDict)