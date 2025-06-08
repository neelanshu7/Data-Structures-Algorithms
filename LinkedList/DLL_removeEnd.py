"""
You are building a digital library system where each book is represented by a unique book ID. The library catalog is stored as a doubly linked list, allowing users to navigate through the list of books. Occasionally, books are removed from the library, and when a book is removed from the end of the catalog, it should no longer appear in the list. Your task is to write a program that deletes the last book from the catalog and prints the updated list of book IDs.Write a program to delete the last book from the doubly linked list representing the library catalog. After the deletion, print the updated list of book IDs. If the list is empty, Print the message as “List is empty”.

Input Format
    The first line contains an integer N, the number of books initially in the catalog.
    The second line contains N space-separated integers representing the book IDs.
Constraints
    The input values are all positive integers.
    There will be at least 1 book in the catalog initially.
Output Format
    Print the updated list of book IDs in sequence from the start to the end of the catalog after the last book has been removed.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def delete_last(self):
        if not self.head:
            return False  # Empty list condn
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return True
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(' '.join(elements))

n = int(input())
book_ids = list(map(int, input().split())) 

dll = DoublyLinkedList()
for book_id in book_ids:
    dll.append(book_id)

dll.delete_last() # Delete last

# Display
if dll.head is None:
    print("List is empty")
else:
    dll.display()