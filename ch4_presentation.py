def debug(variable_name, variable):
    print(variable_name, "=", variable, "\n    type =", type(variable))

# # 註解 : # 與 '''
# print("我是第一行")
# print("我是第二行")
# print("我是第三行")
# print("我是第四行")
# print("我是第五行")


# # 用 \ 來延續多行
# paragraph1 = '''
# Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
# In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
# Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
# '''
# print("paragraph1 : ", paragraph1)
#
# paragraph2 = '''
# Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side \
# data as well.
# In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one \
# doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause \
# a data write. However, it's useful to establish a convention that any operations that cause writes should be sent \
# explicitly via a mutation.
# Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful\
# for fetching the new state of an object after an update.
# '''
# print("paragraph2 : ", paragraph2)


# # if 與 else，與縮排
# flag = True
# if flag:
#     print("我是 True 的第一行!")
#     print("我是 True 的第二行!")
#     print("我是 True 的第三行!")
# else:
#     print("我是 False 的第一行!")
#     print("我是 False 的第二行!")
#     print("我是 False 的第三行!")


# # elif
# color = "moda"
# if color == "red":
#     print("It's a tomato")
# elif color == "green":
#     print("It's a green pepper")
# elif color == "bee purple":
#     print("I don't know what it is, but only bees can see it")
# else:
#     print("I've never heard of the color", color)


# # 各種運算子
# equality ==
# inequality !=
# less than <
# less than or equal <=
# greater than >
# greater than or equal >=
# membership in ...
# x = 9
# print("x =", x)
# print("x == 5,", x == 5)
# print("x == 7,", x == 7)
# print("5 < x,", 5 < x)
# print("x < 5,", x < 5)
# print("x in (1, 3, 5, 7),", x in (1, 3, 5, 7))
# # ===== 分隔線 ==== 若 if 順序寫錯了
# x = 9
# if x < 0:
#     print("x 是負數")
# elif x == 0:
#     print("x = 0")
# elif x < 10:
#     print("x 是一位數")
# elif x < 100:
#     print("x 是二位數")
# elif x < 1000:
#     print("x 是三位數")
# else:
#     print("x 是四位數以上")
#
# if x < 0:
#     print("x 是負數")
# elif x == 0:
#     print("x = 0")
# elif x < 100:
#     print("x 是二位數")
# elif x < 10:
#     print("x 是一位數")
# elif x < 1000:
#     print("x 是三位數")
# else:
#     print("x 是四位數以上")


# # 什麼是 True (精確的說法是 "什麼不是 False")
# boolean False
# null None
# zero integer 0
# zero float 0.0
# empty string ''
# empty list []
# empty tuple ()
# empty dict {}
# empty set set()
#
# # "非 False" 就會被當成 True
# flag = {}
# if flag:
#     print("我是 True 的第一行!")
#     print("我是 True 的第二行!")
#     print("我是 True 的第三行!")
# else:
#     print("我是 False 的第一行!")
#     print("我是 False 的第二行!")
#     print("我是 False 的第三行!")


# # while : 重複做類似的事

# # 題目 : 從 1 print 到 5
# # hardcode : 但如果要你 print 到 10000 呢?
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
#
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
# # print("我是 while 區塊外的 count, count =", count)

# # while : break
# while True:
#     stuff = input("String to capitalize [type q to quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())

# # while : continue
# while True:
#     value = input("Integer, please [q to quit]: ")
#     if value == "q":
#         break
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, "squared is", number * number)
#
# # 題目 : 從 1 print 到 5，但跳過偶數
# count = 1
# while count <= 11:
#     if count % 2 == 0:
# #        count += 1
#         continue
#     print(count)
#     count += 1

# # while : else
# numbers = [1, 3, 5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('Found even number', number)
#         break
#     position += 1
# else: # break not called
#     print('No even number found')


# # for

# rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
# print(rabbits[0])
# print(rabbits[1])
# print(rabbits[2])
# print(rabbits[3])
#
# current = 0
# while current < len(rabbits):
#     print(rabbits[current])
#     current += 1
#
# for rabbit in rabbits:
#     print(rabbit)
# # ===== 分隔線 ====
# word = 'cat'
# for letter in word:
#     print(letter)
#
# current = 0
# while current < len(word):
#     print(word[current])
#     current += 1
#
# # hardcore 做法
# print(word[0])
# print(word[1])
# print(word[2])


