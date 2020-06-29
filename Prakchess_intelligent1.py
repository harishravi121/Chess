
import random

chessboard=[[  5.2,   3.4 ,  3.5,   9.1 ,  10.1,    3.6 ,  3.7 ,  5.4],
 [  1.10  ,  1.10  , 1.10,    1.10,    1.10,    1.10,   1.10,    1.10 ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  0.00  ,   0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00 ,    0.00,     0.00  ],
 [  1.00,     1.00,    1.00,     1.00,     1.00,     1.00,     1.00,    1.00,  ],
 [  5.0,     3.0,   3.1 , 9.00  , 10.00,     3.2 , 3.3 ,  5.1],
            [  'A',     'B',  'C' , 'D'  ,' E',   ' F' ,'G' ,  'H']];
print('Standard chess notation white being bottom and black with 0.1 at top')
for i in range(0,9):
    print(chessboard[i])


#The computing engine should have the rules and then calculate from the other person's perspective and then do the best move with say 9 calculations
PNG='d4Nf6Nc3d5Bg5Bf5e3e6...'
PGNmidgame='Qd7cxd4exd4Bb4Bxf5Bxc3+bxc3'
PGNmidgame2='Rac1Nb4Nf4Qxf6Rg8dxc5Qe6+fxe6'
PGNendgame='Ka8NC7Rxc7Rxc7Rf8Qd7Rf1+Kxf1Qf4+Ke1Qf4+kg1,Qe3 Nc7+Kd8Nge6#'

#Need to make an array of 40 previous positions and next positions and linking with symbol and seeing legal moves for each position'

P1='A2'

def allowedP1():
    global P1new
    P1new=[]
    P1new.append(P1[0]+str(int(P1[1])+1))
    if(int(P1[1])==2):
        P1new.append(P1[0]+str(int(P1[1])+2))
    print(P1new)

def updatepiece(move):
    global P1
    if(P1==move[0]+move[1]):
        P1=move[2]+move[3]
        print(P1)









haha=1;
while haha:

    #c=random.sample(['A','B','C','D','E','F','G','H'],2);
    #d=random.sample(range(1,8),2);

    #move=c[0]+str(d[0])+c[1]+str(d[1])
    move=input()
    illegal=0
    if(chessboard[8-int(move[1])][ord(move[0])-65]!=0):
        flag=1
        print(move)
        if(chessboard[8-int(move[1])][ord(move[0])-65]==1.00):
            if(int(move[3])-int(move[1])==1):
                   print('Legal')
            if(int(move[3])-int(move[1])>=3):
                   print('Illegal')
                   illegal=1
        if(illegal==0):
                
            chessboard[8-int(move[3])][ord(move[2])-65]=chessboard[8-int(move[1])][ord(move[0])-65]
            chessboard[8-int(move[1])][ord(move[0])-65]=0;
            
            allowedP1()
            updatepiece(move)
        for i in range(0,9):
            print(chessboard[i])
        print('')
    
        for i in range(0,10000):
            for j in range(0,5000):
                1
        
#Put example demo of how to play the game or even you can't play it
