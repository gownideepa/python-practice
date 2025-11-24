
'''Tree Traversals bookmark_borderGiven an array of unique elements, construct a Binary Search Tree and print the Preorder, Inorder and Postorder Traversals of the tree.

Input Format
The first line of input contains T - the number of test cases. It is followed by 2T lines. The first line of each test case contains N - the number of nodes in the BST. The next line contains N unique integers - value of the nodes.

Output Format
For each test case, print the PreOrder, InOrder and PostOrder Traversals of the Binary Search Tree, separate each traversal by a newline. Separate the output of different test cases with an extra newline.

Constraints
1 <= T <= 100
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
1 2 3 4 5
1 2 3 4 5
5 4 3 2 1

3 2 1 4 5
1 2 3 4 5
1 2 5 4 3

4 0 1 5 15 7 17
0 1 4 5 7 15 17
1 0 7 17 15 5 4 '''


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insert(root,ele):
    if (root is None):
        return Node(ele)
    if (ele<root.data):
        root.left=insert(root.left,ele)
    if (ele>root.data):
        root.right=insert(root.right,ele)
    return root
def preorder(root):
    if (root is None):
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
# creation of bst
def create_bst(arr):
    root=None
    for ele in arr:
        root=insert(root,ele)
    return root

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    bst_root=create_bst(a)
    preorder(bst_root)
    print()
    inorder(bst_root)
    print()
    postorder(bst_root)

    print()


