# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 07:45:17 2023

@author: idaue

En måte å sjekke trender i temperatur gjennom året er å ta gjennomsnittet av temperaturen
for en tidsperiode (for eksempel ei uke eller en måned) og så sjekke om snittet endrer seg.
Ved å ta gjennomsnittet så fjerner man at temperaturen går opp og ned fra en dag til den
neste. Regn ut gjennomsnittstemperaturen for hver måned (for eksempel april 2007) og legg
disse gjennomsnittene i ei ny liste. Bruk funksjonen fra del 1 deloppgave e) for å regne ut ei
liste med differanser. Plott både lista over gjennomsnittstemperaturer og lista over
differanser med måned og år på x-aksen.
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
            value_per_month = dict()
            value_per_year[date.year] = value_per_month
            value_per_month[date.month] = []
            value_per_month[date.month].append(value)
        else:
            if date.month not in value_per_month:
                value_per_month[date.month] = []
                value_per_month[date.month].append(value)
            else:
                value_per_month[date.month].append(value)
        
    return value_per_year 

def diff(list):
    differanser=[] #lager en tom liste for å lagre differanser
    j = 0
    
    for i in list:
        differanse = i-j 
        differanser.append(differanse) 
        j = i
    return differanser

def mean(list):
    sum = 0
    for i in list:
        sum += i
        
    return sum / len(list)  

def plot_verdi(month, mean, diff, year): 
    plt.plot(month,mean, label=f"{year}mean temperature")
    plt.plot(month, diff, label=f"{year}delta temperature")
    plt.xlabel("months")
    plt.ylabel("temperatures")
    plt.legend()
    plt.title("Mean and Delta T by year")    
    plt.grid(True)
    
    plt.show()
    
if __name__ == '__main__':
    
    dataset = pd.read_csv('snoedybder_vaer_en_stasjon_dogn.csv', encoding='utf-8', sep=';')
    temp_per_year = dict_from_data(dataset, 5)
     
    for year in temp_per_year:
        diff_list = []
        mean_list = []
        month_list = []
        
        mean_last = 0
        for month in temp_per_year[year]:
            mean_month = mean(temp_per_year[year][month])
            differ = mean_month - mean_last
            mean_list.append(mean_month)
            diff_list.append(differ)
            mean_last = mean_month
            month_list.append(month)
       
        plot_verdi(month_list,mean_list, diff_list, year)
        