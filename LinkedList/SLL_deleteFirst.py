"""
You are developing a task management application where tasks are represented by unique IDs. Users can delete tasks from the beginning of the task list to quickly remove the most urgent tasks. You need to write a program to handle the deletion of task IDs from the beginning of a linked list. After all deletions are completed, the final list of task IDs should be printed to confirm that the tasks have been removed.Write a program to delete task IDs from the beginning of the linked list. After all deletions, print the entire linked list to show the updated list of task IDs. If the list is empty, Print the message as “List is empty”.

Input Format: 
    The first line contains an integer N, the number of task IDs to be initially added to the linked list.
    The second line contains N space-separated integers representing the task IDs.
    The third line contains an integer M, the number of tasks to be deleted from the beginning.
Constraints: NA

Output Format: 
    After completing all deletions, print the current linked list with elements separated by a space.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        # Traverse to the end and add the new node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_from_beginning(self, count):
        while self.head and count > 0:
            self.head = self.head.next
            count -= 1

    def print_list(self):
        if not self.head:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

# Read input
N = int(input())  # Number of task IDs
task_ids = list(map(int, input().split()))
M = int(input())  # Number of deletions from beginning

# Create the linked list and add task IDs
task_list = LinkedList()
for task_id in task_ids:
    task_list.append(task_id)

# Perform deletions
task_list.delete_from_beginning(M)

# Print updated list
task_list.print_list()
