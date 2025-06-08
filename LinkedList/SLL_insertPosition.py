"""
You are developing a task tracker for a project where tasks are assigned unique IDs. These tasks are arranged in a linked list, based on the order in which they need to be completed. Sometimes, a new task needs to be inserted at a specific position in the list, ensuring it is prioritized correctly. Your task is to write a program to insert a new task at a given position in the task list and print the updated list after the insertion.Write a program that inserts a new task (represented by a unique task ID) at a specific position in the task list. After the insertion, print the updated list of task IDs. If the entered position value is out the range, print the message as “Position out of range”.

Input Format: 
    1. The first line contains an integer N, the number of task IDs initially added to the linked list.
    2. The second line contains N space-separated integers representing the task IDs.
    3. The third line contains an integer P, the position at which the new task ID should be inserted (1-based index).
    4. The fourth line contains an integer M, the new task ID to be inserted.

Constraints: The value of P will always be between 1 and N+1 (both inclusive).

Output Format: Print the updated task list with the elements separated by a space.
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

    def insert_at_position(self, pos, task_id):
        new_node = Node(task_id)
        if pos < 1:
            print("Position out of range")
            return False

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return True

        current = self.head
        count = 1
        while current and count < pos - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of range")
            return False

        new_node.next = current.next
        current.next = new_node
        return True

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

def main():
    N = int(input())
    task_ids = list(map(int, input().split()))
    P = int(input())
    M = int(input())

    task_list = TaskLinkedList()
    for task_id in task_ids:
        task_list.insert_at_end(task_id)

    if not task_list.insert_at_position(P, M):
        return
    else:
        task_list.print_list()

# Call the main function
main()