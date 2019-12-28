from collections import deque
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cpu = deque()
        ans = 0
        size_of_tasks = len(tasks)
        dict_task_size = {}
        for task in tasks:
            dict_task_size[task] = dict_task_size.get(task,0) + 1

        while True:
            sorted_dict_items = sorted(dict_task_size.items(), key=lambda x: x[1], reverse=True)
            for task in sorted_dict_items:
                if dict_task_size[task[0]] == 0:
                    continue
                cpu.append(task[0])
                ans += 1
                dict_task_size[task[0]] = dict_task_size[task[0]] - 1
                size_of_tasks = size_of_tasks - 1
                if len(cpu) == n+1:
                    break
            if size_of_tasks == 0:
                break
            if len(cpu) <= n:
                ans = ans + n + 1 - len(cpu)
            cpu.clear()
        return ans

def test1():
    tasks = ['A', 'A', 'A', 'B', 'B', 'B']
    n = 2
    solution = Solution()
    ans = solution.leastInterval(tasks, n)
    print(ans)

def test2():
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    solution = Solution()
    ans = solution.leastInterval(tasks, n)
    print(ans)

if __name__ == "__main__":
    test2()
