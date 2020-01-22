from src.linked.ListNode import ListNode

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        heap_array = []

        head = ListNode(-1)
        cur = head

        # put the first node from each of the list to heap
        for linked_list in lists:
            if linked_list:
                heap_array.append(linked_list)

        heap_size = len(heap_array)

        # rearrange the node in the heap
        # for each of the node, shift_up
        for cur_index in range(heap_size-1,0,-1):
            to_be_checked = (cur_index - 1)//2
            if heap_array[cur_index].val < heap_array[to_be_checked].val:
                self.swap(heap_array, cur_index, to_be_checked)

        # until lists is empty
        while heap_size > 0:

            # remove the top node from the heap, and then rearrange the heap
            top_node = self.pop_top(heap_array)
            # append the top node to the result linked list
            cur.next = top_node
            cur = top_node
            # if top_node.next is empty, heap_size--, lists size--
            if not top_node.next:
                heap_size -= 1

            # add top_node.next to the linked list, rearrange
            else:
                self.add_node_to_heap(heap_array, top_node.next)

        return head.next

    def add_node_to_heap(self, heap_array, node):
        heap_array.append(node)
        self.shift_up(heap_array, len(heap_array)-1)

    def pop_top(self, heap_array):
        # remove the top node from the heap, and then rearrange the heap
        top_node = heap_array[0]
        heap_array[0] = heap_array[len(heap_array) - 1]
        heap_array.pop()
        self.shift_down(heap_array,0)
        return top_node

    def shift_down(self, heap_array, node_index):
        first_child_index = node_index * 2 + 1
        if first_child_index >= len(heap_array):
            return

        if first_child_index == len(heap_array) - 1:
            if heap_array[node_index].val > heap_array[first_child_index].val:
                self.swap(heap_array, node_index, first_child_index)

        second_child_index = node_index * 2 + 2
        if second_child_index <= len(heap_array) - 1:
            to_be_replaced_index = first_child_index
            if heap_array[first_child_index].val > heap_array[second_child_index].val:
                to_be_replaced_index = second_child_index

            self.swap(heap_array, node_index, to_be_replaced_index)

            self.shift_down(heap_array, to_be_replaced_index)

    def shift_up(self, heap_array, node_index):
        if node_index == 0:
            return
        to_be_checked = (node_index - 1)//2
        if heap_array[node_index].val < heap_array[to_be_checked].val:
            self.swap(heap_array, node_index, to_be_checked)

        self.shift_up(heap_array, to_be_checked)

    def swap(self, heap_array, left, right):
        heap_array[left], heap_array[right] = heap_array[right], heap_array[left]


def test2():
    solution = Solution()
    head = solution.mergeKLists([None])
    print('end')

def test3():

    solution = Solution()
    l11 = ListNode(-8)
    l12 = ListNode(2)
    l13 = ListNode(4)

    l11.next = l12
    l12.next = l13

    l21 = ListNode(-9)
    l22 = ListNode(-9)
    l23 = ListNode(-9)
    l24 = ListNode(-9)
    l25 = ListNode(-8)
    l26 = ListNode(-5)
    l27 = ListNode(-3)
    l28 = ListNode(-2)
    l29 = ListNode(1)

    l21.next = l22
    l22.next = l23
    l23.next = l24
    l24.next = l25
    l25.next = l26
    l26.next = l27
    l27.next = l28
    l28.next = l29

    l31 = ListNode(-9)
    l32 = ListNode(-7)
    l33 = ListNode(-5)
    l34 = ListNode(-3)
    l35 = ListNode(-3)
    l36 = ListNode(-1)
    l37 = ListNode(0)
    l38 = ListNode(3)
    l39 = ListNode(4)

    l31.next = l32
    l32.next = l33
    l33.next = l34
    l34.next = l35
    l35.next = l36
    l36.next = l37
    l37.next = l38
    l38.next = l39

    l41 = ListNode(-9)
    l42 = ListNode(-7)
    l43 = ListNode(-6)
    l44 = ListNode(-6)
    l45 = ListNode(-6)
    l46 = ListNode(-1)
    l47 = ListNode(3)
    l48 = ListNode(4)

    l41.next = l42
    l42.next = l43
    l43.next = l44
    l44.next = l45
    l45.next = l46
    l46.next = l47
    l47.next = l48

    l51 = ListNode(-10)
    l52 = ListNode(-3)
    l53 = ListNode(0)

    l51.next = l52
    l52.next = l53

    l61 = ListNode(-9)
    l62 = ListNode(0)
    l63 = ListNode(4)

    l61.next = l62
    l62.next = l63

    l71 = ListNode(-8)
    l72 = ListNode(-8)

    l71.next = l72

    head = solution.mergeKLists([l11, l21, l31, l41, l51, l61, l71])
    head = head.next
    while head:
        print(head.val)
        head= head.next
    print('end')

def test1():
    solution = Solution()
    l11 = ListNode(1)
    l12 = ListNode(4)
    l13 = ListNode(5)

    l11.next = l12
    l12.next = l13

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l21.next = l22
    l22.next = l23

    l31 = ListNode(2)
    l32 = ListNode(6)
    l31.next = l32
    head = solution.mergeKLists([l11, l21, l31])
    print('end')


if __name__ == '__main__':
    test3()

