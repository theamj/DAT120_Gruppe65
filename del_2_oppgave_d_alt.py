#%%

import pylab
from Oppgave_B_Del_2 import dager_skifoere
from del_2_oppgave_c_alt import skifore_trend

skisesong = dager_skifoere()
sesong = []
for i in skisesong[1]:
    sesong.append(i[0])
pylab.plot(sesong, dager_skifoere()[0])

# %%
