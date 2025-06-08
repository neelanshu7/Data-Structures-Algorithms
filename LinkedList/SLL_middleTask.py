"""
Imagine you are managing a long-term project with a series of tasks arranged in a linear sequence. Each task is dependent on the completion of the previous one, and the tasks are stored in a singly linked list. At certain points in the project, you want to identify the critical task, which lies in the middle of the task flow, so you can allocate additional resources to it and ensure timely completion. In case there are two middle tasks, you want to focus on the second middle task as it represents the next crucial step in the project. You are given the head of a singly linked list, where each node represents a task in a project workflow. Your task is to find and return the middle task. If the list has two middle tasks, return the second middle task and all the tasks after it.

Input Format: 
    The input consists of a linked list represented by its head node.
    Each node contains an integer value representing the task ID or any relevant information.
Constraints: NA
Output Format: 
    The output will be a list of integers starting from the middle node to the end of the linked list.
    If there are two middle nodes, the output should start from the second middle node.
"""
import math
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TaskLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, task_id):
        new_node = Node(task_id)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self,N):
        if N%2==0:
            N=(N/2)+1
        else:
            N=math.ceil(N/2)
        current=self.head
        count=0
        while(self.head and count<N-1):
            self.head=self.head.next
            count=count+1
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

N = int(input())
task_ids = list(map(int, input().split()))

task_list = TaskLinkedList()
for task_id in task_ids:
    task_list.insert_at_end(task_id)

task_list.delete(N)

task_list.print_list()