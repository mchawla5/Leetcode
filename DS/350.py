'''
INTERSECTION OF 2 ARRAYS II

Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

SOLUTION:
Method 1: (using counters)          Run Time: 105ms; Memory: 13.9
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
Method 2: (using 2 pointers)        Run Time: 104ms; Memory: 14.2
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
Method 3: (efficient dictionary)    Run Time: 93ms; Memory: 14
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
Method 3: (efficient counters)      Run Time: 89ms; Memory: 14
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
'''

from collections import Counter

def intersectionM1(nums1, nums2):
    output = []
    if len(nums1) <= len(nums2):
        d = Counter(nums1)
        for num in nums2:
            if d[num] > 0:
                d[num] -=1
                output.append(num)
    else:
        d = Counter(nums2)
        for num in nums1:
            if d[num] > 0:
                d[num] -=1
                output.append(num)
    return(output)

def intersectionM2(nums1, nums2):
    sortednums1 = sorted(nums1)
    sortednums2 = sorted(nums2)
    i = j =0
    output = []
    while (i<len(sortednums1) and j<len(sortednums2)):
        if(sortednums1[i] < sortednums2[j]):
            i +=1
        elif(sortednums2[j] < sortednums1[i]):
            j +=1
        else:
            output.append(sortednums1[i])
            i +=1
            j +=1
    return output

def intersectionM3(nums1, nums2):
    d = {}
    output = []
    for i in nums1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
        
    for i in nums2:
        if i in d and d[i] > 0:
            d[i] -= 1
            output.append(i)
    return output

def intersectionM4(nums1, nums2):
    output = []
    d1 = Counter(nums1)
    d2 = Counter(nums2)
    intersect = d1 & d2
    for ele in intersect.elements():
        output.append(ele)
    return(output)


if __name__=="__main__":
    nums11 = [1,2,2,1]
    nums21 = [2,2]

    nums12 = [4,9,5]
    nums22 = [9,4,9,8,4]

    method = int(input("Select the method you want to run:   1. Using Counters   2. Using 2 Pointers   3. Efficient Dictionary   4. Efficient Counters\n"))
    if method == 1:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM1(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM1(nums12, nums22)))
    elif method == 2:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM2(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM2(nums12, nums22)))
    elif method == 3:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM3(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM3(nums12, nums22)))
    elif method == 4:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM4(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM4(nums12, nums22)))
    else:
        print("No method selected\n")