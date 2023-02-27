import random
number= random.randint(0,101)
tries=0

while tries<5:
    guess=int(input("guess the number "))
    if guess==number:
        print("you have guessed it right ")
        break
    else:
        print("try again ")
    tries+=1
if not tries<5:
    print("you loose the number was:" , number)