name= str(input("enter your name "))
age= int(input("\nenter your age "))
function= str(input("\nenter your region:- chandigarh(C), panchkula(P), mohali(M) "))

if age >=18 and (function== str("chandigarh") or function== str("C")):
    print("\nYOU ARE ELIGIBLE TO VOTE ")
    print("\nyour voting booth is sector 17 chandigarh ")
elif age >=18 and (function== str("panchkula ") or function== str("P")):
    print("\nYOU ARE ELIGIBLE TO VOTE ")
    print("\nyour voting booth is sector 21 panchkula ")
elif age >=18 and (function== str("mohali ") or function== str("M")):
    print("\nYOU ARE ELIGIBLE TO VOTE ")
    print("\nyour voting booth is sector 105 mohali ")
else:
    print("\nYOU ARE NOT ELIGIBLE TO VOTE")
