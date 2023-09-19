# Oppgave f) Lag en funksjon som tar inn ei liste med tall. 
# Funksjonen skal finne og returnere lengden til den lengste sammenhengende sekvensen av 0-ere i lista.

def match_zero_sequence(list):

    sequence_size = 0
    largest_sequence = 0

    for i in list:
        if( i == 0 ):
            sequence_size += 1
        else:
            sequence_size = 0
        if( sequence_size > largest_sequence ):
            largest_sequence = sequence_size
    
    return largest_sequence # goofed a little in git lol

# list = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0] # quick test for the code
# print(zero_sequence(list))


# Frivillig a - Ta inn ei liste med heltall. 
# Returner lengden og verdien til den lengste sekvensen av samme verdi.

def match_sequence(list):

    sequence_size = 0
    largest_sequence = 0
    last_number = list[0]

    for i in list:
        if( last_number == i ):
            sequence_size += 1
        else:
            sequence_size = 1

        last_number = i
        if( sequence_size > largest_sequence ):
            largest_sequence = sequence_size
            value = last_number
    
    return largest_sequence, value

# list = [4, 4, 4, 4, 4, 1, 1, 1, 1, 0, 0, 0]
# print(match_sequence(list))


# Frivillig b - Det samme for flyttall, men med en oppgitt toleranse.

def match_float_sequence(list, margin):

    sequence_size = 0
    largest_sequence = 0
    last_number = list[0]
    
    current_sequence = []
    current_min = last_number
    current_max = last_number

    for i in list:
        if( current_max < i ):
            current_max = i
        if( current_min > i ):
            current_min = i

        if ( current_max - current_min < margin ):
            current_sequence.append(i)
            sequence_size += 1
        else:
            current_sequence = [i]
            sequence_size = 1
            current_min = i
            current_max = i

        if( sequence_size > largest_sequence ):
             largest_sequence = sequence_size
             largest_list = current_sequence
             value = i
        last_number = i
    
    return largest_sequence, value, largest_list

# More testing ! this one creates a list of random numbers between -1.0 and 1.0
# Then the float_sequence() function is tested on the list with a margin of 0.5 

""" 
import random

def randlist(size, min = -1.0, max = 1.0):
    list = []

    for i in range(size):
        rnum = random.uniform(min, max)
        list.append(rnum)

    return list

list = randlist(20)
print(float_sequence(list, 0.5))
"""