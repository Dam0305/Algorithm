# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """

        if not head or left == right:
            return head

        root = start = ListNode(None)
        root.next = head
        for _ in range(left-1):
            start = start.next
        end = start.next

        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next





#arr = [1,2,3,4,5]
# arr = [5]
# arr = [1,2,3]
arr = [3,5]
left, right = 1,2
n1 = ListNode(arr[0])
curr = n1
for i in range(1, len(arr)):
    curr.next = ListNode(arr[i])
    curr = curr.next

p = Solution().reverseBetween(n1, left, right)

while p:
    print(p.val)
    p = p.next
