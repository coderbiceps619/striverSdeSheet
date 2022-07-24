# Problem Statement: Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list instead, you will be given access to the node to be deleted directly. It is guaranteed that the node to be deleted is not a tail node in the list.
# Examples:
# Example 1:
# Input:
#  Linked list: [1,4,2,3]
#        Node = 2
# Output:
# Linked list: [1,4,3]
# Explanation: Access is given to node 2. After deleting nodes, the linked list will be modified to [1,4,3].
# Example 2:
# Input:
#  Linked list: [1,2,3,4]
#        Node = 1
# Output: Linked list: [2,3,4]
# Explanation:
#  Access is given to node 1. After deleting nodes, the linked list will be modified to [2,3,4].

# Time Complexity: O(1)
# Reason: It is a two-step process that can be obtained in constant time.
# Space Complexity: O(1)

def deleteNode(self, node):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        