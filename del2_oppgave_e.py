# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 06:13:59 2023

@author: idaue

Beregn veksten for den tenkte planten for hvert år i datasettet med bruk av funksjonen fra
del 1 oppgave h). Plott dette for hvert år i datasettet. Inkluder bare år hvor det er
temperaturdata for mesteparten av året, det må være data for minst 300 dager for at et år
skal være gyldig. Dette vil kreve at dere lager separate lister for hvert år som kan brukes som
parameter til funksjonen fra del 1 oppgave h)
"""
import pandas as pd
from numpy import NaN
import matplotlib.pyplot as plt
from datetime import datetime

def dict_from_data(dataset, column):
    value_per_year = dict()

    for row in dataset.values:
        if row[2] is NaN:
            break
        date = datetime.strptime(row[2], '%d.%m.%Y')
        if row[column] != '-':
            value = row[column].replace(',','.')
            value = float(value)
    
        if date.year not in value_per_year:
            value_per_year[date.year] = []
        value_per_year[date.year].append(value)
        
    return value_per_year 


def g_rate(n):
    if n < 5: 
       return 0
    else:
        return n - 5

def growth(list):
    g_units = 0
    growth_day = []
    for i in (list): 
        g_units = g_units + g_rate(i)
        growth_day.append(g_units)
    return(growth_day)

def plot_verdi(day,growth,year): 
    plt.plot(day,growth,label=f"growth in {year} ")
    plt.xlabel("days")
    plt.ylabel("g_units")
    plt.legend()
    plt.title("Growth per year")    
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    
    dataset = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')
    temp_per_year = dict_from_data(dataset, 5)
        
    excluded = []
    year_list = []
    
    for year in temp_per_year:
        dash_count = 0
        for i in temp_per_year[year]:
                dash_count += 1
        missing_data = (365 - dash_count)
     
        if missing_data < 65:
            
            day_list = []
            growth_list = (growth(temp_per_year[year]))
            for i in range(len(growth_list)):
                day_list.append(i+1)
            year_list.append(year)
        
            plot_verdi(day_list,growth_list,year)
          
        