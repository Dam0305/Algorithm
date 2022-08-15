# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return head
        even = head.next
        node, e = head, even

        while node and e:
            if not e or not e.next:
                node.next = None
                break
            node.next = node.next.next
            e.next = e.next.next
            node = node.next
            e = e.next


        p = head
        while p.next:
            p = p.next

        p.next = even

        return head


arr = [1,1]
# arr = [1,2,3,4,5,6,7,8]
# arr = [1,2,3,4,5]
n1 = ListNode(arr[0])
curr = n1
for i in range(1, len(arr)):
    curr.next = ListNode(arr[i])
    curr = curr.next

p = Solution().oddEvenList(n1)

while p:
    print(p.val)
    p = p.next