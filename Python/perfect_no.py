n=int(input("Enter Any Number: "))
divisors=[]
for i in range(1,n):
    if n%i==0:
            divisors.append(i)
# print(divisors)
total=sum(divisors)
if total==n:
    print(f"{n} is Perfect Number")
else:
    print(f"{n} is not a perfect number")