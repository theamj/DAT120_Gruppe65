# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:23:04 2023

@author: 47954
"""

testliste = [4,7,15,]
testliste2 = [15,7,4]

# Oppgave H)    En plante vil vokse ved en temperatur over 5 grader. 
#               Ettersom tempereturen øker, vokser planten linjært fortere.
#               Lager en funksjon som regner ut den totale veksten.

def pos_growth(list):
    g_units = 0
    for i in range(len(list)): 
     g_rate = (list)[i] - 5
     g_units = g_units + g_rate
    return(g_units)


if __name__==  "__main__":
    print(pos_growth(testliste))


#  Frivillig A) Tar med negativ vekst, planten dør hvis vekst når 0.
     
def growth(list):
    g_units = 0
    for i in range(len(list)): 
        g_rate = (list)[i] - 5
        g_units = g_units + g_rate
        if g_units <= 0:
            return 0
    return g_units

if __name__==  "__main__":
   
    print(growth(testliste))


# Frivillig B)  Returner i tilegg periode og størrelse av størst vekst.
#               !!!Har misforstått oppgaven!!
def results(list):     
    
    g_units = 0
    g_max = 0
    d_max = 0
    
    for i in range(len(list)): 
       
        g_rate = (list)[i] - 5
        g_units = g_units + g_rate
               
        if g_units <= 0:
            return [i, d_max, g_max]
       
        if g_rate > g_max:
            g_max = g_rate
            d_max = i
    return [g_units, i, g_max]
        

if __name__==  "__main__":
    print(results(testliste2))