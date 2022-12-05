'''
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums

Example 1:
Input: n = 7
Output: 3
Explanation: According to the given rules:
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is max(0,1,1,2,1,3,2,3) = 3.

Example 2:
Input: n = 2
Output: 1
Explanation: According to the given rules, nums = [0,1,1]. The maximum is max(0,1,1) = 1.

Example 3:
Input: n = 3
Output: 2
Explanation: According to the given rules, nums = [0,1,1,2]. The maximum is max(0,1,1,2) = 2.
'''

def method1(n):
    dp = [0]* (n+1)
    ans = 0
    if n>0:
        dp[1] = 1
        ans = 1
    bound = n//2
    for i in range(1, bound+1):
        dp[2*i] = dp[i]
        ans = max(ans, dp[2*1])
        if (2*i + 1) <= n:
            dp[2*i + 1] = dp[i] + dp[i+1]
            ans = max(ans, dp[2*i +1])
    return ans

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'n': 7
        },
        'output': 3
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'n': 2
        },
        'output': 1
    })
    # TESTCASE 3:
    tests.append({
        'input': {
            'n': 3
        },
        'output': 2
    })
    # TESTCASE 4:
    tests.append({
        'input': {
            'n': 15
        },
        'output': 5
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))