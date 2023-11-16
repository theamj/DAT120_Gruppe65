#%%
"""
    Øving 10 - gruppearbeid del 2 - oppgave g)
    
    Finn antall penværsdager for hvert år og plott dette. Man kan finne antall penværsdager ved
    å sjekke gjennomsnittlig skydekke. Hver dag med verdi 3 eller lavere er en penværsdag.
    Inkluder bare år hvor det er data om skydekke for mesteparten av året, det må være data for
    minst 300 dager for at et år skal være gyldig.
    
    author: 279220
    date: 16/11/2023

"""

from numpy import NaN
import pandas as pd
import pylab
from del_2_oppgave_f import dict_from_data

data = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')

sky_coverage_yearly = dict_from_data(data, 6)

day_count_list = []
excluded = []
year_list = []

for year in sky_coverage_yearly:
    missing_data = 365 - len(sky_coverage_yearly[year])
    good_days = 0
    
    for day in sky_coverage_yearly[year]:
        
        if day == "-":
            missing_data += 1

        else:
            if float(day) <= 3:
                good_days += 1

    if missing_data < 65:
        day_count_list.append(good_days)
        year_list.append(year)

pylab.plot(year_list, day_count_list)

pylab.xlabel("år")
pylab.ylabel("finværsdager")
# %%
