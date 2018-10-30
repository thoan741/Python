# Uppgift 1


# pressureString = input("Vilket tryck är det? (t.ex 1013 mbar): ")
    # pressureString = pressureString.split()

    #if ifInputLengthCorrect(pressureString,2):
    #    pass
    # else:
    #    print("Du har inte gjort en korrekt inmatning. Du behöver mata in på formen: tal enhet (t.ex 1013 mbar)")
    #    return

    # numberString = pressureString[0]
    # unit = pressureString[1]


#Uppgift 2

# pressureString = input("Vilket tryck är det? (t.ex 1013 mbar): ")
# pressureString = pressureString.split()

# if ifInputLengthCorrect(pressureString, 2):
#    pass
# else:
#    print("Du har inte gjort en korrekt inmatning. Du behöver mata in på formen: tal enhet (t.ex 1013 mbar)")
#    print("Försök igen!")
#    main()
#    return

# numberString = pressureString[0]
# unit = pressureString[1]

# Uppgift 3

# pressureString = input("Skriv in ett tryckvärde följt av två enheter som det ska konverteras mellan "
    #                        "(t.ex 1013 mbar pascal): ")
    # pressureString = pressureString.split()

    # if ifInputLengthCorrect(pressureString, 3):
    #     pass
    # else:
    #     print("Du har inte gjort en korrekt inmatning. "
    #           "Du behöver mata in på formen: tal enhet enhet (t.ex 1013 mbar pascal)")
    #     print("Försök igen!")
    #     main()
    #     return

    # numberString = pressureString[0]
    # unit = pressureString[1]
    # newUnit = pressureString[2]

# number = convertBothTo(numberString, Unit, newUnit, pressureDict)[0]
        # Unit = convertBothTo(numberString, Unit, newUnit, pressureDict)[1]

# Library:

#def convertBothTo(number, aUnit, newUnit, aDict):
#    """
#    Denna kommer att konvertera ett godtyckligt antal steg, tills dess att enhetstypen matchar den efterfrågade.
#    """
#    number = makeNumberFloat(number)
#    while aUnit != newUnit:
#        number = convertToNextValue(number, aUnit, aDict)
#        aUnit = nextUnit(aUnit, aDict)
#    return (number, aUnit)