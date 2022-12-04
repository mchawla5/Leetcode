'''
BEST TIME TO BUY AND SELL STOCK

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

SOLUTION:
Method 1: (using DP)          Run Time: 105ms; Memory: 13.9
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
Method 2: (using 2 pointers)        Run Time: 104ms; Memory: 14.2
    |_ Time Complexity = O(N)
    |_ Space Complexity = O(N)
Method3: (Efficient DP)
    |_ Time Complexity = O(n)
    |_ Space Complexity = O(1)
'''

def pricesM1(prices):
    min_value = min(prices)
    id = 0
    diff_so_far = [0]*len(prices)
    for i in range(1, len(prices)):
        if prices[i] == min_value:
            id = i
        if i>id:
            if(prices[i]> prices[i-1]):
                diff_so_far[i] = max(prices[i] - min_value, diff_so_far[i-1])
            else:
                diff_so_far[i] = diff_so_far[i-1]
    return(diff_so_far[-1])

def pricesM2(prices):
    id = 0
    diff_so_far = 0
    d = {}
    for i in range(0, len(prices)):
        d[prices[i]] = i
    min_value = min(d)
    id = d[min_value]
    if min_value == 0:
        del d[min_value]
        min_value = min(d)
        id = d[min_value]
    
    for i in range(1, len(prices)):
        if(prices[i]> prices[i-1]):
            diff_so_far = max(prices[i] - min_value, diff_so_far)
    return(diff_so_far)

def pricesM3(prices):
    profit = 0
    buy = prices[0]
    for i in range(len(prices)):
        if buy > prices[i]:
            buy = prices[i]
        else:
            profit = max(profit, prices[i]-buy)
    return profit

if __name__=="__main__":
    prices1 = [7,1,5,3,6,4]
    prices2 = [7,6,4,3,1]
    prices3 = [2,4,1]
    prices4 = [1,2,4,2,5,7,2,4,9,0]

    method = int(input("Select the method you want to run:   1. Using DP   2. Using 2 Pointers   3. Efficient DP\n"))
    if method == 1:
        print("prices1 array: "+str(prices1)+"   output: "+str(pricesM1(prices1) == 5))
        print("prices2 array: "+str(prices2)+"   output: "+str(pricesM1(prices2) == 0))
        print("prices3 array: "+str(prices3)+"   output: "+str(pricesM1(prices3) == 2))
        print("prices4 array: "+str(prices4)+"   output: "+str(pricesM1(prices4) == 8))
    elif method == 2:
        print("prices1 array: "+str(prices1)+"   output: "+str(pricesM2(prices1)))
        print("prices2 array: "+str(prices2)+"   output: "+str(pricesM2(prices2)))
        print("prices3 array: "+str(prices3)+"   output: "+str(pricesM2(prices3)))
        print("prices4 array: "+str(prices4)+"   output: "+str(pricesM2(prices4)))
    elif method == 3:
        print("prices1 array: "+str(prices1)+"   output: "+str(pricesM3(prices1)))
        print("prices2 array: "+str(prices2)+"   output: "+str(pricesM3(prices2)))
        print("prices3 array: "+str(prices3)+"   output: "+str(pricesM3(prices3)))
        print("prices4 array: "+str(prices4)+"   output: "+str(pricesM3(prices4)))
    else:
        print("No method selected\n")