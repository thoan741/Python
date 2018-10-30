from Laboration6Library import *

def main():

    numberString = input("Ange ett tryck:")
    unit = input("Från vilken sort?:")
    newUnit = input("Till vilken sort?:")

    pressureDict = {"mbar": ["torr", 1013],
                    "torr": ["pascal", 760],
                    "pascal": ["atm", 101325],
                    "atm": ["mbar", 1]}

    while not checkIfValidSort(unit, pressureDict):
        print("Den enhet som vi går från måste vara en de fördefinierade. (mbar, pascal, atm eller torr)")
        unit = input("Försök igen: ")
    while not checkIfValidSort(newUnit, pressureDict):
        print("Den enhet som vi går till måste vara en de definierade (mbar, pascal, atm eller torr).")
        newUnit = input("Försök igen: ")
    while not checkIfValidNumber(numberString):
        print("Trycket måste skrivas in som ett tal.")
        numberString = input("Försök igen: ")

    sortDict = {"Från enhet": unit, "Till enhet": newUnit, "Från värde": numberString}


    saveNumber = float(numberString)
    saveUnit = unit
    number = convertBothTo(sortDict, pressureDict)[0]
    unit = convertBothTo(sortDict, pressureDict)[1]
    print(saveNumber, saveUnit, "=", number, unit)


main()