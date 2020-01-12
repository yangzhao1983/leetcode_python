from src.linked.ListNode import ListNode
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        reversed_head = head
        forward_head = head.next

        while forward_head:
            tmp_head = forward_head
            forward_head = forward_head.next
            tmp_head.next = reversed_head
            reversed_head = tmp_head

        head.next = None
        return reversed_head


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