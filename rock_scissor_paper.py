from random import randint
print("Your Turn")
print("choose:\n r for ROCK    [0]\n p for PAPER   [--]\n s for SCISSOR [8<]")
u = input()
a = randint(1,3)
if a == 1:
    c = 'r'
elif a==2:
    c = 'p'
else:
    c = 's'
if u=='r':
    if c=='r':
        print(" You both chosen ROCK \n Its a DRAW")
    elif c=='p':
        print(" You chosen ROCK \n Computer chosen PAPER \n You Lose")
    elif c=='s':
        print(" You chosen ROCK \n Computer chosen SCISSOR \n You Win")
elif u=='p':
    if c=='p':
        print(" You both chosen PAPER \n Its a DRAW")
    elif c=='r':
        print(" You chosen PAPER \n Computer chosen ROCK \n You Win")
    elif c=='s':
        print(" You chosen PAPER \n Computer chosen SCISSOR \n You Lose")
elif u=='s':
    if c=='s':
        print(" You both chosen SCISSOR \n Its a DRAW")
    elif c=='p':
        print(" You chosen SCISSOR \n Computer chosen PAPER \n You Win")
    elif c=='r':
        print(" You chosen SCISSOR \n Computer chosen ROCK \n You Lose")
