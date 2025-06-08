"""
You are designing a digital library system where books are represented by unique book IDs. The library catalog is stored as a doubly linked list, allowing users to navigate both forwards and backwards through the list of books. When a new book is added to the library, it needs to be appended to the end of the catalog. Your task is to write a program that inserts a new book at the end of the catalog and prints the updated list of book IDs. Write a program to append a new book (represented by a unique book ID) to the end of the doubly linked list representing the library catalog. After the insertion, print the updated list of book IDs.

Input Format
    The first line contains an integer N, the number of books initially in the catalog.
    The second line contains N space-separated integers representing the book IDs.
Constraints
    The input values are all positive integers.
    There will be at least 1 book in the catalog initially.
Output Format
    Print the updated list of book IDs in sequence from the start to the end of the catalog.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__(self):
        self.head=None
    def traverse_forward(self):
        print("Forward Traversal:")
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        # print()
    def traverse_backward(self):
        print("Backward Traversal:")
        temp = self.head
        if not temp:
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev
        # print()
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Input reading
N = int(input())
task_ids = list(map(int, input().split()))

# Create the linked list and insert task IDs
task_list = DLL()
for task_id in task_ids:
    task_list.insert_at_end(task_id)

# Output the final linked list
task_list.print_list()