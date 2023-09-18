#chess clock

import time
import random

tz=0
Tot=60 #Total time
Tot2=50+random.random()*10 #Total time with a fun variable
tz2=0
tx=time.time()
print(round(Tot-tz,2),round(Tot2-tz2,2),'seconds')

for i in range(50):
    a=input()
    ty=time.time()
    tz+=ty-tx
    print(round(Tot-tz,2),round(Tot2-tz2,2),'seconds') #Printing time
    b=input()
    tx=time.time()
    tz2+=tx-ty
    print(round(Tot-tz,2),round(Tot2-tz2,2),'seconds')
    print(round((2**(tz))*100*random.random(),2),round((2**(tz2))*100*random.random(),2))
