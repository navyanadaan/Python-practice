import random
a = 1

while a <= 5:
    print(a)
    a+=1

n = int(input("Enter a number: "))
ctr =  1
sum_even = sum_odd = 0
while ctr <= n:
    if ctr%2 == 0:
        sum_even += ctr
    else:
        sum_odd += ctr
    ctr += 1

print("Sum of even numbers: ", sum_even)
print("Sum of odd numbers: ", sum_odd)

num = random.randint(10, 50)
ctr = 0

while ctr < 5:
    guess = int(input("Enter a number: "))
    if guess == num:
        print("You guessed it right!")
        break
    else:
        print("Try again!")
    ctr += 1

if not ctr < 5:
    print("\nYou lose the number was " + str(num))

a = b = c = 0

for i in range(0, 3):
    print("Enter 2 numbers")
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    if b==0:
        print("\nThe Denominator cannot be zero. Enter again!")
        continue
    else:
        c = a//b
        print("\nThe Quotient is: ", c)