# -*- coding: utf-8 -*-
class calcStack:
    """
    Här definieras en klass. I instanser av denna klass kommer värden sparas
    i en lista.
    """

    def __init__(self):
        """
        Det här är en konstruktor, och denna kommer att skapa en instans
        av klassen calcStack när man t.ex. skriver x = calcStack().
        """
        self.__L = []

    def full(self):
        """
        Returnerar alltid falskt, stacken är aldrig full.
        """
        return False

    def empty(self):
        """
        En instans av stacken är bara tom när den är just en tom lista. Returnerar booleanskt värde.
        """
        return not self.__L

    def push(self, e):
        """
        Kommer att lägga till ett element sist i en instans.
        """
        self.__L.append(e)

    def pop(self):
        """
        Hämtar även ut element längst bak i instansen. sparar undan sista elementet,
        tar bort det från instansen och returnerar sedan elementet.
        """
        a = self.__L[-1]
        self.__L.pop()
        #del self.__L[-1]
        return a


    def show(self):
        """
        Printar stacken.
        """
        a = self.__L
        print(a)

#kö = calcStack()

#kö.show()

#kö.push(5)

#kö.show()

#kö.push(7)

#kö.show()

#kö.pop()

#kö.show()
