class Node:
    # Constructor to initialize a node
    def __init__(self, data=None):
        self.data = data  # Node data
        self.next = None  # Pointer to the next node


class LinkedList:
    # Constructor to initialize a linked list
    def __init__(self):
        self.head = None  # Head of the list

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Link the new node to the head
        self.head = new_node  # Update the head to the new node

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node  # Make the new node the head
        else:
            cur = self.head  # Start from the head
            while cur.next:  # Traverse to the end of the list
                cur = cur.next
            cur.next = new_node  # Link the last node to the new node

    # Insert a new node after a given previous node
    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Previous node does not exist.")
            return
        new_node = Node(data)  # Create a new node
        new_node.next = prev_node.next  # Link the new node to the next node of prev_node
        prev_node.next = new_node  # Link prev_node to the new node

    # Delete a node by key
    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:  # If the head node itself holds the key
            self.head = cur.next  # Update the head
            cur = None  # Free the old head
            return
        prev = None
        while cur and cur.data != key:  # Search for the key
            prev = cur
            cur = cur.next
        if cur is None:  # If the key is not present
            return
        prev.next = cur.next  # Unlink the node
        cur = None  # Free the node

    # Search for an element by value
    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur  # Return the node if found
            cur = cur.next
        return None  # Return None if not found

    # Print the linked list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')  # Print the data
            current = current.next
        print()  # New line at the end of the list


# Function to reverse the linked list
def reverse_list(linked_list: LinkedList):
    prev = None
    current = linked_list.head
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev  # Reverse the current node's pointer
        prev = current  # Move pointers one position ahead
        current = next_node
    linked_list.head = prev  # Update the head to the new first node


# Algorithm to sort the linked list using merge sort

# Function to merge two sorted lists
def sorted_merge(a: Node, b: Node) -> Node:
    if a is None:
        return b
    if b is None:
        return a
    if a.data <= b.data:
        result = a
        result.next = sorted_merge(a.next, b)
    else:
        result = b
        result.next = sorted_merge(a, b.next)
    return result

# Function to get the middle of the list
def get_middle(head: Node) -> Node:
    if head is None:
        return head
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Function to perform merge sort on the linked list
def merge_sort(head: Node) -> Node:
    if head is None or head.next is None:
        return head
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    sorted_list = sorted_merge(left, right)
    return sorted_list

# Function to sort the linked list
def sort_linked_list(linked_list: LinkedList):
    linked_list.head = merge_sort(linked_list.head)


# Function to merge two sorted linked lists
def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged_list = LinkedList()
    merged_list.head = sorted_merge(list1.head, list2.head)
    return merged_list


# Example usage

# Create two lists
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

# Print initial lists
print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()

# Reverse the first list
reverse_list(list1)
print("Reversed List 1:")
list1.print_list()

# Sort the first list
sort_linked_list(list1)
print("Sorted Reversed List 1:")
list1.print_list()

# Merge the two sorted lists
merged_list = merge_sorted_lists(list1, list2)
print("Merged Sorted List:")
merged_list.print_list()
