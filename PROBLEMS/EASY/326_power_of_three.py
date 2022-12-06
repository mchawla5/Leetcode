'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 3^3

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3^x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3^x = (-1).

SOUTION
    Method1 (recursion):
        |_ O(logn)
    Method2 (Math):
        |_ O(1)
'''

def method1(n):
    return n>0 and (n == 1 or (n%3==0 and method1(n/3)))

def method2(n):
    return n > 0 and (3**30 % n == 0)

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'n': 1
        },
        'output': True
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'n': 27
        },
        'output': True
    })
    # TESTCASE 3;
    tests.append({
        'input': {
            'n': 0
        },
        'output': False
    })
    choice = int(input("Enter the method you want to run with:  1. Recursion    2. Math\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+('PASS' if (method1(**test['input']) == test['output']) else 'FAIL'))
        if choice == 2:
            print("TESTCASE "+str(i+1)+": "+('PASS' if (method2(**test['input']) == test['output']) else 'FAIL'))