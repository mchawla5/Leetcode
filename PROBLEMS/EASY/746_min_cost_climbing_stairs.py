'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

def method1(cost):
    cost.append(0)
    for i in range(len(cost)-3, -1, -1):
        cost[i] += min(cost[i+1], cost[i+2])
    return min(cost[0], cost[1])

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'cost': [10,15,20]
        },
        'output': 15
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'cost': [1,100,1,1,1,100,1,1,100,1]
        },
        'output': 6
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))