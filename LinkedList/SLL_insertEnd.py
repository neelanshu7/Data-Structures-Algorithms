"""
You are working on a real-time inventory management system where you need to maintain a list of product IDs in a linked list. As new products are added to the inventory, their IDs are appended at the end of the list. You have been tasked with writing a program to handle this operation.Write a program to insert a new product ID at the end of the linked list. After the completion of insertion, print the entire linked list to confirm that the new ID has been added.

Input Format
    1. The first line contains an integer N, the number of product IDs to be initially added to the linked list.
    2. The second line contains N space-separated integers, representing the product IDs.
Constraints: NA
Output Format: After inserting the product ID, print the current linked list, with elements separated by a space.
"""

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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Input reading
N = int(input())
task_ids = list(map(int, input().split()))

# Create the linked list and insert task IDs
task_list = TaskLinkedList()
for task_id in task_ids:
    task_list.insert_at_end(task_id)

# Output the final linked list
task_list.print_list()