# # ===== 分隔線 ==== 對 dict 迭代
# accusation = {'room': 'ballroom',
#               'weapon': 'lead pipe',
#               'person': 'Col. Mustard'}
#
# debug("accusation", accusation)
# for card in accusation:  # or, for card in accusation.keys():
#     print(card)
#
# debug("accusation.values()", accusation.values())
# for value in accusation.values():
#     print(value)
#
# debug("accusation.items()", accusation.items())
# for item in accusation.items():
#     print(item)
#
# debug("accusation.items()", accusation.items())
# for card, contents in accusation.items():
#     print('Card', card, 'has the contents', contents)


# # for 也有 break 跟 continue

# # for : else - 若沒執行 break 才執行 else
# cheeses = ['a']
# for cheese in cheeses:
#     print('This shop has some lovely', cheese)
#     break
# else: # no break means no cheese
#     print('This is not much of a cheese shop, is it?')


# # zip()
# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# debug("zip(days, fruits, drinks, desserts)", zip(days, fruits, drinks, desserts))
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)
#
# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'
# debug("list(zip(english, french))", list(zip(english, french)))
# debug("dict(zip(english, french))", dict(zip(english, french)))


# # range( start, stop, step )
# for x in range(0,3):
#     print(x)
#
# for x in range(2, -1, -1):
#     print(x)
#
# for x in range(0, 11, 2):
#     print(x)


# # 生成式

# # 串列生成式
# 一次一個
# number_list = []
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# number_list.append(4)
# number_list.append(5)
# debug("number_list", number_list)
#
# 用 for 跟 range()
# number_list = []
# for number in range(1, 6):
#     number_list.append(number)
# debug("number_list", number_list)
#
# 用 list()
# number_list = list(range(1, 6))
# debug("number_list", number_list)
#
# python style
# number_list = [number for number in range(1,6)]
# debug("number_list", number_list)
#
# number_list = [number-1 for number in range(1,6)]
# debug("number_list", number_list)
#
# number_list = [number for number in range(1,6) if number % 2 == 1]
# debug("number_list", number_list)
#
# 用 for 實作
# a_list = []
# for number in range(1,6):
#     if number % 2 == 1:
#         a_list.append(number)
# debug("a_list", a_list)
#
# # 雙層 for 迴圈
# rows = range(1,4)
# cols = range(1,3)
# for row in rows:
#     for col in cols:
#         print(row, col)
#
# python style
# rows = range(1,4)
# cols = range(1,3)
# cells = [(row, col) for row in rows for col in cols]
# debug("cells", cells)
# for cell in cells:
#     print(cell)
# # tuple unpacking
# for row, col in cells:
#     print(row, col)


# # 字典生成式
word = 'abbcccddddeeeee'
# letter_counts = {letter: word.count(letter) for letter in word}
# debug("letter_counts", letter_counts)
#
# 用 for 實作
# letter_counts = {}
# for letter in word:
    # debug("letter", letter)
    # debug("word.count("+letter+")", word.count(letter))
    # letter_counts[letter] = word.count(letter)
    # # letter_counts['a'] = 1
    # # letter_counts['b'] = 2
    # debug("letter_counts", letter_counts)
# debug("letter_counts", letter_counts)
#
# # 不重複跑的寫法 (例如本來 'd' 會跑三次)
# letter_counts = {letter: word.count(letter) for letter in set(word)}
# debug("letter_counts", letter_counts)


# # 集合生成式
# a_set = {number for number in range(1,6) if number % 3 == 1}
# debug("a_set", a_set)

# tuple 沒有生成式，同樣語法會變成 "產生器生成式"，p105 會講到
# number_thing = (number for number in range(1, 6))


# # function
# def commentary(color):
#     if color == "red":
#         print("It's a tomato")
#     elif color == "green":
#         print("It's a green pepper")
#     elif color == "bee purple":
#         print("I don't know what it is, but only bees can see it")
#     else:
#         print("I've never heard of the color", color)
#
#
# comment = commentary('bee purple"')
# debug("comment", comment)


