a=2
b=4
c=7 

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
elif a>c:
    print("a is greater than c")
elif a==c:
    print("a is equal to c")
elif a<b:
    print("a is smaller than b")
elif a<c:
    print("a is smaller than c")
elif b>c: 
    print("b is greater than c")
elif b<c:
    print("b is smaller than c")
elif b==c:
    print("b is equal to c")
elif a>b>c:
    print("a is greater than b and c")
elif a<b<c:
    print("a is smaller than b and c")
elif a==b==c:
    print("a is equal to b and c")
else:
    print("a is neither equal to b nor c")


# Data Types

## Numbers:

### Integers
print("\nInteger Data Type:")

number = 23

print(type(number))

### Booleans
print("\nBoolean Data Type:")

boolean = bool(1)

print(type(boolean))

## Floating Point Numbers:

### Fractions
print("\nFraction Data Type:")

fraction = 1/3

print(type(fraction))

### Exponential
print("\nExponential Data Type:")

exponential = 1e-3

print(type(exponential))

## Complex Numbers:
print("\nComplex Data Type:")

complex = 1 + 2j

print(type(complex))

print("\nReal Part: " + str(complex.real))
print("\nImaginary Part: " + str(complex.imag))

## Strings:
print("\nString Data Type:")

string = "Hello World"

print(type(string))

## String Sequences:
print("\nString Sequences:")

string = "Hello"

print("String at index 0 is " + string[0])

print("\nString Length is " + str(len(string)))

## Lists:
print("\nList Data Type:")

list = [10, 20, 30, 40, 50]

print(type(list))

print("\nList Length is " + str(len(list)))

print("\nList is : " + str(list))

list[2] = 38

print("\nList is : " + str(list))

## Tuples:
print("\nTuple Data Type:")

tuple = (10, 20, 30, 40, 50)

print(type(tuple))

print("\nTuple Length is " + str(len(tuple)))

print("\nTuple at index 4 = " + str(tuple[4]))

## Dictionaries:
print("\nDictionary Data Type:")

dictionary = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty"}

print(type(dictionary))

print("\nDictionary Length is " + str(len(dictionary)))

print("\nDictionary at index 30 = " + str(dictionary[30]))

print("\nDictionary Keys are : " + str(dictionary.keys()))

print("\nDictionary Values are : " + str(dictionary.values()))





list= [5,15,25,35,45,55,65,75]

print(type(list))

print("\nList Length is " + str(len(list)))



list[5] = 37

print("\nList is : " + str(list)) 



tuple = (7, 14, 21, 28, 35, 42, 50)
print(type(tuple))

print("\ntuple length is " + str(len(tuple)))

print("\ntuple at index 6 is "  + str(tuple[6]) )

tuple[4] = 32

print("\n tuple is " + str(len(tuple)))




