'''Implement Queue bookmark_borderImplement the Queue data structure and perform Enqueue / Dequeue operations.

Note: 
 Do not use any inbuilt functions / libraries for the Queue.  Input Format
The first line of input contains T - number of operations. It is followed by T lines, each line contains either "Enqueue x" or "Dequeue".

Output Format:
For each "Dequeue" operation, print the dequeued element, separated by a newline. If the queue is empty, print "Empty".

Constraints:
1 <= T <= 10000
-100 <= x <= 100

Example:
Input
8
Enqueue 5
Dequeue
Dequeue
Enqueue 10
Enqueue -15
Dequeue
Enqueue -10
Dequeue

Output:
5
Empty
10
-15 


# Solution:'''



t=int(input())
st1=[]
for i in range(t):
    a=input()
    if "Enqueue" in a:
        op,ele=map(str,a.split())
        st1.append(ele)
    else:
        if len(st1)==0:
            print("Empty")
        else:

            print(st1.pop(0))




