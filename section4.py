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




