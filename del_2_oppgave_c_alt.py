"""
    trosh!
    
"""

import pandas
import datetime
from Oppgave_B_Del_2 import dager_skifoere

def beregn_lineær_trend(x_koordinater, y_koordinater):
    # Beregn gjennomsnittet av x- og y-verdiene
    gjennomsnitt_x = sum(x_koordinater) / len(x_koordinater)
    gjennomsnitt_y = sum(y_koordinater) / len(y_koordinater)

    # Beregn a ved hjelp av formelen for a
    a_numerator = sum((x - gjennomsnitt_x) * (y - gjennomsnitt_y) for x, y in zip(x_koordinater, y_koordinater))
    a_denominator = sum((x - gjennomsnitt_x) ** 2 for x in x_koordinater)
    a = a_numerator / a_denominator

    # Beregn b ved hjelp av formelen for b
    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a, b

def skifore_trend():
    skisesong = dager_skifoere()
    sesong = []
    for i in skisesong[1]:
        sesong.append(i[0])
        
    return beregn_lineær_trend(skisesong[0], sesong)

if __name__ == "__init__":
    print(skifore_trend())
