'''
MERGE SORTED ARRAY

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

SOLUTION:
Method 1:
    |_ Time Complexity = O(NlogN)
    |_ Space Complexity = O(1)
Method 2:
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(1)
'''

def mergeSortedM1(nums1, nums2, m, n):
    idx = 0
    for i in range(len(nums1)):
        if idx >= n:
            break
        if nums1[i] == 0:
            nums1[i] = nums2[idx]
            idx += 1
    nums1 = sorted(nums1)
    return nums1

def mergeSortedM2(nums1, nums2, m, n):
    pos = m+n-1
    while m and n:
        if nums1[m-1] >= nums2[n-1]:
            nums1[pos] = nums1[m-1]
            m -= 1
            pos -= 1
        else:
            nums1[pos] = nums2[n-1]
            n -= 1
            pos -=1 
    while n:
        nums1[pos] = nums2[n-1]
        n -= 1
        pos -= 1
    return nums1


if __name__=="__main__":
    nums11 = [9,10,11,0,0,0,0]
    nums21 = [1,2,3,4]
    m1 = 3
    n1 = 4
    nums12 = [1,2,3,0,0,0]
    nums22 = [2,5,6]
    m2 = 3
    n2 = 3
    nums13 = [1]
    nums23 = []
    m3 = 1
    n3 = 0
    nums14 = [0]
    nums24 = [1]
    m4 = 0
    n4 = 1
    method = int(input("Select the method you want to run: 1. My Approach   2. Another Approach\n"))
    if method == 1:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+" m: "+str(m1)+"   n: "+str(n1)+"   output: "+str(mergeSortedM1(nums11, nums21, m1, n1)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+" m: "+str(m2)+"   n: "+str(n2)+"   output: "+str(mergeSortedM1(nums12, nums22, m2, n2)))
        print("nums1 array: "+str(nums13)+"  nums2 array: "+str(nums23)+" m: "+str(m3)+"   n: "+str(n3)+"   output: "+str(mergeSortedM1(nums13, nums23, m3, n3)))
        print("nums1 array: "+str(nums14)+"  nums2 array: "+str(nums24)+" m: "+str(m4)+"   n: "+str(n4)+"   output: "+str(mergeSortedM1(nums14, nums24, m4, n4)))
    elif method == 2:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+" m: "+str(m1)+"   n: "+str(n1)+"   output: "+str(mergeSortedM2(nums11, nums21, m1, n1)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+" m: "+str(m2)+"   n: "+str(n2)+"   output: "+str(mergeSortedM2(nums12, nums22, m2, n2)))
        print("nums1 array: "+str(nums13)+"  nums2 array: "+str(nums23)+" m: "+str(m3)+"   n: "+str(n3)+"   output: "+str(mergeSortedM2(nums13, nums23, m3, n3)))
        print("nums1 array: "+str(nums14)+"  nums2 array: "+str(nums24)+" m: "+str(m4)+"   n: "+str(n4)+"   output: "+str(mergeSortedM2(nums14, nums24, m4, n4)))
    else:
        print("No method selected\n")