'''
In Pascal's triangle, each number is the sum of the two numbers directly above
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
'''
def method1(numRows):
    out = [[0]*i for i in range(1,numRows+1)]
    for i in range(numRows):
        out[i][0] = 1
        for j in range(1,i):
            out[i][j] = out[i-1][j-1] + out[i-1][j]
        out[i][i] = 1
    return out

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'numRows': 5
        },
        'output': [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'numRows': 1
        },
        'output': [[1]]
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))