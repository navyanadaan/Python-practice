maths= float(input("enter maths score: "))
science= float(input("enter science score: "))
SST= float(input("enter SST score: "))
english= float(input("enter english score: "))
hindi= float(input("enter hindi score: "))
total= (maths+science+english+SST+hindi)


if total/500*100>= 75 or (maths+SST+science)/300*100>=75:
    print("you are eligible for admission") 
else:
    print("you are not eligible for admission ")
