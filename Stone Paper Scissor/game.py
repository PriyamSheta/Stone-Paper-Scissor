import os

def isWinner(a,b):
    if a==b:
        return None
    else:
        if a=='1':
            if b=='2':
                return False
            else:
                return True
        if a=='2':
            if b=='1':
                return True
            else:
                return False
        if a=='3':
            if b=='1':
                return False
            else:
                return True

dic={"1":"Stone","2":"Paper","3":"Scissor"}
player1=input("Please select one of these: Stone(1) , Paper(2) , Scissor(3)  ")
os.system("cls")
player2=input("Please select one of these: Stone(1) , Paper(2) , Scissor(3)  ")
os.system("cls")
print("Player 1 chose ", dic[player1])
print("Player 2 chose ", dic[player2])

winner=isWinner(player1,player2)

if winner:
    print("Player1 won")
elif winner==False:
    print("Player2 won")
else:
    print("Tie game!!! Well Played")