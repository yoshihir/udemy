# 16 リスト型

l = [1, 20, 4, 30]
print(l)

print(l[1])
print(l[0:2])

len(l)
print(list('abcdefg'))

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
print(n[::-1])

a = ['a', 'b', 'c']
b = [1, 2, 3]
x = [a, b]
print(x)
print(x[0][1])

# 17 リストの操作

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
## 配列は上書きできる
s[0] = 'X'
print(s)

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n.append(100)
print(n)
n.insert(0, 200)
print(n)

n.pop(0)
print(n)

del n[0]
print(n)

n.remove(2)
print(n)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

x = a + b
print(x)

a += b
print(a)

a.extend(b)
print(a)

# 18 リストのメソッド
r = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(r.index(3))
print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

x = ''.join(to_split)
print(x)

print(help(list))

# 19 リストのコピー
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
y[0] = 100
print('y =', y)
print('x =', x)

# 20 リストの使い所
seat = []
min = 0
max = 5

print(min <= len(seat) < max)
seat.append('p')
print(min <= len(seat) < max)
seat.pop()
print(min <= len(seat) < max)

# 21 タプル型
t = (1, 2, 3, 4, 5)
print(help(tuple))
## appendやpopがないlistのイメージ

t = ([1, 2, 3], [4, 5, 6])
print(t)

# 22 タプルのアンパッキング
num_tuple = (10, 20)
x, y = num_tuple
print(x, y)

min, max = 0, 100
print(min, max)

a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# 23 タプルの使い所
## appendとかされたくないところで使う(valのイメージ)

# 24 辞書型

