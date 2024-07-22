import random
p1,p2,temp,flag,Final_flag=0,0,0,0,0
def roll():
        temp=random.randint(1,5)
        return temp
def game():
    global p1,flag,Final_flag
    temp=0
    print("It's player one's Turn")
    while(input()!="N"):
        I=roll()
        temp+=I
        print("You rolled ",I,"Total:",temp+p1)
        if I==0:
             print("Turn Over")
             flag=1
             break
        else:
             print("Do you want to continue?")
    if flag==0:
        p1+=temp
    flag=0
    temp=0   
    print("Player One Grand Total:",p1)
    if p1>20:
         print("Player one wins")
         Final_flag=1
def game2():
    global p2,flag,Final_flag
    temp=0
    print("It's player two's Turn")
    while(input()!="N"):
        I=roll()
        temp+=I
        print("You rolled ",I,"Total:",temp+p2)
        if I==0:
             print("Turn Over")
             flag=1
             break
        else:
             print("Do you want to continue?")
    if flag==0:
        p2+=temp
    flag=0
    temp=0   
    print("Player Two Grand Total:",p2)
    if p2>20:
         print("Player two wins")
         Final_flag=1

print("Do you want to play?")
print("Yes/No")
Choice=input()
if Choice=="Yes" or Choice=="yes" or Choice=="YES":
    print("Welcome to the game")
    while(Final_flag==0):
        game()
        if Final_flag==0:
            game2()  
            print("Player one has",p1,"Player two has",p2)

    print("Player one has",p1,"Player two has",p2)
else:
    print("Goodbye")