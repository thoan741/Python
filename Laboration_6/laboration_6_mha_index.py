TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")
SortLista = ["mbar", "torr", "pascal", "atm"]


def tryckHanterare(tryck, sort, ls):
    if sort in ls:
        try:
            tal = float(tryck)
            print("Tryck = ", tal, sort)
        except ValueError:
            print("Tryck måste matas in som en siffra")
    else:
        print(sort, "är inte en definierad sort")


tryckHanterare(TryckString, Sort, SortLista)

# uppgift 2

TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")
SortLista = ["mbar", "torr", "pascal", "atm"]
VardeLista = [int(1013), int(760), int(101325), int(1)]

def konvertering(value, sort, sortList, valueList):
    i = sortList.index(sort)
    value = int(value)
    if i == 3:
        value = value * valueList[0] / valueList[3]
        sort = sortList[0]
        print("konverterat till nästa sort blir trycket: ", value, sort)
    else:
        value = value * valueList[i+1] / valueList[i]
        sort = sortList[i+1]
        print("konverterat till nästa sort blir trycket: ", value, sort)


konvertering(TryckString, Sort, SortLista, VardeLista)

# uppgift 3:

TryckString = input("Mata in trycket: ")
Sort = input("Mata in sorten: ")
NewSort = input("mata in nya sorten: ")
SortLista = ["mbar", "torr", "pascal", "atm"]
VardeLista = [int(1013), int(760), int(101325), int(1)]


def konvertering(value, sort, newSort,sortList, valueList):
    i = sortList.index(sort)
    j = sortList.index(newSort)
    value = int(value)
    value = value * valueList[j] / valueList[i]
    sort = newSort
    print("det nya trycket blir: ", value, sort)


konvertering(TryckString, Sort, NewSort, SortLista, VardeLista)
