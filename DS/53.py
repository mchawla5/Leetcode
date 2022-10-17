'''
FIND SUBARRAY WITH GREATEST SUM

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

SOLUTION:
Method 1 (using back tracking)          Run Time: 936ms
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
Method 2 (Kadane's Algo)                Run Time: 1201ms
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
Method 3 (Alternate Kadane)             Run Time: 1653ms
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
Method 4 (optimized alternate Kadane)   Run Time: 715ms
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
Method 5 (Greedy)                       Run Time: 2008ms
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
'''

def subArrayM1(nums):
    max_val_so_far = nums[0]
    max_value = nums[0]
    for i in range(1, len(nums)):
        max_val_so_far = max(max_val_so_far + nums[i], nums[i])
        max_value = max(max_val_so_far, max_value)
    return(max_value)

def subArrayM2(nums):
    max_val_so_far = 0
    max_value = nums[0]
    for num in nums:
        max_val_so_far = max(max_val_so_far, 0) + num
        max_value = max(max_value, max_val_so_far)
    return(max_value)

def subArrayM3(nums):
    max_val_so_far = 0
    max_val = nums[0]
    for num in nums:
        if max_val_so_far < 0:
            max_val_so_far = 0
        max_val_so_far += num
        max_val = max(max_val_so_far, max_val)
    return(max_val)

def subArrayM4(nums):
    max_val_so_far = nums[0]
    max_val = nums[0]
    for i in range(1, len(nums)):
        if max_val_so_far < 0:
            max_val_so_far = 0
        max_val_so_far += nums[i]
        max_val = max(max_val_so_far, max_val)
    return(max_val)

def subArrayM5(nums):
    if max(nums)<0:
        return max(nums)
    max_val_so_far, max_val = 0,0
    for num in nums:
        max_val_so_far = max(0, max_val_so_far + num)
        max_val = max(max_val_so_far, max_val)
    return max_val


if __name__=="__main__":
    nums_1 = [-2,1,-3,4,-1,2,1,-5,4]
    nums_2 = [-2,-1]
    method = int(input("Select the method to run: 1. DP   2. Kadane's Algo   3. Alternate Kadane    4. Optimized Alternate Kadane   5. Greedy\n"))
    if method == 1:
        print(subArrayM1(nums_1) == 6)
        print(subArrayM1(nums_2) == -1)
    elif method == 2:
        print(subArrayM2(nums_1) == 6)
        print(subArrayM2(nums_2) == -1)
    elif method == 3:
        print(subArrayM3(nums_1) == 6)
        print(subArrayM3(nums_2) == -1)
    elif method == 4:
        print(subArrayM4(nums_1) == 6)
        print(subArrayM4(nums_2) == -1)
    elif method == 5:
        print(subArrayM5(nums_1) == 6)
        print(subArrayM5(nums_2) == -1)
    else:
        print("No method selected")
    
    