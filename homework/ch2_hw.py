# -*- coding: utf-8 -*-

paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

print(paragraph)

# Q1: 印出這個段落的長度
len(paragraph)

# Q2: 把文章裡 'GraphQL' 這個單字變全大寫, 其餘單字變全小寫
paragraph_lower = paragraph.lower()
paragraph_lower_replace = paragraph_lower.replace('graphql', 'GRAPHQL')
print(paragraph_lower_replace)

# Q3: 印出這個段落有多少個英文單字(不含標點符號與空白)
paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

paragraph_replace = paragraph.replace('-', ' ')
len(paragraph_replace.split())

# Q4: x = 1, y = 6, 把兩個變數的值交換, 讓他變成 x = 6, y = 1, 只能使用加減乘除, 不能使用第三個變數
x = 1
y = 6
print ('x =',x,', y =',y)
x = x + 5
y = y - 5
print ('x =',x,', y =',y)