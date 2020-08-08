# 31 コメント

"""
test
test
test
"""
# comment
some_value = 100
## コメントは上に書く

# 32 1行が長くなる時
s = 'aaaaaaaaaa' \
    + 'bbbbbbbbbbbb'
print(s)
s = ('aaaaaaaaaa'
     + 'bbbbbbbbbbbb')
## pythonの1行は80文字が目安

# 33 if文
x = - 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
else:
    print('aaaa')

a = 5
b = 10

if a > 0:
    print('a is possible')
    if b > 0:
        print('b is possible')

# 34. デバッガーを使って確認してみる
## step intoとか中身を見る方法の話
# 35. 比較演算子と論理演算子
a = 1
b = 1
a == b
a != b
a < b
a > b
a <= b
a >= b

if a > 0 and b > 0:
    print(1)
if a > 0 or b > 0:
    print(1)

# 36. InとNotの使い所
y = [1, 2, 3]
x = 1

if x in y:
    print(1)

## notは数字比較には使わない
if not a == b:
    print(1)

## notはbooleanでよく使う
is_ok = True
if not is_ok:
    print(1)

# 37. 値が入っていない判定をするテクニック
# False, 0, [], (), {}, set()
is_ok = ''
if is_ok:
    print('OK!')
else:
    print('No!')

# 38. Noneを判定する場合
is_empty = None
if is_empty is not None:
    print('None!!')

## isはオブジェクトの比較を行っている

# 39. while文とcontinue文とbreak文
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while True:
    if count < 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

# 40. while else文
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print('done')

# 41. input関数
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

# 42. for文とbreak文とcontinue文
some_list = [1, 2, 3, 4, 5]

for i in some_list:
    print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

# 43. for else文
## elseはfor終了時に表示される
for fruit in ['apple', 'banana', 'orange']:
    print(fruit)
else:
    print('I')

# 44. range関数
for i in range(10):
    print(i)

for _ in range(10):
    print('hello')

# 45. enumerate関数
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# 46. zip関数
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'te', 'beer']

for day, fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

# 47. 辞書をfor文で処理をする
d = {'x': 100, 'y': 200}

for k, v in d.items():
    print(k, ':', v)


# 48. 関数定義
def say_someting():
    s = 'hi'
    return s


result = say_someting()
print(result)


def what_is_this(color):
    if color == 'red':
        return 'tomoto'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
result = what_is_this('green')
result = what_is_this('yellow')
print(result)


# 49. 関数の引数と返り値の宣言
## 下記のように宣言ができるけど、stringを渡せてしまう
def add_num(a: int, b: int) -> int:
    return a + b


r = add_num(10, 20)
print(r)


# 50. 位置引数とキーワード引数とデフォルト引数
def menu(entree='beef', drink='wine', dessert='ice'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)


menu(entree='chicken')


# 51. デフォルト引数で気をつけること
## listやdictionaryなどの参照渡し系は関数で渡さない
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func(100)
print(r)

r = test_func(100)
print(r)


# 52. 位置引数のタプル化
## *argでタプルにして渡せる
def say_something(*args):
    for arg in args:
        print(arg)


say_something('Hi', 'Mike', 'Nance')


# 53. キーワード引数の辞書化
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


menu(entree='beef', drink='coffee')


# d = {
#     'entree': 'beef',
#     'drink': 'ice coffee',
#     'dessert': 'ice'
# }
# menu(**d)


# 54. Docstringsとは
def example_func(param1, param2):
    """Example function with type

    Args:
        prams1 (int): The fist
        prams2 (int): The second

    Returns:
        bool: The
    """
    print(param1)
    print(param2)
    return True


print(example_func.__doc__)


# 55. 関数内関数
## この関数内だけで使う関数は inner functionとして中に書く
def outer(a, b):
    def plus(c, d):
        return c + d

    r = plus(a, b)
    print(r)


outer(1, 2)


# 56. クロージャー
def outer2(a, b):
    def inner():
        return a + b

    return inner


## この時点では実行されない
f = outer2(1, 2)
## ()付きのときに初めて実行される
r = f()
print(r)


# 57. デコレーター
## @functionをつけると56のように()付きで実行をやらなくて済む
## @を2個書くこともできる

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func', func.__name__)
        print('args', args)
        print('kwargs', kwargs)
        result = func(*args, **kwargs)
        print('result', result)
        return result

    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result

    return wrapper


@print_info
@print_more
def add_num(a, b):
    return a + b


r = add_num(10, 20)
print(r)

# 58. ラムダ
## こんな感じで1行で書ける
## def sample_func(word):
##     return word.capitalize()
# ↓
## sample_func = lambda word: word.capitalize()

l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

sample_func = lambda word: word.capitalize()

change_words(l, sample_func)

# 59. ジェネレーター

