# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:52:09 2023

@author: jopre
"""

def beregn_differanser(liste):
    differanser=[] #lager en tom liste for å lagre differanser
    
    for i in range(len(liste)-1): #går gjennom alle tallene utenom det siste
        differanse = liste[i+1]-liste[i]#regner ut differansen mellom neste tallet og dette
        differanser.append(differanse) #legger til differansen i den nye listen
        
    return differanser #retunerer listen med differanser
    
talliste = [1,3,6,10,15]
resulatat = beregn_differanser(talliste)
print (resulatat) # skriver ut differansen mellom tallene i listen