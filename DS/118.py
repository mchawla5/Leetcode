'''
PASCAL'S TRIANGLE

In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

SOLUTION:
Method 1: (bruteforce)
    |_ Time Complexity = O(N^2)
    |_ Space Complexity = O(N^2)
Method 2: (dp)
    |_ Time Complexity = O(N^2)
    |_ Space Complexity = O(N^2)
Method 3: (best run time)
    |_ Time Complexity = O(N^2)
    |_ Space Complexity = O(N^2)
Method 4: (best memory)
    |_ Time Complexity = O(N^2)
    |_ Space Complexity = O(N^2)
'''

def pascalM1(numRows):
    out = [[0]*i for i in range(1,numRows+1)]
    for i in range(numRows):
        out[i][0] = 1
        for j in range(1,i):
            out[i][j] = out[i-1][j-1] + out[i-1][j]
        out[i][i] = 1
    return out

def pascalM2(numRows):
    out = []
    for i in range(numRows):
        if i==0:
            prev = [1]
            out.append(prev)
        else:
            curr =[1]
            j = 1
            while(j<i):
                curr.append(prev[j-1]+prev[j])
                j +=1
            curr.append(1)
            out.append(curr)
            prev = curr
    return out

def pascalM3(numRows):
    if numRows == 1:
        return[[1]]
    out = [[1],[1,1]]
    for i in range(numRows-2):
        out.append([1] + [ out[-1][j] + out[-1][j+1] for j in range(i+1) ] + [1])
    return out

def pascalM4(numRows):
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1,1]]
    out = [[1], [1,1]]
    for i in range(numRows-2):
        cur = out[-1]
        l,r = 0,1
        temp = [1]
        while r < len(cur):
            new_cur = cur[l] + cur[r]
            temp.append(new_cur)
            l +=1
            r +=1
        temp.append(1)
        out.append(temp)
    return out            


if __name__=="__main__":
    numRows = 7
    method = int(input("Select the method you want to run:   1. Using bruteforce   2. Using DP   3. Best runtime   4. Best memory\n"))
    if method == 1:
        print("number of rows: "+str(numRows)+"\t\toutput: "+str(pascalM1(numRows)))
    elif method == 2:
        print("original matrix: "+str(numRows)+"\t\toutput: "+str(pascalM2(numRows)))
    elif method == 3:
        print("original matrix: "+str(numRows)+"\t\toutput: "+str(pascalM3(numRows)))
    elif method == 4:
        print("original matrix: "+str(numRows)+"\t\toutput: "+str(pascalM4(numRows)))
    else:
        print("No method selected\n")