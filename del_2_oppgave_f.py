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
from oppgave_f import match_number_sequence as sequence


def dict_from_data(dataset, column):
    value_per_year = dict()

    for row in dataset.values:
        if row[2] is NaN:
            break
        date = datetime.strptime(row[2], '%d.%m.%Y')
        value = row[column].replace(',', '.')
        if value.isnumeric():
            value = float(value)
    
        if date.year not in value_per_year:
            value_per_year[date.year] = []
        value_per_year[date.year].append(value)
        
    return value_per_year 

if __name__ == '__main__':
    
    dataset = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')

    rain_per_year = dict_from_data(dataset, 4)

    drought_list = []
    excluded = []
    year_list = []
    for year in rain_per_year:
        dash_count = 0
        for i in rain_per_year[year]:
            if i == "-":
                dash_count += 1
        
        missing_data = (365-len(rain_per_year[year])) + dash_count
        if missing_data < 65:
            drought_list.append(sequence(rain_per_year[year], 0))
            year_list.append(year)
        else:
            excluded.append(year)

    print(excluded)

    pylab.plot(year_list, drought_list)

    pylab.xlabel("år")
    pylab.ylabel("dager uten regn")

# %%
