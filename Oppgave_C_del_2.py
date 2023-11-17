import csv

def beregn_lineær_trend(x_koordinater, y_koordinater):
    # Beregn gjennomsnittet av x- og y-verdiene
    gjennomsnitt_x = sum(x_koordinater) / len(x_koordinater)
    gjennomsnitt_y = sum(y_koordinater) / len(y_koordinater)

    # Beregn a ved hjelp av formelen for a
    a_numerator = sum((x - gjennomsnitt_x) * (y - gjennomsnitt_y) for x, y in zip(x_koordinater, y_koordinater))
    a_denominator = sum((x - gjennomsnitt_x) ** 2 for x in x_koordinater)
    a = a_numerator / a_denominator

    # Beregn b ved hjelp av formelen for b
    b = gjennomsnitt_y - a * gjennomsnitt_x

    return a, b

def les_data(filnavn):
    x_koordinater = []
    y_koordinater = []

    with open(filnavn, newline='') as csvfile:
        leser = csv.reader(csvfile, delimiter=',')
        next(leser)  

        for rad in leser:
            try:
                x_koordinater.append(int(rad[0]))  
                y_koordinater.append(int(rad[1]))  
            except (ValueError, IndexError) as e:
                print(f"Feil i raden {rad}: {e}")

    return x_koordinater, y_koordinater


filnavn = 'snoedybder_vaer_en_stasjon_dogn.csv'
x_koordinater, y_koordinater = les_data(filnavn)


print("x_koordinater:", x_koordinater)
print("y_koordinater:", y_koordinater)


a, b = beregn_lineær_trend(x_koordinater, y_koordinater)


print(f"Trenden er: antall_dager = {a} * år + {b}")
