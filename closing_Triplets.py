'''Given three arrays A, B, and C, choose a triplet a, b, c such that a, b, and c belong to the arrays A, B, and C respectively, such that the absolute difference between the maximum and minimum element of the chosen triplet is minimized, i.e., minimize |max(a,b,c)-min(a,b,c)|.

Input Format:
The first line of input contains T - the number of test cases. It is followed by 6T lines, the first line contains N1 - the size of the array A and the second line contains the elements of the array A. The third line contains N2 - the size of the array B and the fourth line contains the elements of the array B. The fifth line contains N3 - the size of the array C and the sixth line contains the array C elements.

Output Format:
For each test case, print the minimum absolute difference, separated by a newline.

Constraints:
10 points
1 <= T <= 100
1 <= N1, N2, N3 <= 100
0 <= A[i], B[i], C[i] <= 109

30 points
1 <= T <= 100
1 <= N1 ,N2, N3 <= 500
0 <= A[i], B[i], C[i] <= 109

60 points
1 <= T <= 100
1 <= N1, N2, N3 <= 10000
0 <= A[i], B[i], C[i] <= 109

Example:
Input
1
5
10 8 5 4 1
3
6 9 15
4
8 3 2 6

Output
1

Explanation:

Example 1: The triplet (5,6,6) belongs to the arrays A, B, and C respectively and it gives |max(a,b,c)-min(a,b,c)| = 1.


Solution:


'''


for i in range(int(input())):
    n=int(input())
    b1=list(map(int,input().split()))
    m=int(input())
    b2=list(map(int,input().split()))
    k=int(input())
    b3=list(map(int,input().split()))
    a1=sorted(b1)
    a2=sorted(b2)
    a3=sorted(b3)
    p1=0
    p2=0
    p3=0
    ans=float('inf')
    while p1<n and p2<m and p3<k:
        x=min(a1[p1],a2[p2],a3[p3])
        y=max(a1[p1],a2[p2],a3[p3])
        ans=min(ans,y-x)
        if a1[p1]==x:
            p1+=1
        elif a2[p2]==x:
            p2+=1
        else:
            p3+=1

    print("The minimum difference between maximum and minimum value of a triplet:",ans)

