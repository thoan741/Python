# -*- coding: utf-8 -*-
class calcQueue:
    """
    Här definieras en klass. I instanser av denna klass kommer värden sparas
    i en lista.
    """

    def __init__(self):
        """
        Det här är en konstruktor, och denna kommer att skapa en instans
        av klassen calcQueue när man t.ex. skriver x = calcQueue().
        """
        self.__Q = []

    def full(self):
        """
        Returnerar alltid falskt, kön är aldrig full.
        """
        return False

    def empty(self):
        """
        En instans av kön är bara tom när den är just en tom lista. Returnerar booleanskt värde.
        """
        return self.__Q == []

    def enqueue(self, e):
        """
        enqueue kommer att lägga till ett element sist i en instans av klassen.
        """
        self.__Q.append(e)

    def dequeue(self):
        """
        Funktionen dequeue kommer att spara det första elementet i instansen,
        ta bort det elementet ur instansen för att sedan returnera det elementet.
        """
        a = self.__Q[0]
        self.__Q.pop(0)
        #del self.__Q[0]
        return a

    def show(self):
        """
        Printar kön.
        """
        a = self.__Q
        print(a)

#kö = calcQueue()

#kö.show()

#kö.enqueue(31.0)

#kö.show()

#kö.enqueue(15.3)

#kö.enqueue('+')

#kö.show()

#kö.dequeue()

#kö.show()
