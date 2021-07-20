import random
comp=random.randint(1,3)
if comp==1:
    comp='s'
elif comp==2:
    comp='p'
else:
    comp='sc'
print("WELCOME TO THIS GAME ! HOPE YOU WILL ENJOY THIS GAME")
ch=input("Do you want to continue this game Y/N: \n").casefold()
while ch!='n':
    if ch=='y':
        count_you=0
        count_comp=0
        name=input("Enter Your Name \n")
        n=int(input("Enter the number of times you want to play this game: \n"))
        for i in range(n):
            print("Computer Turn: Stone(s) Paper(p) amd Scissors(sc)")
            a=input("Your Turn: Stone(s) Paper(p) amd Scissors(sc)\n")
            if a=='s' or a=='p' or a=='sc':
                def Game_Win(comp,you):
                    if comp==you:
                        return None
                    elif comp=='s' and a=='p':
                        return True
                    elif comp=='s' and a=='sc':
                        return False
                    elif comp=='p' and a=='sc':
                        return True
                    elif comp=='p' and a=='s':
                        return False
                    elif comp=='sc' and a=='s':
                        return True
                    elif comp=='sc' and a=='p':
                        return False
                g=Game_Win(comp,a)

                print("Your Turn",a)
                print("Computer Turn:",comp)
    
                if g==None:
                    print("Game Tie")
                elif g==True:
                    print("You Win!")
                    count_you=count_you+1
                else:
                    print("You Loose!")
                    count_comp=count_comp+1
            else:
                print("Invalid Choice")

        if count_you>count_comp:
            print(f"Finally {name} win")
            print(f"Out of {n} time {name} win {count_you} times and Computer win {count_comp} times")
        elif count_you<count_comp:
            print("Finally Computer win")
            print(f"Out of {n} time Computer win {count_comp} times and {name} win {count_you} times")
        elif count_you==count_you:
            print("Finally The Game is Tie")
            print(f"Out of {n} times {name} win {count_you} times and Computer Win {count_comp} times")
        ch=input("Do You want to continue this Game: Y/N") 
    else:
        print("Invalid Choice.")
        break   
else:
    print("You are exit from this game")

