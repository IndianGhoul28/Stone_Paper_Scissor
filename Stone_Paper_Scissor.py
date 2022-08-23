import random

def game2 (comp,you):
    if (comp==you):
        return None
    elif (comp=="s"):
        if (you == "sc"):
            return False
        elif (you == "p"):
            return True
        
    elif (comp=="p"):
        if (you == "s"):
            return False
        elif (you == "sc"):
            return True

    elif (comp=="sc"):
        if (you == "p"):
            return False
        elif (you == "s"):
            return True


print("Computer turn: Stone(s), Paper(p), Scissor(sc)")
rand_num = random.randint(1,3)
if (rand_num == 1):
    comp = 's'
elif rand_num==2:
    comp = 'p'
elif rand_num==3:
    comp = 'sc'

you = input("Your turn: Stone(s), Paper(p), Scissor(sc): ")

a = game2(comp, you)
print(comp)
print(you)

if a == None:
    print("It's a tie.")
elif a:
    print('You win')
else:
    print("You loose")



