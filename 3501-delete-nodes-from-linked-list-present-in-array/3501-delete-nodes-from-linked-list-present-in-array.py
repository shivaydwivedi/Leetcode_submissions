# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        nums_set = set(nums)  # O(k)
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while curr:
            if curr.val in nums_set:
                prev.next = curr.next  # delete node
            else:
                prev = curr  # keep node
            curr = curr.next
        
        return dummy.next

        