# Traversing a string
name = 'Navya'

for ch in name:
    print(ch," ", end ="")
    
print("\n")

# Reverse a string

length = len(name)

for ch in range(-1, (-length-1), -1):
    print(name[ch])

print("\n")

# String Operations
surname = "Nadaan"

print(name + " " + surname)

print(name*3)

print("\n")

ptn = "#"

for a in range (1,11):
    print(ptn*a)

print("\n")

# Membership Operator

FullName = name + " " + surname

print(name in FullName)
print(name not in FullName)

print("\n")

# Comparison Operators
## 0 - 9 = 48 - 57
## A - Z = 65 - 90
## a - z = 97 - 122
print(name == surname)
print(name != surname)
print("ABC" == "abc")
print("abc" != "ABC")
print("abc" > "ABC")
print("AB" > "ABC")
print("abcd" < "abcD")
print(ord("A"))
print(chr(65))

print("\n")

# String Slicing

FirstName = FullName[0:5]
print(FirstName)

LastName = FullName[6:13]
print(LastName)

fullname = FirstName[0:5] + " " + LastName[0:6]
print(fullname)

print("Hello " + fullname[0:13:2])

# String Methods

print(fullname.capitalize())
print(fullname.upper())
print(fullname.lower())

print("\n")

line = str(input("Enter a line: "))
lowercount = uppercount = digitcount = alphacount = 0
for a in line:
    if a.islower():
        lowercount += 1
    elif a.isupper():
        uppercount += 1
    elif a.isdigit():
        digitcount += 1
    elif a.isalpha():
        alphacount += 1
print("Lowercase: ", lowercount)
print("Uppercase: ", uppercount)
print("Digits: ", digitcount)
print("Alphabets: ", alphacount)