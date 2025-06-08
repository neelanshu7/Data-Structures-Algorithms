"""
You are developing a project management application for a team of software developers. In this application, tasks are represented by unique IDs, and team members can add tasks to their project. As tasks are completed, they need to be removed from the task list to maintain an organized view of ongoing tasks. The team wants to delete the completed tasks from the end of the list, ensuring they focus only on active work. Write a program to manage the deletion of completed tasks from the end of the task list. After all deletions, print the updated list of remaining task IDs to show which tasks are still pending. If the list is empty, Print the message as “List is empty”.

Input Format:
    The first line contains an integer N, the number of task IDs to be initially added to the task list.
    The second line contains N space-separated integers representing the task IDs.
    The third line contains an integer M, the number of completed tasks to be deleted from the end of the list.
Constraints: NA

Output Format: 
    After completing all deletions, print the current task list with elements separated by a space.
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
 
    def delete_from_end(self, count):
        for _ in range(count):
            if not self.head:
                return
            if not self.head.next:
                self.head = None
                return
            temp = self.head
            while temp.next and temp.next.next:
                temp = temp.next
            temp.next = None

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
M = int(input())  # Number of deletions from end

# Create the linked list and add task IDs
task_list = LinkedList()
for task_id in task_ids:
    task_list.append(task_id)

# Perform deletions
task_list.delete_from_end(M)

# Print updated list
task_list.print_list()