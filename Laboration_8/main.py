# Author: Thomas Andersson
# Version: 1.3
# Date: 2018-11-02
# Kommentarer: Felhantering gällande fel vid inläsning av filen morse.d

from morse import *


def main():
    """
    Andra elementet i x ändras endast till False när ctrl+D klickas, och då avslutas programmet.
    Alla andra jämförelser kollar om andra elementet som returnas ur konverteringsfunktionerna
    är sant eller falskt, där de respektive kommer ge falskt om det ej kan översättas.
    Kan det inte översättas åt något håll, kommer första stället i strängen där översättning inte fungerade
    att printas ut för respektive konverteringsmetod.
    """
    x = [True, True]
    if symbolToMorseDict:
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
    else:
        print("Filen som hämtas in är inte på korrekt form, eller så har en fil som inte finns försökt hämtas in.")
        print("Tack och adjö!")


main()