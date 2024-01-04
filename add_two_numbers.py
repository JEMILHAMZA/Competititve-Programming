# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    #     class ListNode:
    # def __init__(self, val=0, next=None):
    #     self.val = val
    #     self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode()  # Dummy head to simplify handling of the result list
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # If either l1 or l2 is None, use 0 as the value
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the new digit and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10

            # Add the new digit to the result list
            current.next = ListNode(new_digit)
            current = current.next

            # Move to the next nodes in l1 and l2, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next
       
