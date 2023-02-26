
line = str(input("Enter a line: "))
lowercount = uppercount = digitcount = 0
for a in line:
    if a.islower():
        lowercount = 1
    elif a.isupper():
        uppercount = 1
    elif a.isdigit():
        digitcount = 1
print("Lowercase: ", lowercount)
print("Uppercase: ", uppercount)
print("Digits: ", digitcount)


name = 'Andrew Roberts'

for ch in name:
    print(ch," ", end ="")
    
print("\n")

#reverse
length = len(name)

for ch in range(-1, (-length-1), -1):
    print(name[ch])

print("\n")


#pattern

ptn = "<3"

for a in range (1,16):
    print(ptn*a)

print("\n")

