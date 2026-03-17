num=int(input("Enter the Number: "))
count=0
while num>0:
    last_digit=num%10 # x%10 returns last digits 
    count+=1 # we are incrementing count for every ld
    num=num//10 # x//10 removes the last digit
print(count)