from src.linked.ListNode import ListNode
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        first_node = dummy
        second_node = dummy
        while first_node and first_node.next:
            second_node = first_node.next
            if second_node.val == val:
                first_node.next = second_node.next
            else:
                first_node = first_node.next
        return dummy.next

def test1():
    ln1 = ListNode(1)
    ln2 = ListNode(2)
    ln3 = ListNode(6)
    ln4 = ListNode(3)
    ln5 = ListNode(4)
    ln6 = ListNode(5)
    ln7 = ListNode(6)
    ln1.next = ln2
    ln2.next = ln3
    ln3.next = ln4
    ln4.next = ln5
    ln5.next = ln6
    ln6.next = ln7

    solution = Solution()
    head = solution.removeElements(ln1, 6)
    while head:
        print(head.val)
        head = head.next

if __name__ == "__main__":
    test1()