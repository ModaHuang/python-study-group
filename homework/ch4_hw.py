"""
1.1 分別寫出四個function可以印出字元'K', 'D', 'A', 'Y', 請使用迴圈寫, 不是直接把答案印出
*       *
*     *
*   *
* * *
*     *
*       *
*        *
"""
def print_letter_K():
    for layer in range(1, 9):
        if layer <= 4:
            spaces = " " * (4 - layer)
        elif layer > 4:
            spaces = " " * (layer - 5)
        print("*" + spaces + "*")
    else:
        print("\n")


def print_letter_D():
    for layer in range(1, 9):
        if layer <= 4:
            spaces = " " * (layer - 1)
        elif layer > 4:
            spaces = " " * (8 - layer)
        print("*" + spaces + "*")
    else:
        print("\n")


def print_letter_A():
    for layer in range(1, 9):
        spaces1 = " " * (8 - layer)
        spaces2 = " " * ((layer - 2) * 2 + 1)
        if layer == 1:
            print(spaces1 + "*")
        elif layer == 5:
            stars = "*" * ((layer - 2)*2 + 1)
            print(spaces1 + "*" + stars + "*")
        else:
            print(spaces1 + "*" + spaces2 + "*")
    else:
        print("\n")


def print_letter_Y():
    for layer in range(1, 9):
        if layer <= 4:
            spaces1 = " " * (layer - 1)
            spaces2 = " " * (9 - 2*layer)
            print(spaces1 + "*" + spaces2 + "*")
        elif layer > 4:
            spaces = " " * 4
            print(spaces + "*")
    else:
        print("\n")


print("Q1.1 :")
print_letter_K()
print_letter_K()
print_letter_D()
print_letter_A()
print_letter_Y()


"""
1.2 多加一個function可以印出一棵聖誕樹, 使用上面的 function 印出 KKDAY 跟聖誕樹
           *
           |
          ***
           |
         *****
           |
        *******
           |
       *********
           |
      ***********
           |
     *************
           |
    ***************
           |
   *****************
           |
  *******************
           |
 *********************
           |
"""


def print_xmas_tree(layers):
    for layer in range(1, layers + 1):
        spaces = " " * (layers - layer)
        stars = "*" * (layer*2 - 1)
        print(spaces + stars)
        print((" " * (layers - 1)) + "|")


print("Q1.2 :")
print_letter_K()
print_letter_K()
print_letter_D()
print_letter_A()
print_letter_Y()
print_xmas_tree(10)


"""
1.3 印個花樣多一點的聖誕樹
          []
         [~~]
        [~~~~]
       [~~~~~~]
      [~~~~~~~~]
     [~~~~~~~~~~]
    [~~~~~~~~~~~~]
   [~~~~~~~~~~~~~~]
  [~~~~~~~~~~~~~~~~]
 [__________________]
          []
          []
"""


def print_xmax_tree_2():
    for layer in range(1, 11):
        space1 = " " * (10 - layer)
        space2 = "~" * (2*(layer - 1))
        print(space1 + "[" + space2 + "]")
    else:
        space1 = " " * (10 - 1)
        print(space1 + "[]")
        print(space1 + "[]")


print("Q1.3 :")
print_xmax_tree_2()


"""
2. 使用迴圈找出 300 以下的質數
"""


prime_number = list()

for number in range(2, 301):
    for divisor in range(2, number):
        if (number % divisor) == 0:
            break
    else:
        prime_number.append(number)

print("Q2 :")
print(prime_number)


"""
3. 費氏數列, f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2)
列出f(20)的完整費氏數列
0 1 1 2 .... f(20)
"""


def fibonacci_number(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci_number(number - 1) + fibonacci_number(number - 2)


fibonacci_number_list = list()

for integer in range(0, 21):
    fibonacci_number_list.append(fibonacci_number(integer))

print("Q3 :")
print(fibonacci_number_list)

"""
4. 四位數中，使用迴圈找出 0 ~ 7 所能組成的奇數個數
"""

odd_list = list()

for thousand in range(0, 8):
    for hundreds in range(0, 8):
        for ten in range(0, 8):
            for digits in range(0, 8):
                number = (1000 * thousand) + (100 * hundreds) + (10 * ten) + digits
                if number % 2 == 0:
                    continue
                else:
                    number_to_str = str(thousand) + str(hundreds) + str(ten) + str(digits)
                    odd_list.append(number_to_str)

print("Q4 :")
print(odd_list)