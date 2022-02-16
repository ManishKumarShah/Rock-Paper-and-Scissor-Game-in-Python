# Rock Paper And Scissor Game
import random

def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'Rock':
        if you =='Paper':
            return True
        else:
            return False                 
    elif comp == 'Paper':
        if you =='Scissor':
            return True 
        else:
            return False
    elif comp == 'Scissor':
        if you =='Rock':
            return True
        else:
            return False
           
random = random.randint(1,3)
if random == 1:
    comp = 'Rock'
elif random == 2:
    comp = 'Paper'
elif random  ==3:
    comp='Scissor'         
you = input( "Your Turn : choose ( Rock ,Paper or Scissor) :")
print(f"Computer Choosed :{comp}")
a=gamewin(comp,you)
if a == None :
    print('The game is Tie')
elif a :
    print("****** Hurray !! You win !!********")
else:
    print("***** You Loose !! ***** \n\n -- BETTER LUCK NEXT TIME -- ")
print("\nThanks for Playing !! , Want to PLAY AGAIN !! ")        
