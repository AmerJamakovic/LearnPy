#Napisati program koji simulira bacanje 3 kockice (jedna kockica ima 6 strana i na tim stranama su brojevi 1-6).
#Simuliranje bacanja svake kockice ostvariti funkcijom rand()%6+1.
#Simulirati konstanto bacanje sve tri kockice dok se u dva uzastopna bacanja ne desi da se dobiju isti brojevi na sve tri kockice
#(npr. u šestom bacanju se dobiju brojevi 2,2,2 a u sedmom 4,4,4 na sve tri kockice).
#Ispisati koliko je ukupno bilo bacanja dok se nije ispunio navedeni uslov. Nije potrebno tražiti bilo kakav unos od korisnika.
#Tekst je napisan za rad u CPP.

import random as r

SameNumbersTwoTimes=False
numberOfThrows=0


while not SameNumbersTwoTimes:
    numberOfThrows += 1
    ThreeDice = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6)]
    if ThreeDice[0]==ThreeDice[1] and ThreeDice[0]==ThreeDice[2]:
        FirstSameThrow=ThreeDice
        ThreeDice = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6)]
        if ThreeDice[0]==ThreeDice[1] and ThreeDice[0]==ThreeDice[2]:
            SameNumbersTwoTimes=True
            print(f"Dice was thrown {numberOfThrows} times. First time you got {FirstSameThrow} and second time you got {ThreeDice}")
        
