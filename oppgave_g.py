"""
Skriv en funksjon som regner ut hva trenden i et datasett er. Datasettet skal bestå av to
lister, ei liste med x-koordinater og ei liste med y-koordinater. Elementene på samme indeks
i de to listene hører sammen. Trenden skal beregnes som to tall a og b, som skal fungere som
parametere i en lineær formel: verdi = ax + b. Implementer følgende formler, hvor n er til
men ikke med lengden til lista, xi er i-ende element i lista x, og 𝑥 er gjennomsnittet av alle
verdiene i lista x. Merk at disse formlene og hvorfor de ser slik ut er pensum i emnet STA100,
temaet lineær regresjon, minste kvadraters metode.
𝑎 = ∑ (𝑥𝑖 − 𝑥)(𝑦𝑖 − 𝑦)𝑛
𝑖=0
∑ (𝑥𝑖 − 𝑥)2𝑛
𝑖=0
𝑏 = 𝑦 − 𝑎 ∗ 𝑥
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

# Eksempel på bruk av funksjonen
x_koordinater = [1, 2, 3, 4, 5]
y_koordinater = [2, 4, 5, 4, 5]

a, b = beregn_lineær_trend(x_koordinater, y_koordinater)
print(f"Trenden er: verdi = {a}x + {b}")



