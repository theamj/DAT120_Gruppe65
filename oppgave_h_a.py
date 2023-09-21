# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 12:57:18 2023

@author: 47954
"""
testliste = [4,7,15,]
testliste2 = [15,7,4]

def g_rate(n):
    return n - 5

       
def growth(list):
    g_units = 0
    for i in range(len(list)): 
        g_units = g_units + g_rate((list)[i])
        if g_units <= 0:
            return (f"Planten døde dag: {i}.")
    return (f"Planten har vokst totalt: {g_units} enheter.")

if __name__==  "__main__":
    print(growth(testliste2))
