# Author: Thomas Andersson
# Date: 2018-10-31
# Version 1.3
# Tillsnyggat, tagit bort tester och kommenterat.

import urllib.request

"""
urllib.request låter mig hämta text från hemsidor.
"""

link = "http://www.nada.kth.se/kurser/su/DA2001/sudata18/laborationer/morse.d"
f = urllib.request.urlopen(link)
myFile = f.read()

myString = str(myFile)[2:-1]
improvedString = myString[0:134] + 'Å' + myString[142:148] + 'Ä' + myString[156:161] + 'Ö' + myString[169:]
myDict = {improvedString[0]: improvedString[2:int(improvedString[1])+2]}
myDict[improvedString[4]] = improvedString[6:10]
"""
Här snyggas textfilen som laddades ner till. Först konverteras den från bit till sträng.
Sedan tar jag bort onödiga tecken i början av strängen. Bokstäver Å,Ä,Ö sparas inte korrekt, så jag byter ut de tecknen,
samt tar bort en flärp i slutet.
"""



def makeDict(str):
    """
    makeDict skapar ett dictionary ur en teckensträng, där varje bokstav kommer att bli ett keyword
     och paras ihop med den morsesträng som tillhör ordet.
    :param str: str är en textsträng där en bokstav kommer först, sedan ett nummer n,
     och sedan en morsekod som är n tecken långt
    :return: Ett dictionary där varje keyword är en bokstav/nummer/symbol som är parat ihop med
     den teckensträng som är morsekoden för den bokstaven.
    """
    a = 0
    b = 1
    c = {}
    while a < len(str):
        c[str[a]] = str[a+2:int(str[b])+a+2]
        a = int(str[b])+a+2
        b = a+1
    return c


symbolToMorseDict = makeDict(improvedString)
# Jag skapar ett dictionary med funktionen makeDict och teckensträngen som laddades ned.
# Denna kan användas för att konvertera symboler,bokstäver och nummer till morsekod.

morseToSymbolDict = {v: k for k, v in symbolToMorseDict.items()}
# Här skapas ett nytt dictionary med hjälp av det som skapades över, där value och keyword har bytt plats överallt,
# för att då få ett nytt dictionary som konverterar morsetecken till bokstäver,symboler eller siffror.


def inputManagement():
    """
    Denna ser till att programavslut sker korrekt.
    """
    try:
        a = input("Mata in ett meddelande i klartext eller morsekod: ")
        return [a, True]
    except EOFError as e:
        return [e, False]




def convertSymbolsToMorse(msg, aDict):
    """
    Konverterar ett meddelande från morse till bokstäver/siffror/symboler.
    :param msg: Denna parameter innehåller ett meddelande.
    :param aDict: Ett dictionary med bokstäver som keyword och motsvarande morsetecken
     som värde i en teckensträng.
    :return: Returnerar den omvandlade teckensträngen om möjligt, annars returneras falskt samt vart problem uppstod.
    """
    b = ''
    for i in msg:
        if i.upper() in aDict:
            a = aDict[i.upper()]
            b = b + a + ' '
        elif i == ' ':
            b = b + ' '
        else:
            return [i, False]

    return [b, True]


def convertMorseToSymbols(msg, aDict):
    """
    Konverterar ett morsemeddelande till bokstäver.
    :param msg: msg kommer vara en teckensträng, som förväntas innehålla morsetecken.
    :param aDict: dictionary som konverterar morsekod till bokstäver.
    :return: returnerar ett morsemeddelande omvandlat till bokstäver om det går, annars returneras False och
     vart i textsträngen problemet uppstod..
    """
    msg = msg.split("  ")
    last = "."
    res = ""
    for x in msg:
        x = x.split()
        for i in x:
            if last in [".", "!", "?"]:
                if i in aDict:
                    res = res + aDict[i]
                    last = aDict[i]
                else:
                    return [i, False]
            else:
                if i in aDict:
                    res = res + aDict[i].lower()
                    last = aDict[i]
                else:
                    return [i, False]
        res = res + ' '
    return [res, True]


