from Laboration6Library import *


def main():

    numberString = input("Ange ett tryck:")
    unit = input("Från vilken sort?:")
    pressureDict = {"mbar": ["torr", 1013],
                    "torr": ["pascal", 760],
                    "pascal": ["atm", 101325],
                    "atm": ["mbar", 1]}

    while not checkIfValidSort(unit, pressureDict):
        print("Enheten måste matas in som en av definierade tryckenheterna (mbar, pascal, atm eller torr).")
        unit = input("Försök igen: ")
    while not checkIfValidNumber(numberString):
        print("Trycket måste skrivas in som ett tal.")
        numberString = input("Försök igen: ")

    number = convertToNextValue(numberString, unit, pressureDict)
    unit = nextUnit(unit, pressureDict)
    print("Konverterat till nästkommande tryckenhet blir trycket: ", number, unit)


main()