"""
Bruk funksjonen fra oppgave f) på den oppgitte lista «døgn-nedbør» for å finne den lengste
perioden uten nedbør
"""

from oppgave_f import match_zero_sequence as sequence
import lister_for_del_1 as lists

report = lists.dogn_nedbor
print(sequence(report))
