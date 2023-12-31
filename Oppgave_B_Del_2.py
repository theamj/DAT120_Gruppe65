import csv
from datetime import datetime

def tell_større_eller_lik_verdi(liste, verdi):
    antall_større_eller_like = 0 

    for element in liste:
        if element >= verdi:
            antall_større_eller_like += 1

    return antall_større_eller_like

def dager_skifoere():
    skiføre_data = []

    with open('snoedybder_vaer_en_stasjon_dogn.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)  

        for row in reader:
            dato_str = row[2]

            
            if dato_str:
                try:
                    dato = datetime.strptime(dato_str, '%d.%m.%Y')
                    snødybde = row[3]

                    
                    try:
                        snødybde = float(snødybde)
                    except ValueError:
                        continue 

                    skiføre_data.append((dato, snødybde))

                except ValueError:
                    continue  

    vintersesonger = {}

    for dato, snødybde in skiføre_data:
        år = dato.year
        måned = dato.month

        if måned >= 10:  
            sesong_start_år = år
        else:
            sesong_start_år = år - 1

        sesong_key = (sesong_start_år, sesong_start_år + 1)
        
        if sesong_key not in vintersesonger:
            vintersesonger[sesong_key] = []

        vintersesonger[sesong_key].append(snødybde)
        
    antall_dager_med_skiføre = []
    sesong_list = []
    for sesong_key, snødybder in vintersesonger.items():
        sesong_list.append(sesong_key)
        antall_dager_med_skiføre.append(tell_større_eller_lik_verdi(snødybder, 20))

    return antall_dager_med_skiføre, sesong_list

if __name__ == "__main__":
    indata = dager_skifoere()
    i = 0
    for dager in indata[0]:
        print(f"Antall dager med skiføre i sesong {indata[1][i]}: {dager}")
        i += 1