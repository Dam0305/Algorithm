# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """


        node, result = head, None

        while node:
            next, node.next = node.next, result
            result, node = node, next


        return result


n1 = ListNode(1)
curr = n1
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(5)

result = Solution().reverseList(n1)

p = result
while p:
    print(p.val)
    p = p.next