# # 題外話 : None 與 False 是不一樣的
# def is_none(thing):
#     if thing is None:
#         print("It's None")
#     elif:
#         print("It's True")
#     else:
#         print("It's False")
#
# is_none(None)
# is_none(True)
# is_none(False)
# is_none(0)
# is_none(0.0)
# is_none(())
# is_none([])
# is_none({})
# is_none(set())

# # 引數類型
# def menu(wine, entree, dessert):
#     return {'wine':wine,'entree':entree,'dessert':dessert }
#
#
# # 位置引數
# debug("menu('chardonny','chichen','cake')", menu('chardonny','chichen','cake'))
# # 關鍵字引數
# menu(entree='beef', dessert='bagel', wine='bordeaux')
# debug("menu(entree='beef', dessert='bagel', wine='bordeaux')", menu(entree='beef', dessert='bagel', wine='bordeaux'))
# # 混合著用 : 位置引數必須放前面
# debug("menu('frontenac', dessert='flan', entree='fish')", menu('frontenac', dessert='flan', entree='fish'))
# # 指定預設參數值
# def menu(wine, entree, dessert='pudding'):
#     return {'wine': wine, 'entree': entree, 'dessert': dessert}
#
#
# menu('chardonnay', 'chicken')
# debug("menu('chardonnay', 'chicken')", menu('chardonnay', 'chicken'))
# menu('dunkelfelder', 'duck', 'doughnut')
# debug("menu('dunkelfelder', 'duck', 'doughnut')", menu('dunkelfelder', 'duck', 'doughnut'))


# # 預設引數是 list 或 dist 時會遇到的 bug
# def buggy(arg, result=[]):
#     result.append(arg)
#     print(result)
#
#
# buggy('a', ['c'])
# buggy('a')
# buggy('b')  # expect ['b']
#
# # 這樣才會清掉 result
# def works(arg):
#     result = []
#     result.append(arg)
#     return result
#
#
# debug("works('a')", works('a'))
# debug("works('b')", works('b'))
#
# # 但上面就無法在第二個引數丟 list 進去了
# def nonbuggy(arg, result=None):
#     if result is None:
#         result = []
#     result.append(arg)
#     print(result)
#
#
# nonbuggy('a', ['c'])
# nonbuggy('a')
# nonbuggy('b')


# # 用 * 來收集位置引數 - 不限定長度
# def print_args(*args):  # 會存成 tuple
#     print('Positional argument tuple:', args)
#
#
# print_args(3, 2, 1, 'wait!', 'uh...')

# # 也可以用來抓取剩下的引數
# def print_more(required1, required2, *args):
#     print('Need this one:', required1)
#     print('Need this one too:', required2)
#     print('All the rest:', args)
#
#
# print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')


# # 用 ** 來收集關鍵字引數 - 不限定長度
# def print_kwargs(**kwargs):
#     print('Keyword arguments:', kwargs)
#
#
# print_kwargs(wine='merlot', entree='mutton', dessert='macaroon')


# # 文件字串
# def echo(anything):
#     'echo returns its input argument'
#     return anything
#
#
# def print_if_true(thing, check):
#     '''
#     Prints the first argument if a second argument is true.
#     The operation is:
#         1. Check whether the *second* argument is true.
#         2. If it is, print the *first* argument.
#     '''
#     if check: print(thing)
#
#
# help(echo)
# print(echo.__doc__)
#
# help(print_if_true)
# print_if_true(word, True)


# # 把 function 當引數，丟給另一個 function
# def answer():
#     print(42)
#
#
# # answer()
#
#
# def run_something(func):
#     func()
#
#
# # run_something(answer)
# # run_something(answer())
# # debug("run_something", run_something)

# # ===== 分隔線 =====
# def add_args(arg1, arg2):
#     print(arg1 + arg2)
#
#
# def run_something_with_args(func, arg1, arg2):
#     func(arg1, arg2)
#
#
# run_something_with_args(add_args, 5, 9)
# run_something_with_args(debug, 5, 9)


# # 跟 *args 與 **kwargs 結合
# def sum_args(*args):
#     return sum(args)
#
#
# def run_with_positional_args(func, *args):
#     return func(*args)
#
#
# run_with_positional_args(sum_args, 1, 2, 3, 4)
# debug("run_with_positional_args(sum_args, 1, 2, 3, 4)", run_with_positional_args(sum_args, 1, 2, 3, 4))


