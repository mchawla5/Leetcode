'''
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4^x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

SOLUTION
    Method1 (Recursion):
        |_ O(logn)
    Method2 (Bit Manipulation):
        |_ O(1)
    Method3 (Math):
        |_ O(1)
'''

def method1(n):
    return n>0 and (n == 1 or (n%4==0 and method1(n/4)))

def method2(n):
    return n > 0 and not (n & (n-1)) and (len(bin(n))%2 == 1)

def method3(n):
    return n > 0 and (4**30 % n == 0)

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
            'n': 16
        },
        'output': True
    })
    # TESTCASE 3;
    tests.append({
        'input': {
            'n': 5
        },
        'output': False
    })
    choice = int(input("Enter the method you want to run with:  1. Recursion    2. Bit Manipuation    3. Math\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+('PASS' if (method1(**test['input']) == test['output']) else 'FAIL'))
        if choice == 2:
            print("TESTCASE "+str(i+1)+": "+('PASS' if (method2(**test['input']) == test['output']) else 'FAIL'))
        if choice == 3:
            print("TESTCASE "+str(i+1)+": "+('PASS' if (method3(**test['input']) == test['output']) else 'FAIL'))