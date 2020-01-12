from src.linked.ListNode import ListNode
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow_head = head
        quick_head = head
        while quick_head and quick_head.next:
            quick_head = quick_head.next.next
            slow_head = slow_head.next
            if quick_head == slow_head:
                break
        if not quick_head or not quick_head.next:
            return None
        first_end = quick_head
        second_end = head
        while first_end != second_end:
            first_end = first_end.next
            second_end = second_end.next
        return first_end

def test1():
    listNode1 = ListNode(3)
    listNode2 = ListNode(2)
    listNode3 = ListNode(0)
    listNode4 = ListNode(-4)

    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    listNode4.next = listNode2
    solution = Solution()
    head = solution.detectCycle(listNode1)
    print(head.val)

if __name__ == "__main__":
    test1()