a=1


while a<=180:
    print("Enter 3 numbers")
    a = int(input("Enter 1st angle: "))
    b = int(input("Enter 2nd angle: "))
    c = int(input("Enter 3rd angle: "))
    if a==0:
        print("\nThe angle cannot be zero. Enter again!")
        continue
    if b==0:
        print("\nThe angle cannot be zero. Enter again!")
        continue
    if c==0:
        print("\nThe angle cannot be zero. Enter again!")
        continue
    elif a+b+c==180:
        print("\nyes it is a triangle " )
        break
    else:
        print("\nno it is not a triangle ")
        break




#new

line = str(input("Enter a line: "))
lowercount = uppercount = digitcount = 0
for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
print("Lowercase: ", lowercount)
print("Uppercase: ", uppercount)
print("Digits: ", digitcount)
