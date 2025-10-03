'''First Missing Positive Integer:


You are given an array of integers of size N. Find the first positive integer that is missing from the array.

Note
 Try solving in O(N) time without using any additional space, except the input array.  Input Format
The first line of input contains T - the number of test cases. For each test case, the first line contains one integer N - the size of the array. The second line contains N integers - the elements of the array.

Output Format
For each test case, print the first missing positive integer, separated by a newline.

Constraints
1 <= T <= 100
1 <= N <= 105
-105 <= A[i] <= 105

Example:
Input
2
5
2 0 1 5 -3
6
2 -7 3 1 8 -1

Output
3
4

Explanation

Example 1: The first missing positive integer is 3, as 1 and 2 are present in the array.'''


# Solution:
t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=[x for x in arr if x>0]
    if not arr:
        print(1)
        continue
    arr=sorted(set(arr))
    if  arr[0]!=1:

        print(1)
        continue
    m=-1
    for i in range(len(arr)-1):
        if arr[i+1]!=arr[i]+1:
            m=arr[i]+1
            break
    if m==-1:
        print(arr[-1]+1)
    else:

        print(m)


