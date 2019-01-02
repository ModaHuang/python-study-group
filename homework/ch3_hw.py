"""
1. The elements of a list are mutable whereas the elements of a tuple are immutable.
2. When we do not want to change the data over time, the tuple is a preferred data type whereas when we need to change the data in future, list would be a wise option.
3. Iterating over the elements of a tuple is faster compared to iterating over a list.
4. Elements of a tuple are enclosed in parenthesis whereas the elements of list are enclosed in square bracket.
"""

# Q1:
data1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even = {2, 4, 6, 8, 10}
# find the odd numbers in data1 and represents as a set odd. print(odd)

odd = set()
for number in data1:
    if number % 2 == 1:
        odd.add(number)
print("Q1 \n odd =", odd)


# Q2:
data2 = ('moda', ('走', '了'), ('買', '肥宅', '歡樂水'))
# find the index of '歡樂水' in data2 and print '歡樂水', print(data2...)

print("Q2 \n", data2[2][2])


# Q3:
data3 = {39, 12, 61, 10, 3, 99, 78, 87, 93, 11, 666, 999}
# 3.1 計算data3所有數字的總和
# 3.2 找出data3內最大的數字, data3_max, 及最小的數字 data3_min, print(data3_max), print(data3_min)
# 3.3 分別將 data3 的數字由大到小排序 print(data_desc), 由小到大排序 print(data_asc)

print("Q3.1 \n sum =", sum(data3))

print("Q3.2 \n max =", max(data3), "\n min =", min(data3))

data3_sorted = sorted(data3)
data3_sorted_reverse = sorted(data3, reverse=True)
print("Q3.3 \n sorted =", data3_sorted, "\n sorted_reverse =", data3_sorted_reverse)

# Q4:
data4 = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
# 4.1 將'moda'換成'米血', 並將data4 轉成字串, 印出 '米血走了~ 買肥宅歡樂水'
# 4.2 將data4轉成字串, 順序跟原本的data4相反, 印出 '歡樂水肥宅買~ 了走moda'

if 'moda' in data4:
    data4[data4.index('moda')] = '米血'
print("Q4.1 \n ", ''.join(data4))

data4 = ['moda', '走', '了', '~ ', '買', '肥宅', '歡樂水']
data4_sorted_reverse = []
count = -1
while count >= (0 - len(data4)):
    data4_sorted_reverse.append(data4[count])
    count = count - 1
print("Q4.2 \n ", ''.join(data4_sorted_reverse))