# # 內部函式
# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)
#
#
# debug("outer(4, 7)", outer(4, 7))


# # Closure
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2
#
#
# a = knights2('Duck')
# b = knights2('Hasenpfeffer')
#
# debug("a", a)
# debug("b", b)
#
# debug("a()", a())
# debug("b()", b())


# # 匿名函式 : lambda() - Javascript 也有，但我不太懂用在哪
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
#
# def enliven(word):  # give that prose more punch
#     return word.capitalize() + '!'
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
# edit_story(stairs, enliven)
# edit_story(stairs, lambda word: word.capitalize() + '!')


# # 產生器 - 好像只能給 for 用，其他用法我也不知道
# 實作 range()
# def my_range(first=0, last=10, step=1):
#     number = first
#     while number < last:
#         yield number
#         number += step
#
#
# debug("my_range", my_range)
#
# ranger = my_range(1, 5)
# debug("ranger", ranger)
#
# for x in ranger:
#     print(x)

# # 裝飾器
# def document_it(func):
#     def new_function(*args, **kwargs):
#         print('Running function:', func.__name__)
#         print('Positional arguments:', args)
#         print('Keyword arguments:', kwargs)
#         result = func(*args, **kwargs)
#         print('Result:', result)
#         return result
#     return new_function
#
#
# def square_it(func):
#     def new_function(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * result
#     return new_function
#
#
# def add_ints(a, b):
#     return a + b
#
#
# cooler_add_ints = document_it(add_ints)  # manual decorator assignment
# cooler_add_ints(3, 5)
#
# cooler_debug = document_it(debug)
# cooler_debug(3, 5)
#
# @square_it
# @document_it
# def add_ints(a, b):
#     return a + b
#
#
# add_ints(3, 5)


# # 命名空間與範圍
# animal = 'fruitbat'
#
# # function 可以讀全域變數
# def print_global():
#     print('inside print_global:', animal)
#
#
# print('at the top level:', animal)
# print_global()
#
#
# # 但 function 無法改變全域變數的值(除非用關鍵字 global)
# def change_and_print_global():
#     print('inside change_and_print_global:', animal)
#     animal = 'wombat'
#     print('after the change:', animal)
#
#
# change_and_print_global()
#
#
# # 即使全域變數跟區域變數，變數名字一樣，也是不同的物件
# def change_local():
#     animal = 'wombat'
#     print('inside change_local:', animal, id(animal))
#
# change_local()
# debug("animal", animal)
# debug("id(animal)", id(animal))


# # 用 global 去改變全域變數的值
# animal = 'fruitbat'
# def change_and_print_global():
#     global animal
#     animal = 'wombat'
#     print('inside change_and_print_global:', animal)
#
#
# debug("animal", animal)
# change_and_print_global()
# debug("animal", animal)


# # locals() 與 globals()
# animal = 'fruitbat'
#
#
# def change_local():
#     animal = 'wombat' # local variable
#     print('locals:', locals())
#
#
# debug("animal", animal)
# change_local()
# print('globals:', globals())  # reformatted a little for presentation


# # 在名稱中使用 _ 與 __
# def amazing():
#     '''This is the amazing function.
#     Want to see it again?'''
#     print('This function is named:', amazing.__name__)
#     print('And its docstring is:', amazing.__doc__)
#
#
# amazing()


# # try 與 expect
# short_list = [1, 2, 3]
# position = 5
# # try:
# #     short_list[position]
# # except:
# # #     print('Need a position between 0 and', len(short_list)-1, ' but got', position)
#
#
# short_list = [1, 2, 3]
# while True:
#     value = input('Position [q to quit]? ')
#     if value == 'q':
#         break
#     try:
#         position = int(value)
#         print(short_list[position])
#     except IndexError as err:
#         print('Bad index:', position)
#     except Exception as other:
#         print('Something else broke:', other)


# # # 製作你自己的例外 - ch6 類別看完再回來看
# class UppercaseException(Exception):
#     pass
#
#
# words = ['eeenie', 'meenie', 'miny', 'MO']
# for word in words:
#     if word.isupper():
#         raise UppercaseException(word)
#
# try:
#     raise OopsException('panic')
# except OopsException as exc:\
#     print(exc)
