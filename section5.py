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


