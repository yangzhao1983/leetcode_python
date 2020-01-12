from src.linked.ListNode import ListNode
class Solution(object):
    def __init__(self):
        self.reversed_head = None

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        else:
            self.do_reverse(head)

        head.next = None
        return self.reversed_head

    def do_reverse(self, head):
        if head.next:
            reversed_tail = self.do_reverse(head.next)
            reversed_tail.next = head
        else:
            self.reversed_head = head
        return head

def test1():
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(3)
    ln4 = ListNode(4)
    ln5 = ListNode(5)

    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5

    solution = Solution()
    head = solution.reverseList(ln1)
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    test1()