def sum_of_biggest(nums):
    minimum=min(nums)
    result=[]
    for i in nums:
        if i>minimum:
            result.append(i)
    sum_of_numbers=sum(result)    
    return sum_of_numbers
nums = list(map(int, input("Enter the List Of Numbers: ").split()))
print(sum_of_biggest(nums))
