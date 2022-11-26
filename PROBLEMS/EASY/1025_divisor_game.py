'''
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Example 1:
Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Example 2:
Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 
Constraints:
1 <= n <= 1000

SOLUTION
    M1 - DP O(n^3/2)
    M2 - Intutive
'''
import math

def divisorGameM2(n):
    return n%2 == 0

def divisorGameM1(n):
    if (n == 1):                # anyone reaches at the last result
        return 0
    if dp[n] != -1:             # have computed a value
        return dp[n]
    else:
        for i in range(1, math.floor(math.sqrt(n))+1):      # reducing the repeated factors
            if (n%i == 0):
                if divisorGameM1(n-i) == 0:
                    dp[n] = 1
                    return dp[n]
                if i!= 1 and divisorGameM1(n - n/i) == 0:
                    dp[n] = 1
                    return  dp[n]
        dp[n] = 0
        return dp[n]

if __name__ == "__main__":
    dp = [-1] * 1001
    print(bool(divisorGameM1(1)))
    print(bool(divisorGameM1(2)))
    print(bool(divisorGameM1(3)))

    print(bool(divisorGameM2(1)))
    print(bool(divisorGameM2(2)))
    print(bool(divisorGameM2(3)))