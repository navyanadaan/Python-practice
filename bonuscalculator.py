name= str(input("enter your name "))
age= int(input("\nenter your age "))
salary= float(input("\nenter your salary "))

if salary >= 200000:
    bonus =50000
    total= salary + bonus
    print("name: " +str(name))
    print("age: " + str(age))
    print("salary: " + str(salary))
    print("bonus: " + str(bonus))
    print("TOTAL===" + str(total))
elif salary >= 150000:
    bonus = salary*12/100
    total= salary + bonus
    print("name: " +str(name))
    print("age: " + str(age))
    print("salary: " + str(salary))
    print("bonus: " + str(bonus))
    print("TOTAL===" + str(total))
elif salary >= 100000:
    bonus= salary*8/100
    total= salary + bonus
    print("name: " +str(name))
    print("age: " + str(age))
    print("salary: " + str(salary))
    print("bonus: " + str(bonus))
    print("TOTAL===" + str(total))
elif salary >= 70000:
    bonus= salary*5/100
    total= salary + bonus
    print("name: " +str(name))
    print("age: " + str(age))
    print("salary: " + str(salary))
    print("bonus: " + str(bonus))
    print("TOTAL===" + str(total))
else: 
    bonus= 5000
    total= salary + bonus
    print("name: " +str(name))
    print("age: " + str(age))
    print("salary: " + str(salary))
    print("bonus: " + str(bonus))
    print("TOTAL===" + str(total))


