
'''Level Order of Tree bookmark_borderGiven an array of unique elements, construct a Binary Search Tree and print the Level Order of the tree.

Input Format
The first line of input contains T - the number of test cases. It's followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the Level Order of the Binary Search Tree, separate each level by a newline. Separate the output of different test cases with an extra newline.

Constraints
1 <= T <= 1000
1 <= N <= 1000
0 <= ar[i] <= 10000

Example
Input
3
5
1 2 3 4 5
5
3 2 4 1 5
7
4 5 15 0 1 7 17

Output
1
2
3
4
5

3
2 4
1 5

4
0 5
1 15
7 17 '''



class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def create_bst(arr):
    root=None
    for ele in arr:
        root=insert(root,ele)
    return root
def insert(root,ele):
    if root is None:
        return Node(ele)
    if ele<root.data:
        root.left=insert(root.left,ele)
    if ele>root.data:
        root.right=insert(root.right,ele)
    return root
def levelorder(root):
    q=[]
    q.append(root)
    while q:
        n=len(q)
        for i in range(n):
            p=q.pop(0)
            print(p.data,end=" ")
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        print()

   
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    bst_root=create_bst(a)

    levelorder(bst_root)


