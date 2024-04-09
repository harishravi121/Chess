import random
import time


A=['A','B','C','D','E','F','G','H']
N=['1','2','3','4','5','6','7','8']
print('The computer calculates best move but gives human like delay')
while 1:
    move=random.choice(A)+random.choice(N) # replace with computer algo or with player
    time.sleep(2+random.random()*2)
    print(move)
    move=random.choice(A)+random.choice(N)
    time.sleep(2+random.random()*2)
    print(move)
    print()
    
