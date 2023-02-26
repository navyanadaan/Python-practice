#rollNumbers = eval(input("Enter roll numbers: "))
#print(type(rollNumbers))
#print(rollNumbers)


IntegerList = [1,2,3,4,5,6,7,8,9,10]
FloatList = [1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
IntFloatList = IntegerList + FloatList
print(IntFloatList)

for a in IntegerList:
    print(a)

EmptyList = []
EmptyList.append(10)
EmptyList.append(3)
EmptyList.append(1)
EmptyList.append(7)
print(EmptyList)

del EmptyList[3]
print(EmptyList)


IntegerList.pop(3)
print(IntegerList)

list = [1,2,3,4,5,6,7,8,9,10]
list.extend([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
print(list)

