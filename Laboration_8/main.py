# Author: Thomas Andersson
# Version: 1.2
# Date: 2018-10-31
# Kommentarer.



from morse import *

def main():
    """
    Andra elementet i x ändras endast till False när ctrl+D klickas, och då avslutas programmet.
    Alla andra jämförelser kollar om andra elementet som returnas ur konverteringsfunktionerna
    är sant eller falskt, där de respektive kommer ge falskt om det ej kan översättas.
    Kan det inte översättas åt något håll, kommer första stället i strängen där översättning inte fungerade
    att printas ut för bägge konverteringsmetoderna.
    """
    x = [True, True]
    while x[1]:
        x = inputManagement()
        if not x[1]:
            print(x[0])
            print("Tack och adjö!")
            break
        elif convertSymbolsToMorse(x[0], symbolToMorseDict)[1]:
            print(convertSymbolsToMorse(x[0], symbolToMorseDict)[0])
        elif convertMorseToSymbols(x[0], morseToSymbolDict)[1]:
            print(convertMorseToSymbols(x[0], morseToSymbolDict)[0])
        else:
            print((convertSymbolsToMorse(x[0], symbolToMorseDict)[0]), "kan inte översättas till morse!")
            print((convertMorseToSymbols(x[0], morseToSymbolDict)[0]), "är inget morsetecken! ")

main()