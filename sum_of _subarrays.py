'''Problem Statement:
Sum of Subarrays bookmark_borderGiven an array of integers, answer queries of the form: [i, j]: Print the sum of array elements from A[i] to A[j], both inclusive.

Input Format:
The first line of input contains the N-size of the array. The next line contains N integers - elements of the array. The next line contains Q - number of queries. Each of the next Q lines contains 2 space-separated indexes: i and j.

Output Format:
For each query, print the sum of array elements from A[i] to A[j], both inclusive, separated by a new line.

Constraints:
30 points
1 <= N, Q <= 10000

70 points
1 <= N, Q <= 500000

General Constraints
-109 <= A[i] <= 109
0 <= i <= j <= N-1

Example:
Input:
10
1 30 13 -4 -5 12 -53 -12 43 100
4
0 5
1 7
2 3
7 9

Output:
47
-19
9
131

solution:'''

# function to find sumofsubarrays
def sumofsubarrays(n,a,i,j):
        
        if i==0:
            ans=l[j]
        else:
            ans=l[j]-l[i-1]
        return ans
n=int(input())
a=list(map(int,input().split()))
q=int(input())
l=[]
l.append(a[0])
ans=0
for k in range(1,n):
    l.append(l[k-1]+a[k])
for _ in range(q):
    i,j=map(int,input().split())
    res=sumofsubarrays(n,a,i,j)
    print("result:",res)




