'''
Height of Tree bookmark_borderGiven an array of unique elements, construct a Binary Search Tree and find the height of the tree.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the height of the Binary Search Tree, separated by a newline.

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
4
2
3
'''
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
    if ele < root.data:
        root.left=insert(root.left,ele)
    if ele>root.data:
        root.right=insert(root.right,ele)
    return root
def height(root):
    if root is None:
        return -1
    return max(height(root.left),height(root.right))+1

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    bst_root=create_bst(a)
    print(height(bst_root))