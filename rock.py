import random
choice1=["rock","paper","scissor"]
while True:
    a=0
    b=0
    ch=int(input("Do u want to cntinue\n 1:Yes\n 2:No"))
    print("Enter two players player1 and player2")
    if ch==1:
        for i in range(1,6):
            player1=int(input("Enter ur choice\n 1 rock \n 2 paper \n 3 scissor"))
            if player1==1:
                choice2="rock"
            elif player1==2:
                choice2="paper"
            else:
                choice2="scissor"
            player2=random.choice(choice1)
            if (player2==choice2):
                print("Player1",choice2)
                print("Player2",player2)
                print("Draw")
                a+=1
                b+=1
            elif (player2=="scissor" and choice2=="paper") or (player2=="rock" and choice2=="scissor") or(player2=="paper" and choice2=="rock"):
                print("Player1 choice",choice2)
                print("Player2",player2)
                print("Player2  won")
                b+=1
            else:
                print("player1 ",choice2)
                print("Player2",player2)
                print("Player1 won")
                a+=1
        if a==b:
            print("It's draw!!!")
            print("plyer1 score",a)
            print("player2 score",b)
        elif a>b:
            print("Player1 won!!!")
            print("plyer1 score",a)
            print("player2 score",b)
        else:
            print("Player2 won!!!")
            print("plyer1 score",a)
            print("player2 score",b)
    else:
        break
 