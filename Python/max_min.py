def MaxMinDifference(nums):
    """
    nums: List[int]
    Returns: int
    """
    maximum=max(nums)
    minimum=min(nums)
    return maximum-minimum
    pass

nums=list(map(int,input("Enter the List Of Numbers: ").split()))
print(MaxMinDifference(nums))