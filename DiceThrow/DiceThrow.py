#Napisati program koji simulira bacanje 3 kockice (jedna kockica ima 6 strana i na tim stranama su brojevi 1-6).
#Simuliranje bacanja svake kockice ostvariti funkcijom rand()%6+1.
#Simulirati konstanto bacanje sve tri kockice dok se u dva uzastopna bacanja ne desi da se dobiju isti brojevi na sve tri kockice
#(npr. u šestom bacanju se dobiju brojevi 2,2,2 a u sedmom 4,4,4 na sve tri kockice).
#Ispisati koliko je ukupno bilo bacanja dok se nije ispunio navedeni uslov. Nije potrebno tražiti bilo kakav unos od korisnika.
#Tekst je napisan za rad u CPP.

import random as r

same_numbers_two_times=False
number_of_throws=0


while not same_numbers_two_times:
    number_of_throws += 1
    three_dice = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6)]
    if three_dice[0]==three_dice[1] and three_dice[0]==three_dice[2]:
        first_same_throw=three_dice
        three_dice = [r.randint(1, 6), r.randint(1, 6), r.randint(1, 6)]
        if three_dice[0]==three_dice[1] and three_dice[0]==three_dice[2]:
            same_numbers_two_times=True
            print(f"Dice was thrown {number_of_throws} times. First time you got {first_same_throw} and second time you got {three_dice}")
        
