"""
You are developing a task management system where tasks are stored in a circular to-do list. Each task is represented by a unique task ID. The circular nature of the list allows users to loop through their tasks continuously. Your task is to write a program that inserts a new task at the end of the circular linked list and prints the updated list of task IDs. Write a program to append a new task (represented by a unique task ID) to the end of the singly circular linked list representing the to-do list. After the insertion, print the updated list of task IDs by traversing the list once starting from the head.

Input Format:
    The first line contains an integer N, the number of initial tasks in the to-do list.
    The second line contains N space-separated integers representing the task IDs.
Constraints: 
    The input values are all positive integers.
    There will be at least one task initially in the to-do list.
Output Format: 
    Print the updated list of task IDs in sequence from the head of the list, traversing the circular list once.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            ptr = self.head
            while ptr.next != self.head:
                ptr = ptr.next
            ptr.next = new_node
            new_node.next = self.head

    def print_list(self):
        if not self.head:
            print("List is empty")
            return
        ptr = self.head
        i = 0
        while True:
            print(ptr.data,end=' ')
            ptr = ptr.next
            i += 1
            if ptr == self.head:
                break

# Input reading
N = int(input())
task_ids = list(map(int, input().split()))

# Create the linked list and insert task IDs
task_list = CircularLinkedList()
for task_id in task_ids:
    task_list.insert_at_end(task_id)

# Output the final linked list
task_list.print_list()