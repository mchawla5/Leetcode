'''
RESHAPE THE MATRIX

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

SOLUTION:
Method 1: (original approach)
    |_ Time Complexity = O(M*N)
    |_ Space Complexity = O(M*N)
Method 2: (fast for time)
    |_ Time Complexity = O(M*N)
    |_ Space Complexity = O(M*N)
Method 3: (less memory)
    |_ Time Complexity = O(M*N)
    |_ Space Complexity = O(M*N)
'''

from collections import deque

def reshapeM1(mat, r, c):
    m,n = len(mat), len(mat[0])
    if r*c != m*n:
        return mat
    new_mat = [[0]*c for iter in range(r)]
    for i in range(m*n):
        new_mat[i//c][i%c] = mat[i//n][i%n]
    return new_mat

def reshapeM2(mat, r, c):
    if r*c != len(mat) * len(mat[0]):
        return mat
    new_mat = [[]]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            k = mat[i][j]
            if len(new_mat[-1])<c:
                new_mat[-1].append(k)
            else:
                new_mat.append([k])
    return new_mat

def reshapeM3(mat, r, c):
    m,n = len(mat), len(mat[0])
    if r*c != m*n:
        return mat
    new_mat = [[0]*c for iter in range(r)]
    q = deque([])
    for i in range(m):
        for j in range(n):
            q.append(mat[i][j])
    for i in range(r):
        for j in range(c):
            new_mat[i][j] = q.popleft()
    return new_mat



if __name__=="__main__":
    mat = [[1,2],[3,4],[5,6]]
    r = 2
    c = 3

    method = int(input("Select the method you want to run:   1. Using 1 loop of m*n   2. Using 2 loops with append   3. Efficient memory dequeue\n"))
    if method == 1:
        print("original matrix: "+str(mat)+"\t\tnew rows: "+str(r)+"\t\tnew columns: "+str(c)+"\t\toutput: "+str(reshapeM1(mat, r, c)))
    elif method == 2:
        print("original matrix: "+str(mat)+"\t\tnew rows: "+str(r)+"\t\tnew columns: "+str(c)+"\t\toutput: "+str(reshapeM2(mat, r, c)))
    elif method == 3:
        print("original matrix: "+str(mat)+"\t\tnew rows: "+str(r)+"\t\tnew columns: "+str(c)+"\t\toutput: "+str(reshapeM3(mat, r, c)))
    else:
        print("No method selected\n")


    '''
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM2(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM2(nums12, nums22)))
    elif method == 3:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM3(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM3(nums12, nums22)))
    elif method == 4:
        print("nums1 array: "+str(nums11)+"  nums2 array: "+str(nums21)+"   output: "+str(intersectionM4(nums11, nums21)))
        print("nums1 array: "+str(nums12)+"  nums2 array: "+str(nums22)+"   output: "+str(intersectionM4(nums12, nums22)))
    '''