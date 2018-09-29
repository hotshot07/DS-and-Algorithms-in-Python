#Elo ranking system
#Each person has a base rating of 1400
#At each given time, PlayerA has a rating Ra and PlayerB has a rating Rb
#when two players are matched up, the probability of winning is calculated with this formula
#P(a)=1/(1+10**((R(b)-R(a)/400)))

#obviously, P(a)+P(b)=1

import math
import random
import time

def Probability(rating1 ,rating2):
    Pa=1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating2 - rating1) / 400))
    Pb=1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1- rating2) / 400))

    print("Probability of winning is")
    print("Pa =", round(Pa, 5)," Pb =", round(Pb, 5))
    return Pa,Pb


def EloRating(Ra, Rb, d):
    K=100
    Pa,Pb=Probability(Ra,Rb)

    #Player1 wins
    if(d==1):
        Ra = Ra + K*(1-Pa)
        Rb = Rb + K*(0-Pb)

    #Player2 wins
    else:
        Ra = Ra + K*(0-Pa)
        Rb = Rb + K*(1-Pb)


    return Ra,Rb


# Ra and Rb are current ELO ratings
Players={
    'Player1':1400,
    'Player2':1400
}

i=0

copy=dict(Players)

for name1,rating1 in copy.items():
    for name2,rating2 in copy.items():
        if name1==name2:
            continue
        else:
            i+=1
            print("Match:",i)
            print("Match between", name1,"and", name2)

            d=random.randint(1,3)
            print(Players)
            rating1=Players[name1]
            rating2=Players[name2]
            up1,up2=EloRating(rating1,rating2,d)
            if(d==1):
                print("Match won by:",name1)
            else:
                print("Match won by:",name2)
            Players.update({name1:up1})
            Players.update({name2:up2})
            print(Players)













