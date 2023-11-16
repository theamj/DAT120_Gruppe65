#%%
"""
    Øving 10 - gruppearbeid del 2 - oppgave f)
    
    Bruk funksjonen fra del 1 oppgave f) til å finne den lengste perioden med tørke (ingen nedbør) for hvert år i datasettet. 
    Plott resultatet. Inkluder bare år hvor det er nedbørsdata for mesteparten av året, 
    det må være data for minst 300 dager for at et år skal være gyldig.
    
    author: 279220
    date: 10/11/2023
    
"""


import pandas as pd
from numpy import NaN
import pylab
from datetime import datetime
from oppgave_f import match_zero_sequence as sequence

dataset = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')

rain_per_year = dict()

for row in dataset.values:
    if row[2] is NaN:
        break
    date = datetime.strptime(row[2], '%d.%m.%Y')
    rain = row[4].replace(',', '.')
    if rain.isnumeric():
        rain = float(rain)
    
    if date.year not in rain_per_year:
        rain_per_year[date.year] = []
    rain_per_year[date.year].append(rain)


drought_list = []
year_list = []
for year in rain_per_year:
    drought_list.append(sequence(rain_per_year[year]))
    year_list.append(year)

pylab.plot(year_list, drought_list)

pylab.xlabel("år")
pylab.ylabel("dager uten regn")
    
# %%
