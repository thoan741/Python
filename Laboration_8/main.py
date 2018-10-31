# Author: Thomas Andersson
# Version: 1.0
# Date: 2018-10-31



from morse import *

def main():
    x = [True, True]
    while x[1]:
        x = inputManagement()
        if not x[1]:
            break
        elif convertSymbolsToMorse(x[0], symbolToMorseDict)[1]:
            print(convertSymbolsToMorse(x[0], symbolToMorseDict)[0])
        elif convertMorseToSymbols(x[0], morseToSymbolDict)[1]:
            print(convertMorseToSymbols(x[0], morseToSymbolDict)[0])
        else:
            print((convertSymbolsToMorse(x[0], symbolToMorseDict)[0]), "kan inte översättas till morse!")
            print((convertMorseToSymbols(x[0], morseToSymbolDict)[0]), "är inget morsetecken! ")

main()