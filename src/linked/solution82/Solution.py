from src.linked.ListNode import ListNode
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # for each node, loop from node.next (as loop_node) until loop_node.val != node.val
        # if node.next != loop_node, node.next=loop_node
        dummy = ListNode(-1)
        dummy.next = head
        cur_node = dummy
        while cur_node.next:
            loop_node = cur_node.next
            if not loop_node.next:
                break
            else:
                loop_node = loop_node.next
            loop_var = cur_node.next.val
            while loop_node and loop_node.val == loop_var:
                loop_node = loop_node.next

            if cur_node.next.next != loop_node:
                cur_node.next = loop_node
            else:
                cur_node = cur_node.next
        return dummy.next

def test1():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node31 = ListNode(3)
    node4 = ListNode(4)
    node41 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node31
    node31.next = node4
    node4.next = node41
    node41.next = node5
    solution = Solution()
    head = solution.deleteDuplicates(node1);
    print("========");
    while head:
        print(head.val);
        head= head.next;

if __name__ == "__main__":
    test1()
