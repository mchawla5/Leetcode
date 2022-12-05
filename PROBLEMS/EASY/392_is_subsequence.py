'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''

def method1(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i +=1
        j = j+1
    return 1 if i == len(s) else 0

if __name__ == "__main__":
    tests = []
    # TESTCASE 1:
    tests.append({
        'input': {
            's': "abc",
            't': "ahbgdc"
        },
        'output': 1
    })
    # TESTCASE 2:
    tests.append({
        'input': {
            's': "axc",
            't': "ahbgdc"
        },
        'output': 0
    })
    choice = int(input("Enter the method you want to run with:  1. Two pointers\n"))
    for i in range(len(tests)):
        test = tests[i]
        if choice == 1:
            print("TESTCASE "+str(i+1)+": "+str(method1(**test['input']) == test['output']))