'''
TWO SUM

Find the indices of two number that add up to give the target value.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

SOLUTION:
Method 1 (dict)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
Method 2 (efficient dict)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
'''

def twoSumM1(nums, target):
    d = {}
    for i in range(0, len(nums)):
        if nums[i] not in d:
            d[nums[i]] = [i]
        else:
            if i != d[nums[i]]:
                d[nums[i]].append(i)

        diff = target - nums[i]
        if (diff in d) and (i != d[diff][0]):
            return (i, d[diff][0])

def twoSumM2(nums, target):
    d = {}
    for i in range(0, len(nums)):
        if nums[i] in d:
            return (d[nums[i]], i)
        d[target-nums[i]] = i


if __name__=="__main__":
    nums_1 = [2,7,11,15]
    nums_2 = [3,2,4]
    nums_3 = [3,3]
    target = [9,6]
    method = int(input("Select the method to run: 1. Dictionary    2. Efficient Dictionary\n"))
    if method == 1:
        print("Array: "+str(nums_1)+"      Target: "+str(target[0])+"     Output: "+str(twoSumM1(nums_1, target[0])))
        print("Array: "+str(nums_2)+"      Target: "+str(target[1])+"     Output: "+str(twoSumM1(nums_2, target[1])))
        print("Array: "+str(nums_3)+"      Target: "+str(target[1])+"     Output: "+str(twoSumM1(nums_3, target[1])))
    elif method == 2:
        print("Array: "+str(nums_1)+"      Target: "+str(target[0])+"     Output: "+str(twoSumM2(nums_1, target[0])))
        print("Array: "+str(nums_2)+"      Target: "+str(target[1])+"     Output: "+str(twoSumM2(nums_2, target[1])))
        print("Array: "+str(nums_3)+"      Target: "+str(target[1])+"     Output: "+str(twoSumM2(nums_3, target[1])))
    else:
        print("Select a valid method\n")
