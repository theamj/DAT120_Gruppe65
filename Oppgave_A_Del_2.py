import csv
from datetime import datetime

def les_vaerdata(filnavn):
    vaerdata = []

    with open(filnavn, newline='', encoding='utf-8') as csvfile:
        vaerleser = csv.reader(csvfile, delimiter=';')

        header = next(vaerleser)  

        for rad in vaerleser:
            if not rad[2]:  
                continue

            stasjon = {
                'Navn': rad[0],
                'Stasjonsid': rad[1],
                'Dato': datetime.strptime(rad[2], '%d.%m.%Y').date(),
                'Snodybde': int(rad[3]) if rad[3] != '-' else None,
                'Nedbor': float(rad[4].replace(',', '.')) if rad[4] != '-' else None,
                'Middeltemperatur': float(rad[5].replace(',', '.')) if rad[5] != '-' else None,
                'Skydekke': int(float(rad[6].replace(',', '.'))) if rad[6] != '-' else None,
                'Middelvind': float(rad[7].replace(',', '.')) if rad[7] != '-' else None
            }
            vaerdata.append(stasjon)

    return vaerdata

if __name__ == "__main__":
    vaerdata = les_vaerdata('snoedybder_vaer_en_stasjon_dogn.csv')

    for dag in vaerdata:
        print(dag)
