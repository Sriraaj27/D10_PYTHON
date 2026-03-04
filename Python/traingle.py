l,b,h=map(int,input("Enter Length, Breadth and Height: ").split())

if l+b+h==180:
    print("We can Form a Traingle")
    if l==b==h:
        print("Equilateral Triangle")
    elif l==b or b==h or h==l:
        print("Isosceles Traingle")
    else:
        print("Scalene Triangle")
else:
    print("We cannot Form a Triangle")