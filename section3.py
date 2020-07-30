# 8 変数宣言
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num1 = '1'
new_num = int(num1)
print(new_num, type(new_num))

## 型宣言はできるが上書きできてしまう(var)
num2: int = 1

## 変数の先頭に数字は使えない

# 9 まずはprintで出力
print('Hi', 'Mike', sep=',', end='.\n')

# 10 数値
## terminalだとprintと打たなくて良い
## 17 // 3 整数only
## 17 % 3 余り
## 5 ** 2 べき乗

## round関数
pie = 3.141592
print(round(pie, 2))  # 3.14

## math関数
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)
## help関数 ライブラリを入れるとhelpが出る
print(help(math))

# 11 文字列
##
print("I don't know")
print('I don\'t know')
print("say \"I don\'t know\"")
print('hello.\nHow are you?')
## raw dataという意味のr
print(r'\naaaa\n')

print("############")
print("""\
line1
line2
line3\
""")
print("############")

print('Py' + 'thon')

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)

# 12 文字列のインデックスとスライス
word = 'python'
print(word[0])
print(word[1])
print(word[-1])

print(word[0:2])
print(word[2:])
print(word[:2])

word = 'j' + word[1:]
print(word[:])

n = len(word)
print(n)

# 13 文字のメソッド
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)

print("###############")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

# 14 文字の代入
print('a is {}'.format('a'))
print('a is {0} {1} {2}'.format('a', 'b', 'c'))

print('My name is {name} {family}.'.format(name='Jun', family='Sakai'))

a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')



