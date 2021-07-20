import random
# print(randNo)

print("Computer Turn: Sanke(s), Water(w), Gun(g)")
you=input("Your Turn: Sanke(s), Water(w), Gun(g)")

comp=random.randint(1,3)

if comp==1:
    comp='s'
elif comp==2:
    comp='w'
else:
    comp='g'
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='s' and you=='w':
        return False
    elif comp=='s' and you=='g':
        return True
    elif comp=='w' and you=='g':
        return False
    elif comp=='w' and you=='s':
        return True
    elif comp=='g' and you=='s':
        return False
    elif comp=='g' and you=='w':
        return True

g=gamewin(comp,you)

print(f"Your Turn is {you}")
print(f"Computer Turn is {comp}")
if g==None:
    print("The Game is Tie")
elif g:
    print("You Win!")
else:
    print("You Loose")

    