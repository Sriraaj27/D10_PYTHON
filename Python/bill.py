units=int(input("Enter the no.of units consumed: "))
bill=0

if units<=100:
    bill = units * 2
    print(f"Electricity Bill--> {bill}")
elif units<=200:
    first_100=100*2
    second_100 = (units - 100) * 3
    bill=first_100+second_100
    print(f"Electricity Bill--> {bill}")
else:
    first_100=100*2
    second_100=100*3
    after_200=(units-200)*5
    bill=first_100+second_100+after_200
    print(f"Electricity Bill--> {bill}")