Problem Statement:
Substring Matching bookmark_borderYou are given two strings A and B. You are also given Q queries with 4 indices i, j, k, and l. Check whether the substring of A[i:j] matches the substring of B[k:l].

Input Format:
The first line of input contains T - the number of test cases. In each test case, the first line contains the string A and the second line contains the string B.
The next line contains an integer Q - the number of queries. The Q subsequent lines each contain 4 integers i, j, k, and l, separated by a space.

Output Format:
For each query, on a new line, print "Yes" if the substring of A matches the substring of B, print "No" otherwise.

Constraints:
30 points
1 <= T <= 100
1 <= len(A), len(B) <= 100
0 <= Q <= 1000

120 points
1 <= T <= 100
1 <= len(A), len(B) <= 10000
0 <= Q <= 10000

General Constraints
'a' <= A[i], B[i] <= 'z'
0 <= i <= j < len(A)
0 <= k <= l < len(B)

Example:
Input
2
smartinterviews
intermediate
2
5 9 0 4
1 3 2 4
hackerrank
hackerearth
1
0 3 0 3

Output
Yes
No
Yes


Solution:

    
for _ in range(int(input())):
    s=input()
    t=input()
    q=int(input())
    for _ in range(q):
        i,j,k,l=map(int,input().split())
        s1=''
        s2=''
        for a in range(i,j+1):
            s1+=s[a]
        for b in range(k,l+1):
            s2+=t[b]
        if s1==s2:
            print("Yes")
        else:
            print("No")

