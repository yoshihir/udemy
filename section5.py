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



