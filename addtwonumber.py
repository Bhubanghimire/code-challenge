# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        list_node = ListNode()
        print(list_node.val)
        
        while l1 or l2:
            reminder = l2%10
            print(reminder)
            l2 = l2/10


solution = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
solution.addTwoNumbers(l1, l2)



