#list = [15,6,13,22,3,52,2]
#print("List before sorting: ", list)

#n = len(list)

#for i in range(n):
#    for j in range(0, n-i-1):
#        if list[j] > list[j+1] :
#            list[j], list[j+1] = list[j+1], list[j]

#print("List after sorting: ", list)



#homework
list = [10,42,34,68,9,23,14]
print("list before sorting:" , list)

n=len(list)

for i in range(n):
    for j in range(0, n-i-1):
        if list[j] > list[j+1] :
            list[j], list[j+1] = list[j+1], list[j]

print("List after sorting: ", list)