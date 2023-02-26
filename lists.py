# List Manipulation

EmptyList = []
IntegerList = [1,2,3,4,5]
FloatList = [1.0,2.0,3.0,4.0]
CharList = ['a','b','c','d']
StringList = ["Hello","World"]
MixedList = ['a','b','c','d',1,2,3,4,5,1.0,2.0,3.0,4.0]
NestedList = [[1,2,3,4,5],[1.0,2.0,3.0,4.0],['a','b','c','d']]

rollNumbers = eval(input("Enter roll numbers: "))
print(type(rollNumbers))
print(rollNumbers)

a = 5

for a in IntegerList:
    print("5 is in the list")
    break

IntFloatList = IntegerList + FloatList
print(IntFloatList)

for a in IntegerList:
    print(a)

EmptyList.append(5)
EmptyList.append(2)
print(EmptyList)

del EmptyList[0]
print(EmptyList)

IntegerList.pop(3)
print(IntegerList)

list = [1,2,3,4,5,6,7,8,9,10]
list.extend([11,12,13,14,15,16,17,18,19,20])
print(list)

IntegerList.insert(3,1)
print(IntegerList)

print(IntegerList.count(1))

IntegerList.sort(reverse = True)
print(IntegerList)