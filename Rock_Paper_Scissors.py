import random
def main():
    Rock=0
    Paper=1
    Scissors=2
    List_obj=["Rock","Paper","Scissors"]
    Bot_Tally=0
    Player_Tally=0
    Draw_Tally=0
    while True:
        print("Enter an Choice(Rock[0], Paper[1], Scissors[2])=")
        choice=int(input())
        computer=random.randint(0,2)
        print(f"You have Chosen {List_obj[choice]} and The Bot has Chosen {List_obj[computer]}")
        if (choice is Rock and computer is Rock) or (choice is Paper and computer is Paper) or (choice is Scissors and computer is Scissors):
            print("Match Tied")
            Draw_Tally+=1
        elif (choice is Rock and computer is Paper) or (choice is Paper and computer is Scissors) or (choice is Scissors and computer is Rock):
            print("The Bot Wins")
            Bot_Tally+=1
        elif (choice is Scissors and computer is Paper) or (choice is Rock and computer is Scissors) or (choice is Paper and computer is Rock):
            print("You Win")
            Player_Tally+=1
        print("Want to Continue Playing(Y/N)=")
        conplaying=input()
        if conplaying == 'Y' or conplaying == 'y':
            continue
        elif conplaying == 'N' or conplaying == 'n':
            break
    print("Final Score:")
    print("The Player Score is ", Player_Tally)
    print("The Bot Tally is ", Bot_Tally)
    print("The Total Number of Draws is ",Draw_Tally)
    
main()