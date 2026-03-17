nums=list(map(int,input("Enter the List of Numbers: ").split()))
threeshould=int(input("Enter Threeshould Value: "))
result=[]
for i in nums:
    if i>threeshould:
        result.append(i)
print(f"List Elemenst that are Greater than Threeshould are: {result}")
