'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''

def method1(prices):
    profit = 0
    buy = prices[0]
    for i in range(len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        else:
            profit = max(profit, prices[i]-buy)
    return profit

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            'prices': [7,1,5,3,6,4]
        },
        'output': 5
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            'prices': [7,6,4,3,1]
        },
        'output': 0
    })
    choice = int(input("Enter the method you want to run with:  1. DP\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))