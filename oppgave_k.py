"""
Bruk funksjonen fra oppgave g) for å finne trenden i temperaturlista. For å finne trenden
bruker dere lista «temperaturer_tidspunkter» som x-koordinater og lista «temperaturer»
som y-koordinater. Skriv ut om trenden er stigende eller synkende. Trenden er stigende hvis
a er positiv, synkende hvis a er negativ og det er ingen trend hvis a er 0.
"""



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

temperaturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]
temperaturer_tidspunkter = list()
for index in range(len(temperaturer)):
    temperaturer_tidspunkter.append(index)

a, b = beregn_lineær_trend(temperaturer_tidspunkter, temperaturer)
print(f"Trenden er: verdi = {a}x + {b}")
if a == 0 print("Det er ingen trend i dette datasettet.")
elif a < 0 print("Trenden er synkende.")
else:
    print("Trenden er økende")