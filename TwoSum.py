#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []

# print(twoSum([2, 7, 11, 15], 9))

########################################################33

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if val in d:
            return [d[val], i]
        d[nums[i]] = i
    return []

print(twoSum([2, 7, 11, 15], 9))