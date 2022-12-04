'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''
def method1(n):
    one,two= 1,1
    for i in range(n-1):
        temp = one
        one = one+two
        two = temp
    return one

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'n': 2
        },
        'output': 2
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'n': 3
        },
        'output': 3
    })
    # TESTCASE 3:
    tests.append({
        'input': {
            'n': 5
        },
        'output': 8
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))