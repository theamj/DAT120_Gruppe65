#Fila «lister_for_del_1.py» er delt ut sammen med denne øvingen. 
#Bruk funksjonen fra oppgave d) på lista «temperaturer» fra denne fila. 
#Anta at hvert innslag er maksimaltemperaturen for en dag. 
#Finn antall sommerdager (over 20), høysommerdager (over 25) og tropedager (over 30).


def tell_større_eller_lik_verdi (liste, verdi):
    antall_større_eller_lik = 0 
    for element in liste: 
        if element >= verdi :
            antall_større_eller_lik += 1
    return antall_større_eller_lik

tempraturer = [-5, 2, 6, 13, 9, 22, 28, 19, 24, 12, 5, 1, -3, -8, 2, 8, 15, 18, 21, 26, 21, 31, 15, 4, 1, -2]

antall_sommerdager = tell_større_eller_lik_verdi(tempraturer,20)

antall_høysommerdager = tell_større_eller_lik_verdi(tempraturer,25)

antall_tropedager = tell_større_eller_lik_verdi(tempraturer,30)


print(f"Antall sommerdager over 20 grader er {antall_sommerdager}")
print(f"Antall høy sommerdager som er over 25 grader er {antall_høysommerdager}")
print(f"Antall tropedager som er over 30 grader er {antall_tropedager}")
