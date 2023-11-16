# Oppgave f) Lag en funksjon som tar inn ei liste med tall. 
# Funksjonen skal finne og returnere lengden til den lengste sammenhengende sekvensen av 0-ere i lista.

def match_number_sequence(list, match = 0):

    sequence_size = 0
    largest_sequence = 0

    for i in list:
        if( i == match ):
            sequence_size += 1
        else:
            sequence_size = 0
        if( sequence_size > largest_sequence ):
            largest_sequence = sequence_size
    
    return largest_sequence


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

if __name__ == "__main__": # Forgot this feature existed, thanks Ida!

    import random

    # Testing ! this one creates a list of random numbers between -1.0 and 1.0
    # Then the match_float_sequence() function is tested on the list with a margin of 0.5 

    def randlist(size, min = -1.0, max = 1.0):
        list = []

        for i in range(size):
            rnum = random.uniform(min, max)
            list.append(rnum)

        return list

    test_list = [4, 4, 4, 4, 4, 1, 1, 1, 1, 0, 0, 0, 0] # quick test for f) and optional-a
    float_list = randlist(20)
    margin = 0.5

    print(f"Largest sequence of zeros: {match_number_sequence(test_list)}")
    print(f"Largest sequence of equal numbers: {match_sequence(test_list)}")
    print(f"Float list function test results with margin {margin}: {match_float_sequence(float_list, margin)}")
