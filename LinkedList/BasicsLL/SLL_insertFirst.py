"""
You are developing a simple task management application where tasks are represented by unique IDs. Users can add new tasks at the beginning of the task list for quick access. You need to write a program to handle the insertion of task IDs at the beginning of a linked list. After all insertions are completed, the final list of task IDs should be printed to confirm the additions. Write a program to insert new task IDs at the beginning of the linked list. After all insertions, print the entire linked list to show the updated list of task IDs.

Input Format: 
The first line contains an integer N, the number of task IDs to be initially added to the linked list.
The second line contains N space-separated integers representing the task IDs.

Constraints: NA

Output Format: 
After completing all insertions, print the current linked list with elements separated by a space.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TaskLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, task_id):
        new_node = Node(task_id)
        new_node.next = self.head
        self.head = new_node

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
    task_list.insert_at_beginning(task_id)

# Output the final linked list
task_list.print_list()
