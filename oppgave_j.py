# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:35:11 2023

@author: jopre
"""
# Importer funksjonen fra forrige oppgave
from oppgave_e import beregn_differanser

# Temperaturlista (eksempeldata)
temperaturliste = [15, 18, 18, 20, 22, 20, 17, 16, 14]

# Bruk funksjonen for å beregne differansene mellom temperaturer
differanser = beregn_differanser(temperaturliste)

# Gå gjennom lista med differanser og skriv ut informasjon
for indeks, differanse in enumerate(differanser):
    if differanse > 0:
        print(f"Indeks {indeks}: Stigende")
    elif differanse < 0:
        print(f"Indeks {indeks}: Synkende")
    else:
        print(f"Indeks {indeks}: Uforandret")
