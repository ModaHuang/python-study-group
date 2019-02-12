"""
1. 解釋 stack 跟 stack 是什麼? 他們的差別是?

stack : 先進後出
    ↘ ↗
    |-|
    |-|
    |-|
    |_|

stack : 先進先出
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
temp1 = kqueue.kqueue()
temp2 = kqueue.kqueue()

for element in input_list:
    if temp1.size() == 0:
        temp1.push(element)
        for x in temp2.queue:
            temp1.push(x)
        temp2 = kqueue.kqueue()
        # debug("123 temp1.queue", temp1.queue)
        # debug("124 temp2.queue", temp2.queue)
    elif None == temp1.back() or element >= temp1.back():
        temp1.push(element)
        for x in temp2.queue:
            temp1.push(x)
        temp2 = kqueue.kqueue()
        # debug("130 temp1.queue", temp1.queue)
        # debug("131 temp2.queue", temp2.queue)
    else:
        if element <= temp1.front():
            temp2.push(element)
            for x in temp1.queue:
                temp2.push(x)
            temp1 = kqueue.kqueue()
            for x in temp2.queue:
                temp1.push(x)
            temp2 = kqueue.kqueue()
            # debug("141 temp1.queue", temp1.queue)
            # debug("142 temp2.queue", temp2.queue)
        else:
            while element > temp1.front():
                temp2.push(temp1.pop())
                # debug("146 temp1.queue", temp1.queue)
                # debug("147 temp2.queue", temp2.queue)
            else:
                temp2.push(element)
                for x in temp1.queue:
                    temp2.push(x)
                temp1 = kqueue.kqueue()
                for x in temp2.queue:
                    temp1.push(x)
                temp2 = kqueue.kqueue()
                # debug("141 temp1.queue", temp1.queue)
                # debug("142 temp2.queue", temp2.queue)


debug("150 temp1.queue", temp1.queue)
debug("151 temp2.queue", temp2.queue)


temp3 = kstack.kstack()
temp4 = kstack.kstack()

for element in input_list:
    if temp3.size() == 0:
        temp3.push(element)
        for x in temp4.stack:
            temp3.push(x)
        temp4 = kstack.kstack()
        # debug("167 temp3.stack", temp3.stack)
        # debug("168 temp4.stack", temp4.stack)
    elif None == temp3.top() or element >= temp3.top():
        temp3.push(element)
        for x in temp4.stack:
            temp3.push(x)
        temp4 = kstack.kstack()
        # debug("174 temp3.stack", temp3.stack)
        # debug("175 temp4.stack", temp4.stack)
    else:
        if element <= temp3.stack[0]:
            temp4.push(element)
            for x in temp3.stack:
                temp4.push(x)
            temp3 = kstack.kstack()
            for x in temp4.stack:
                temp3.push(x)
            temp4 = kstack.kstack()
            # debug("185 temp3.stack", temp3.stack)
            # debug("186 temp4.stack", temp4.stack)
        else:
            while temp3.size() == 0 or element > temp3.stack[0]:
                temp4.push(temp3.pop())
                if temp3.size() == 0:
                    temp3.push(element)
                # debug("190 temp3.stack", temp3.stack)
                # debug("191 temp4.stack", temp4.stack)
                if element >= temp3.top():
                    temp3.push(element)
                    for x in temp4.stack:
                        temp3.push(x)
                    temp4 = kstack.kstack()
                    break


debug("204 temp3.stack", temp3.stack)
debug("205 temp4.stack", temp4.stack)