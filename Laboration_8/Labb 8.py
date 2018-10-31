# Author: Thomas Andersson
# Date: 2018-10-31
# Version 1.0

import urllib.request

"""
Jag importerar utllib.request, för att kunna läsa och spara textsnuttar från hemsidor.
"""

link = "http://www.nada.kth.se/kurser/su/DA2001/sudata18/laborationer/morse.d"
f = urllib.request.urlopen(link)
myfile = f.read()


myfile = str(myfile)[2:]
myfile2 = myfile[0:134] + 'Å' + myfile[142:148] + 'Ä' + myfile[156:161] + 'Ö' + myfile[169:275]
myDict = {myfile2[0]: myfile2[2:int(myfile2[1])+2]}
myDict[myfile2[4]] = myfile2[6:10]
print(myfile2)
print(myfile)
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

symbolToMorseDict = makeDict(myfile2)
# Jag skapar ett dictionary med funktionen makeDict och teckensträngen som laddades ned.
# Denna kan användas för att konvertera symboler,bokstäver och nummer till morsekod.

morseToSymbolDict = {v: k for k, v in symbolToMorseDict.items()}
# Här skapas ett nytt dictionary med hjälp av det som skapades över, där value och keyword har bytt plats,
# för att få ett nytt dictionairy som konverterar morsetecken till bokstäver,symboler eller siffror.

print(symbolToMorseDict)
print(morseToSymbolDict)

def inputManagement():
    try:
        input("Mata in ett meddelande i klartext eller morsekod: ")
    except EOFError as e:
        #print(e)
        print("Tack och adjö!")

"""
Här är ett första test för att få en snygg avslutning när ctrl+D hålls ned.
"""

def convertType(msg,dict1,dict2):
    """
    Konverterar ett meddelande från en typ till den andra,
    fungerar just nu endast för konvertering från versaler till morsetecken.
    Kommer dela upp denna i två funktioner, en som hanterar morse->bokstäver och en bokstäver->morse.
    Funktionen split kan nog vara bra för att konvertera morse till bokstäver.
    :param msg: Denna parameter innehåller ett meddelande.
    :param dict1: Ett dictionairy som konverterar åt ett håll
    :param dict2: Ett dictionairy som konverterar åt andra hållet.
    :return:
    """
    b = ''
    if msg[0] in dict1:
        for i in msg:
            if i in dict1:
                a = dict1[i]
                b = b+a+' '
            elif i == ' ':
                b = b + ' '
            else:
                pass
    elif msg[0] in dict2:
        for i in msg:
            if i in dict2:
                a = dict2[i]
                b =b+a+' '
            elif i == ' ':
                b = b + ' '
            else:
                pass
    else:
        pass

    return b

print(convertType('HEJ HOPP!', symbolToMorseDict, morseToSymbolDict))

print(convertType('.... . .---  .... --- .--. .--. ..--. ', morseToSymbolDict, symbolToMorseDict))