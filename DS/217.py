'''
CONTAINS DUPLICATE

nums = [1,2,3,1] return True else False

SOLUTION:
Method 1 (using dict)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
Method 2 (using dict - efficient)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(n)
Method 3 (using sets)
    |_ Time Complexity = O(1)
    |_ Space Complexity = O(n)
Method 4 (using sets - efficient)
    |_ Time Complexity = O(1)
    |_ Space Complexity = O(n)
'''

def containsDuplicateM1(nums):
    hm = {}
    for i in nums:
        if i in hm.keys():
            hm[i] = hm[i] +1
        else:
            hm[i] = 1
    for v in hm:
        if (hm[v] > 1):
            return True
    return False

def containsDuplicateM2(nums):
    hm = {}
    for i in nums:
        if i not in hm:
            hm[i] = 1
        else:
            return True
    return False

def containDuplicateM3(nums):
    nums_set =  set(nums)
    if len(nums) == len(nums_set):
        return False
    return True

def containDuplicateM4(nums):
    nums_set =  set()
    for i in nums:
        if i in nums_set:
            return True
        nums_set.add(i)
    return False


if __name__=="__main__":
    nums = []
    size = int(input("Enter the length of array: \n"))
    for i in range(0, size):
        nums.append(int(input("Enter the elements in array: \n")))
    method = int(input("Select the method to run: 1. Original one   2. Efficient dict   3. Using set    4. Efficient set\n"))
    if method == 1:
        print(containsDuplicateM1(nums))
    elif method == 2:
        print(containsDuplicateM2(nums))
    elif method == 3:
        print(containDuplicateM3(nums))
    elif method == 4:
        print(containDuplicateM4(nums))
    else:
        print("No method selected")