def checkIfValidSort(aUnit, aDict):
    """
    Denna funktion kommer att kolla om aUnit är en key i ett dictionary.
   """
    if aUnit in aDict:
        return True
    else:
        return False


def checkIfValidNumber(number):
    """
    Denna funktion kollar om det värde som matades in är ett tal.
    """
    try:
        number = float(number)
        return True
    except ValueError:
        return False


def checkIfValid(number, aUnit, aDict):
    """
    returnerar True om båda funktionerna över returnerar True, annars False.
    """
    if checkIfValidNumber(number) and checkIfValidSort(aUnit, aDict):
        return True
    else:
        return False


def checkIfValid2(number, aUnit, newUnit, aDict):
    """
    Denna behövs bara för uppgift 3. Den kommer att kolla om även den tredje parametern är ett av key-orden i dict.
    """
    if checkIfValid(number, aUnit, aDict) and checkIfValidSort(newUnit, aDict):
        return True
    else:
        return False


def ifInputLengthCorrect(ls, length):
    """
    kollar om längden av teckensträngen efter att split applicerats, är av rätt längd.
    """
    if length == len(ls):
        return True
    else:
        return False


def nextUnit(aUnit, aDict):
    """
    Konverterar enhetstypen till nästa enhetstyp.
    """
    aUnit = aDict[aUnit][0]
    return aUnit


def convertToNextValue(number, aUnit, aDict):
    """
    konverterar storleken trycket till den efterföljande tryck.
    """
    number = float(number)
    number = number * aDict[nextUnit(aUnit, aDict)][1] / aDict[aUnit][1]
    return number


def convertBoth(number, aUnit, aDict):
    """
    Kommer att konvertera både tryck och enhet, returnerar en lista.
    """
    number = float(number)
    number = convertToNextValue(number, aUnit, aDict)
    aUnit = nextUnit(aUnit,aDict)
    return (number, aUnit)


def convertBothTo(convertDict, aDict):
    """
    Denna kommer att konvertera enhet och tal till nästkommande, ett godtyckligt antal steg, tills dess att enhetstypen matchar den efterfrågade.
    """
    convertDict["Från värde"] = float(convertDict["Från värde"])
    while convertDict["Från enhet"] != convertDict["Till enhet"]:
        convertDict["Från värde"] = convertToNextValue(convertDict["Från värde"], convertDict["Från enhet"], aDict)
        convertDict["Från enhet"] = nextUnit(convertDict["Från enhet"], aDict)
    return (convertDict["Från värde"], convertDict["Från enhet"])

