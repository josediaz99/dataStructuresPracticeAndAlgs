class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    output = ListNode()  # Dummy node to facilitate list operations
    current = output     # Pointer to build the new list
    carry = 0            # Carry should be an integer

    currentL1 = l1       # Pointer to traverse the first list
    currentL2 = l2       # Pointer to traverse the second list

    while currentL1 or currentL2 or carry:
        val1 = currentL1.val if currentL1 else 0
        val2 = currentL2.val if currentL2 else 0

        # Calculate new sum and update carry
        total = val1 + val2 + carry
        carry = total // 10
        new_value = total % 10

        # Create a new node with the summed value and link it
        current.next = ListNode(new_value)
        current = current.next  # Move current to the end of the list

        # Move to the next nodes in l1 and l2
        if currentL1:
            currentL1 = currentL1.next
        if currentL2:
            currentL2 = currentL2.next

    # Since the first node is a dummy node, return the next node
    return output.next

# Helper function to print the linked list
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test the function with the given lists
# Assuming you have a function to convert a list to a linked list
def createLinkedList(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Creating linked lists from the lists
l1 = createLinkedList([2, 4, 3])
l2 = createLinkedList([5, 6, 4])

# Adding two numbers
result = addTwoNumbers(l1, l2)

# Printing the result
printList(result)