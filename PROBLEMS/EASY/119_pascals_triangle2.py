'''
In Pascal's triangle, each number is the sum of the two numbers directly above it:
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
'''
def method1(rowIndex):
    out = [[0]*i for i in range(1,rowIndex+2)]
    for i in range(rowIndex+1):
        out[i][0] = 1
        for j in range(1,i):
            out[i][j] = out[i-1][j-1] + out[i-1][j]
        out[i][i] = 1
    return out[rowIndex]

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'rowIndex': 3
        },
        'output': [1,3,3,1]
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'rowIndex': 0
        },
        'output': [1]
    })
    # TESTCASE 3:
    tests.append({
        'input': {
            'rowIndex': 1
        },
        'output': [1,1]
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))