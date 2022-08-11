class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        result_node = ListNode()

        p1, p2 = list1, list2
        r = result_node
        while True:
            if not p2:
                while p1:
                    r.next = p1
                    p1 = p1.next
                    r = r.next
                break

            elif not p1:
                while p2:
                    r.next = p2
                    p2 = p2.next
                    r = r.next
                break

            if p1.val < p2.val:
                r.next = p1
                p1 = p1.next
            else:
                r.next = p2
                p2 = p2.next
            r = r.next

        result_node = result_node.next

        return result_node


n1 = ListNode(1)
curr = n1
curr.next = ListNode(2)
curr = curr.next
curr.next = ListNode(4)

n2 = ListNode(1)
curr = n2
curr.next = ListNode(3)
curr = curr.next
curr.next = ListNode(4)
curr = curr.next

p = n2
while p:
    print(p.val)
    p = p.next

print('==')
print(Solution().mergeTwoLists(n1, n2))
n1 = None
n2 = ListNode(0)
result = Solution().mergeTwoLists(n1, n2)
print('==')
p = result
while p:
    print(p.val)
    p = p.next

