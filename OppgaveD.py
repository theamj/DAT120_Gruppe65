#Skriv en funksjon som tar inn ei liste med flyttall og en enkeltverdi. 
#Funksjonen skal telle antall elementer i lista som er større enn eller 
#lik den oppgitte verdien og returnere dette.
#Definerer funksjonen med to arrgumenter. 
def tell_større_eller_lik_verdi(liste,verdi):
    antall_større_eller_like = 0 


    for element in liste :    #går igjennom hver element i listen 
        if element >= verdi :   # ser om elementet er større eller lik min verdi.
            antall_større_eller_like += 1 #hvis dette er sant økes antall_større_eller_like med 1.
    return antall_større_eller_like

#Eksempel på en liste. 
min_liste = [1.5, 6.4, 4.0, 3.5, 9.2, 4.5, 1.2, 3.6]
#velger en verdi funksjonen skal sammenligne elementene i listen med. 
min_verdi = 4.9

resultat = tell_større_eller_lik_verdi(min_liste,min_verdi) #bruker funksjonen til å telle antall elementer som er større eller lik min verdi.

print(f"Antall elementer som er større eller lik {min_verdi} er {resultat}")
