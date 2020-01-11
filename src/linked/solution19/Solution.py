from src.linked.ListNode import ListNode
## class
## package
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first_head = head
        second_head = head
        step = 0
        while first_head:
            if step > n:
                second_head = second_head.next
            first_head = first_head.next
            step += 1

        if step == n:
            head = head.next
        else:
            second_head.next = second_head.next.next
        return head

def test1():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution = Solution()
    head = solution.removeNthFromEnd(node1, 2);
    print("========");
    while head:
        print(head.val);
        head= head.next;

def test2():
    node1 = ListNode(1)
    solution = Solution()
    head = solution.removeNthFromEnd(node1, 1);
    print("========");
    while head:
        print(head.val);
        head= head.next;

if __name__ == "__main__":
    test1()