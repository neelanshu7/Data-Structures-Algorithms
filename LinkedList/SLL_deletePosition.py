"""
You are building a task tracker for project management, where each task is represented by a unique ID and tasks are stored in the order they need to be completed. Sometimes, due to changes in project priorities, certain tasks need to be removed from the list based on their position. Your task is to write a program that deletes a task at a specified position from the list and prints the updated list of remaining tasks. Write a program that deletes a task (represented by a unique ID) from a given position in the linked list. After the deletion, print the updated list of task IDs. If the list is empty, Print the message as “List is empty”. If the entered position value is out the range, print the message as “Position out of range”.

Input Format
    The first line contains an integer N, the number of task IDs initially added to the linked list.
    The second line contains N space-separated integers representing the task IDs.
    The third line contains an integer P, the position of the task to be deleted (1-based index).
Constraints
    The value of P will always be between 1 and N (both inclusive).
Output Format
    Print the updated task list with the elements separated by a space.
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
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_from_position(self, pos):
        if pos <= 0 or not self.head:
            return
        if pos == 1:
            self.head = self.head.next
            return
        temp = self.head
        for _ in range(pos - 2):
            if not temp.next:
                return
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next

    def print_list(self):
        if not self.head:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

N = int(input())  # Number of task IDs
task_ids = list(map(int, input().split()))
P = int(input())  # Position to delete (1-based index)

# Create linked list and populate it
task_list = LinkedList()
for task_id in task_ids:
    task_list.append(task_id)

# Perform deletions
task_list.delete_from_position(P)

# Print the final list
task_list.print_list()
