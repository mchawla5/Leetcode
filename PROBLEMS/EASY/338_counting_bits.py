'''
COUNTING BITS

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

SOLUTION
Method 1 (Brute Force)
    |_ TC: O(nlogn), SC: O(1)
Method 2 (DP)
    |_ TC: O(n), SC: O(1)

'''

def binaryDigitCounter(temp):
    binary, power, count = 0, 0, 0
    while temp>0:
        if temp%2 != 0:
            binary = 1*10**power + binary
            count +=1
        temp = temp//2
        power +=1
    return count

def method1(n):
    res = []
    for i in range(0, n+1):
        res.append(binaryDigitCounter(i))
    return res

def method2(n):
    dp = [0] * (n+1)
    offset = 1
    for i in range(1, n+1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i-offset]
    return dp

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'n': 2
        },
        'output': [0,1,1]
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'n': 5
        },
        'output': [0,1,1,2,1,2]
    })
    # TESTCASE 3:
    tests.append({
        'input': {
            'n': 1
        },
        'output': [0, 1]
    })
    # TESTCASE 4:
    tests.append({
        'input': {
            'n': 0
        },
        'output': [0]
    })

    choice = int(input("Enter the method you want to run with:  1. Brute Force  2. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))
        if choice == 2:
            print("TESTCASE "+str(i+1)+": "+str(method2(**test['input']) == test['output']))