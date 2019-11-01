class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def __get_top(self, to_remove):

        # put all of items from s1 to s2
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())

        # get top item of s2
        top = self.s2.pop()
        if not to_remove:
            self.s1.append(top)

        # put all of items from s2 back to s1
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())

        return top

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.__get_top(True)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.__get_top(False)


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.s1) == 0

def test1():
    obj = MyQueue();
    obj.push(1);
    obj.push(2);
    obj.push(3);
    param_2 = obj.pop();
    print(param_2);
    param_3 = obj.peek();
    print(param_3);
    param_4 = obj.empty();
    print(param_4)

if __name__ == "__main__":
    test1()