# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:23:04 2023

@author: 47954
"""
testliste = [4,7,15,]

def g_rate(n):
    if n < 5: 
       return 0
    else:
        return n - 5


def growth(list):
    g_units = 0
    for i in range(len(list)): 
        g_units = g_units + g_rate((list)[i])
    return(g_units)


if __name__==  "__main__":
    print(f"Planten har vokst totalt: {growth(testliste)} enheter.")
