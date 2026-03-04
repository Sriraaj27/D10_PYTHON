year=int(input('Enter the year : '))

if year%400==0:
    print(f"{year} is a Leap Year")
elif year%100==0:
    print(f"{year} is Not a Leap Year")
elif year%4==0:
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")