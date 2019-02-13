"""
1. 解釋 stack 跟 stack 是什麼? 他們的差別是?
stack : 先進後出
    ↘ ↗
    |-|
    |-|
    |-|
    |_|
queue : 先進先出
     ↑
    |-|
    |-|
    |-|
    |-|
     ↑
"""

"""
2. 實做一個stack class kstack, 並提供 kstack.push(), kstack.pop(), kstack.size(), kstack.front(), kstack.back() 的功能
"""


# class kqueue():
#     def __init__(self):
#         self.queue = list()
#
#     def push(self, element):
#         self.queue.append(element)
#         return self.queue
#
#     def pop(self):
#         if len(self.queue) != 0:
#             pop_element = self.queue[0]
#             del self.queue[0]
#             return pop_element
#         else:
#             return None
#
#     def size(self):
#         return len(self.queue)
#
#     def front(self):
#         if len(self.queue) != 0:
#             return self.queue[0]
#         else:
#             return None
#
#     def back(self):
#         if len(self.queue) != 0:
#             return self.queue[-1]
#         else:
#             return None


"""
3. 實做一個stack class kstack, 並提供 kstack.push(), kstack.pop(), kstack.size(), kstack.top() 的功能
"""


# class kstack():
#     def __init__(self):
#         self.stack = list()
#
#     def push(self, element):
#         self.stack.append(element)
#         return self.stack
#
#     def pop(self):
#         if len(self.stack) != 0:
#             pop_element = self.stack[-1]
#             del self.stack[-1]
#             return pop_element
#         else:
#             return None
#
#     def size(self):
#         return len(self.stack)
#
#     def top(self):
#         if len(self.stack) != 0:
#             return self.stack[-1]
#         else:
#             return None

"""
4. 將上面兩個分別打包成 ktool 的 module
"""

from ktool import kqueue, kstack

kqueue1 = kqueue.kqueue()
kstack1 = kstack.kstack()


"""
5. 分別使用 ktool 裡的 kstack 及 kstack 對 [2,3,1,9,22,31,8,7,45,9] 由小到大做排序
"""


def debug(variable_name, variable):
    print(variable_name, "=", variable, "\n    type =", type(variable))


input_list = [2, 3, 1, 9, 22, 31, 8, 7, 45, 9]
debug("input_list", input_list)

kqueue1 = kqueue.kqueue()
kqueue_temp = kqueue.kqueue()

for element in input_list:
    if kqueue1.size() == 0 or element >= kqueue1.back():
        kqueue1.push(element)

    else:
        if element <= kqueue1.front():
            kqueue_temp.push(element)

            for x in kqueue1.queue:
                kqueue_temp.push(x)
            kqueue1 = kqueue.kqueue()

            for x in kqueue_temp.queue:
                kqueue1.push(x)
            kqueue_temp = kqueue.kqueue()

        else:
            while element > kqueue1.front():
                kqueue_temp.push(kqueue1.pop())

            else:
                kqueue_temp.push(element)

                for x in kqueue1.queue:
                    kqueue_temp.push(x)
                kqueue1 = kqueue.kqueue()

                for x in kqueue_temp.queue:
                    kqueue1.push(x)
                kqueue_temp = kqueue.kqueue()


debug("kqueue1.queue", kqueue1.queue)
# debug("kqueue_temp.queue", kqueue_temp.queue)


kstack1 = kstack.kstack()
kstack_temp = kstack.kstack()

for element in input_list:
    if kstack1.size() == 0 or element >= kstack1.top():
        kstack1.push(element)

    else:
        if element <= kstack1.stack[0]:
            kstack_temp.push(element)

            for x in kstack1.stack:
                kstack_temp.push(x)
            kstack1 = kstack.kstack()

            for x in kstack_temp.stack:
                kstack1.push(x)
            kstack_temp = kstack.kstack()

        else:
            while kstack1.size() == 0 or element > kstack1.stack[0]:
                kstack_temp.push(kstack1.pop())
                if kstack1.size() == 0:
                    kstack1.push(element)

                if element >= kstack1.top():
                    kstack1.push(element)
                    while kstack_temp.size() != 0:
                        kstack1.push(kstack_temp.pop())
                    kstack_temp = kstack.kstack()
                    break


debug("kstack1.stack", kstack1.stack)
# debug("kstack_temp.stack", kstack_temp.stack)