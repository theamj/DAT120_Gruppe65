# Oppgave f) Lag en funksjon som tar inn ei liste med tall. 
# Funksjonen skal finne og returnere lengden til den lengste sammenhengende sekvensen av 0-ere i lista.

def zero_sequence(list):

    sequence_size = 0
    largest_sequence = 0

    for i in list:
        if( i == 0 ):
            sequence_size += 1
        if( sequence_size > largest_sequence ):
            largest_sequence = sequence_size
        if( i != 0 ):
            sequence_size = 0
    
    return largest_sequence # goofed a little in git lol

# list = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] # quick test for the code
# print(zero_sequence(list))