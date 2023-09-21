# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 13:12:52 2023

@author: 47954
"""

testliste = [4,7,15,]
testliste2 = [15,7,4]


def results(list):     
    
    g_units = 0
    g_max = 0
    
    for i in range(len(list)): 
       
        g_rate = (list)[i] - 5
        g_units = g_units + g_rate
               
        if g_units <= 0:
            return (f"Planten døde periode: {i}.")
       
        if g_rate > g_max:
            g_max = g_rate
            periode = i
    return (f"Planten har vokst totalt: {g_units}.\nPlanten vokste mest i perioden: " +
            f"{periode}, da den vokste med: {g_max} enheter.")
        

if __name__==  "__main__":
    print (results(testliste))