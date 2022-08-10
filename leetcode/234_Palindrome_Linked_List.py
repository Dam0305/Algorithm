class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        arr = []

        p = head
        while p:
            arr.append(p.val)
            p = p.next

        return True if arr == arr[::-1] else False


n = ListNode(1)
curr = n
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(1)
curr = curr.next

print(Solution().isPalindrome(n))
