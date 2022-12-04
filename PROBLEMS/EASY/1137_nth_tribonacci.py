'''
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537
'''

def method1(n):
    minus1 = minus2 = 1
    minus3 = 0
    if n == 0:
        return minus3
    if n == 1:
        return minus2
    if n == 2:
        return minus1
    for i in range(3, n+1):
        dp = minus1 + minus2 +minus3
        minus3 = minus2
        minus2 = minus1
        minus1 = dp
    return dp

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'n': 4
        },
        'output': 4
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'n': 5
        },
        'output': 7
    })
    # TESTCASE 3:
    tests.append({
        'input': {
            'n': 10
        },
        'output': 149
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))