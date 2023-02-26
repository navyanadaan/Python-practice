var1= float(input("enter your number "))
var2= float(input("\nenter your number "))
function= str(input("\naddition(A), subtraction(S), multiplication(M), division(D) "))

if function== str("A") or function== str("addition"):
    var3= var1 + var2
    print("solution= " + str(var3))
elif function== str("S") or function== str("subtraction"):
    var3= var1 - var2
    print("solution= " + str(var3))
elif function== str("M") or function== str("multiplication"):
    var3= var1 * var2
    print("solution= " + str(var3))
elif function== str("D") or function== str("division"):
    var3= var1 / var2
    print("solution= " + str(var3))
else: 
    print("invalid input")
