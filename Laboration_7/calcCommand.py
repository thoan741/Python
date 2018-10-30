# -*- coding: utf-8 -*-

##
 # Läs in modulerna för kö och stack
##
import calcQueue
import calcStack


##
 # listan med giltiga globala kommandon
 # dessa kan inte ingå i en kommandosekvens
##
commands = ['hjälp', 'sluta', 'töm']


##
 # listan med giltiga operatorer
##
operator = ['=', '+', '-', '*', '/', '^']

##
 # skapa kommandokön
##
Q = calcQueue.calcQueue()
##
 # skapa operandstacken
##
S = calcStack.calcStack()
##
 # utskrift av hjälptexten
##
def printHelp():
    print('''
Mata in en sekvens med kommandon i omvänd polsk notation,
separerade med " ". Tillåtna kommandon är:
decimala tal (1, 1.2, ...)
'=' skriv ut värdet på stackens topp.
'+' addera stackens två översta värden.
'-' subtrahera stackens två översta värden.
'*' multiplicera stackens två översta värden.
'/' dividera stackens två översta värden.
'^' exponera stackens två översta värden.

Därutöver kan man skriva
'sluta' för att avsluta sessionen
'hjälp' för att skriva ut denna text eller
'töm'   för att tömma kalkylatorns stack
''')


##
 # Låter omgivande programdelar få del av
 # programmets globala kommandon
 # används av huvudprogrammet
##
def getGlobalCommands():
    return commands


##
 # Städning av kön
 # används av funktionen validate
##
def clearQueue():
    while not Q.empty():
        Q.dequeue()

def clearStack():
    while not S.empty():
        S.pop()


##
 # kontrollerar att inmatningen endast innehåller
 # tillåtna tal och operatorer
 # används av huvudprogrammet efter varje inmatning via tangentbordet
##
def validate(clist):
    ok = True              # antag att allt är bra
    for c in clist:
        if c in operator:  # köa operatorer
            Q.enqueue(c)
        elif c in commands: # inga globala kommandon tillåts här 
            ok = False
            clearQueue()
            print("'" + c + "' är inte tillåtet i en kommandosekvens!")
            break
        else:                # annars kan det bara vara
            try:
                x = float(c) # tal, som köas
                Q.enqueue(x)
            except:          # eller fel, som ger avbrott
                ok = False
                clearQueue()
                print("Känner inte till något '" + c + "'-kommando!")
                break
    return ok                # berätta för huvudprogrammet hur det gick


##
 # utför allt som finns i kommandokön
 # anropas från huvudprogrammet efter varje validering
 # OBS att kön endast innehåller giltiga kommandon och tal
 # eftersom validering av innehållet redan skett
##
def doCommands():
    # töm kön och utför vare kommando
    while not Q.empty():
        cmd = Q.dequeue()
        if cmd == '=':       # Visa vad stacken innehåller
            if S.empty():    # säg ifrån om den är tom
                print('Stacken är tom')
            else:            # annars
                t = S.pop()  # hämta översta elementet
                print(t)     # skriv ut
                S.push(t)    # och lägg tillbaka

        elif cmd in operator: # försök utföra en beräkning
            performCalculation(cmd)
        else:                 # sista alternativet är
            S.push(cmd)       # ett tal, spara det i stacken


##
 # försöker utföra en beräkning:
 #   om stacken inte innehåller minst två operander,
 #     signaleras fel
 #   annars hämtas två värden från stackens topp,
 #   beräkningen utförs och
 #   resultatet läggs tillbaka på stacken
 #
 # pre: stacken innehåller minst två värden och
 #      c är ett giltigt (aritmetiskt) kommando
 # post: stacken innehåller resultatet av beräkningen
 # används av: doCommand 
## 
def performCalculation(c):
    if S.empty():
        print('Stacken är tom!')
    else:
        op1 = S.pop()
        if S.empty():
            print('Stacken innehåller bara en operand!')
            S.push(op1)
        else:
            op2 = S.pop()
            res = None
            if c == '+':
                res = op2 + op1
            elif c == '-':
                res = op2 - op1
            elif c == '*':
                res = op2 * op1
            elif c == '/':
                res = op2 / op1
            elif c == '^':
                res = op2 ** op1
            S.push(res)