# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        a1, a2 = [], []

        p1, p2 = l1, l2

        while p1:
            a1.append(p1.val)
            p1 = p1.next
        while p2:
            a2.append(p2.val)
            p2 = p2.next


        a1 = int(''.join(list(map(str, a1))[::-1]))
        a2 = int(''.join(list(map(str, a2))[::-1]))

        a1 += a2

        a1 = list(str(a1))[::-1]
        a1 = list(map(int, a1))

        result = ListNode(a1[0])

        p = result
        i = 1
        while i < len(a1):
            p.next = ListNode(a1[i])
            p = p.next
            i+=1

        return result






n1 = ListNode(2)
curr = n1
curr.next = ListNode(4)
curr = curr.next
curr.next = ListNode(3)

n2 = ListNode(5)
curr = n2
curr.next = ListNode(6)
curr = curr.next
curr.next = ListNode(4)



result = Solution().addTwoNumbers(n1, n2)
p = result
while p:
    print(p.val)
    p = p.next