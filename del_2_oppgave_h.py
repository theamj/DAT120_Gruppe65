#%%
"""
    Øving 10 - gruppearbeid del 2 - oppgave h)

    For hvert år finn høyeste middelvind samt medianen for vindstyrke. For å finne medianen,
    lag ei liste over alle verdiene for det året, sorter lista, og plukk ut det midterste elementet i
    den sorterte lista. Plott dette for hvert år. Inkluder bare år hvor det er data om vind for
    mesteparten av året, det må være data for minst 300 dager for at et år skal være gyldig.

    Author: 279220
    date: 16/11/2023
    
"""

import numpy
import pandas as pd
import pylab
from del_2_oppgave_f import dict_from_data

data = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')

wind_data_yearly = dict_from_data(data, 7)

wind_max_yearly = []
wind_median_yearly = []
excluded = []
year_list = []

for year in wind_data_yearly:
    missing_data = 365 - len(wind_data_yearly[year])
    wind_data = []
    
    for day in wind_data_yearly[year]:
        
        if day == "-":
            missing_data += 1
        else:
            wind_data.append(float(day))
            
    wind_median = numpy.median(wind_data)
    wind_max = sorted(wind_data, reverse=True)[0]
            
    if missing_data < 65:
        wind_max_yearly.append(wind_max)
        wind_median_yearly.append(wind_median)
        year_list.append(year)
    else:
        excluded.append(year)

print(excluded)

pylab.plot(year_list, wind_max_yearly, label='maks')
pylab.plot(year_list, wind_median_yearly, label='median')

pylab.xlabel("år")
pylab.ylabel("vind [m/s]")
pylab.legend()
# %%
