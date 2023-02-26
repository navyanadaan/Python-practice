#finding a prime number

number= int(input("\nenter a number "))
if number==1 or number<1:
    print("\nnumber can't be smaller than or equal to 1. Enter again! ")
if number>1:
    for i in range(2,number):
        if number%i ==0:
            print(number," it is not a prime number")
            break
        else:
            print(number," is a prime number")
            break